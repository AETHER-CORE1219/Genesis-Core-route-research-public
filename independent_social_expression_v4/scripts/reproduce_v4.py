#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
import subprocess
import sys
from collections import Counter
from pathlib import Path
from statistics import NormalDist

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DECIDED = {"SUPPORTED", "NO_DIRECT_ANCHOR_OBSERVED_IN_ADEQUATE_FIXED_SOURCE"}
UNDECIDED = {
    "PARTIAL",
    "UNKNOWN_NO_ANALYSIS_ELIGIBLE_EVIDENCE",
    "UNKNOWN_SEMANTIC_OR_ACTOR",
}
ROW_KEYS = {"release_id", "fixed_stratum", "family_exposure", "endpoint_state"}
Z95 = 1.6448536269514722
Z80 = NormalDist().inv_cdf(0.80)


def load_json(relative: str):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def load_json_gz(relative: str):
    with gzip.open(ROOT / relative, "rt", encoding="utf-8") as handle:
        return json.load(handle)


def close(actual: float, expected: float, tolerance: float = 1e-12) -> None:
    assert math.isclose(actual, expected, rel_tol=0.0, abs_tol=tolerance), (actual, expected)


def retained_arrays(rows, fixed_strata):
    fixed = set(fixed_strata)
    decided = [row for row in rows if row["endpoint_state"] in DECIDED and row["fixed_stratum"] in fixed]
    cells = []
    retained = []
    for stratum in fixed_strata:
        members = [row for row in decided if row["fixed_stratum"] == stratum]
        n1 = sum(row["family_exposure"] == 1 for row in members)
        n0 = sum(row["family_exposure"] == 0 for row in members)
        if n1 and n0:
            weight = n1 * n0 / (n1 + n0)
            cells.append((stratum, n1, n0, weight))
            retained.extend(members)
    assert cells and len(retained) == 1221
    y = np.asarray([float(row["endpoint_state"] == "SUPPORTED") for row in retained], dtype=float)
    e = np.asarray([float(row["family_exposure"]) for row in retained], dtype=float)
    strata = np.asarray([row["fixed_stratum"] for row in retained], dtype=object)
    return y, e, strata, cells


def primary_analysis(rows, fixed_strata):
    y, e, strata, cells = retained_arrays(rows, fixed_strata)
    total_weight = sum(cell[3] for cell in cells)
    rd = sum(
        weight
        * (
            float(y[(strata == stratum) & (e == 1)].mean())
            - float(y[(strata == stratum) & (e == 0)].mean())
        )
        for stratum, _n1, _n0, weight in cells
    ) / total_weight
    estimable = [cell[0] for cell in cells]
    baseline = estimable[0]
    x = np.asarray(
        [
            [1.0]
            + [float(stratum == value) for value in estimable if value != baseline]
            + [exposure]
            for stratum, exposure in zip(strata, e, strict=True)
        ],
        dtype=float,
    )
    assert np.linalg.matrix_rank(x) == x.shape[1]
    inverse = np.linalg.inv(x.T @ x)
    beta = inverse @ x.T @ y
    residual = y - x @ beta
    leverage = np.einsum("ij,jk,ik->i", x, inverse, x)
    adjusted = residual / (1.0 - leverage)
    covariance = inverse @ (x.T @ ((adjusted * adjusted)[:, None] * x)) @ inverse
    se = math.sqrt(float(covariance[-1, -1]))
    close(float(beta[-1]), rd)
    return {
        "estimate": rd,
        "standard_error_hc3": se,
        "one_sided_95_lower": rd - Z95 * se,
        "one_sided_95_upper": rd + Z95 * se,
        "retained_person_count": len(y),
        "estimable_stratum_count": len(cells),
        "harmonic_weight_sum": total_weight,
        "cells": cells,
    }


def permutation_from_frozen_draws(surface, cells, observed):
    assert surface["draw_count"] == len(surface["y1_supported_draws"]) == 9999
    assert surface["seed"] == 20260817
    metadata = surface["fixed_strata"]
    assert [row["fixed_stratum"] for row in metadata] == [cell[0] for cell in cells]
    total_weight = sum(cell[3] for cell in cells)
    statistics = np.empty(9999, dtype="<f8")
    for repetition, draw in enumerate(surface["y1_supported_draws"]):
        assert len(draw) == len(cells)
        statistic = 0.0
        for y1, public_cell, cell in zip(draw, metadata, cells, strict=True):
            _stratum, n1, n0, weight = cell
            assert public_cell["exposed_decided"] == n1
            assert public_cell["unexposed_decided"] == n0
            total_supported = public_cell["total_supported"]
            assert isinstance(y1, int)
            assert max(0, total_supported - n0) <= y1 <= min(n1, total_supported)
            statistic += weight * (y1 / n1 - (total_supported - y1) / n0)
        statistics[repetition] = statistic / total_weight
    digest = hashlib.sha256(statistics.tobytes()).hexdigest()
    assert digest == surface["statistics_float64_le_sha256"]
    exceed = int(np.count_nonzero(statistics >= observed))
    p_value = (1 + exceed) / 10000
    assert exceed == surface["exceed_or_equal_count"]
    close(p_value, surface["one_sided_p"], 0.0)
    return {"statistics_sha256": digest, "exceed_or_equal_count": exceed, "one_sided_p": p_value}


def manski(rows):
    counts = {exposure: Counter(row["endpoint_state"] for row in rows if row["family_exposure"] == exposure) for exposure in (0, 1)}
    n1, n0 = sum(counts[1].values()), sum(counts[0].values())
    s1, s0 = counts[1]["SUPPORTED"], counts[0]["SUPPORTED"]
    u1 = sum(counts[1][state] for state in UNDECIDED)
    u0 = sum(counts[0][state] for state in UNDECIDED)
    return {
        "exposed_denominator": n1,
        "unexposed_denominator": n0,
        "supported_exposed_count": s1,
        "supported_unexposed_count": s0,
        "undecided_person_count": u1 + u0,
        "undecided_exposed_count": u1,
        "undecided_unexposed_count": u0,
        "sharp_lower_risk_difference": s1 / n1 - (s0 + u0) / n0,
        "sharp_upper_risk_difference": (s1 + u1) / n1 - s0 / n0,
        "all_undecided_zero_risk_difference": s1 / n1 - s0 / n0,
        "all_undecided_one_risk_difference": (s1 + u1) / n1 - (s0 + u0) / n0,
    }


def conditional_power(cells, results):
    delta = results["delta_ref"]
    total_weight = sum(cell[3] for cell in cells)
    z_sum = Z95 + Z80
    mdes = []
    powers = []
    for q0 in results["base_rate_grid"]:
        low, high = 0.0, 1.0 - q0
        for _ in range(80):
            candidate = (low + high) / 2.0
            q1 = q0 + candidate
            variance = sum(
                weight * weight * (q1 * (1 - q1) / n1 + q0 * (1 - q0) / n0)
                for _stratum, n1, n0, weight in cells
            ) / (total_weight * total_weight)
            if candidate >= z_sum * math.sqrt(variance):
                high = candidate
            else:
                low = candidate
        mdes.append({"q0": q0, "mde": high})
        q1 = q0 + delta
        variance = sum(
            weight * weight * (q1 * (1 - q1) / n1 + q0 * (1 - q0) / n0)
            for _stratum, n1, n0, weight in cells
        ) / (total_weight * total_weight)
        powers.append({"q0": q0, "q1": q1, "power": NormalDist().cdf(delta / math.sqrt(variance) - Z95)})
    return mdes, powers


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    if args.strict:
        subprocess.run([sys.executable, str(ROOT / "scripts/validate_public_v4_privacy.py")], check=True)

    results = load_json("RESULTS.json")
    ledger = load_json("data/confirmation1457_anonymous_primary_v4.json")
    decoys = load_json("data/decoy_summary_v4.json")
    draws = load_json_gz("data/primary_permutation_draws_v4.json.gz")
    assert results["schema_id"] == "INDEPENDENT_SOCIAL_EXPRESSION_PUBLIC_RESULTS_V4"
    assert ledger["schema_id"] == "INDEPENDENT_SOCIAL_EXPRESSION_PRIMARY_LEDGER_V4"
    assert decoys["schema_id"] == "INDEPENDENT_SOCIAL_EXPRESSION_DECOY_SUMMARY_V4"
    assert draws["schema_id"] == "INDEPENDENT_SOCIAL_EXPRESSION_PERMUTATION_DRAWS_V4"
    rows = ledger["rows"]
    assert len(rows) == 1457
    assert [row["release_id"] for row in rows] == [f"R{index:04d}" for index in range(1, 1458)]
    assert all(set(row) == ROW_KEYS for row in rows)
    assert sum(row["family_exposure"] for row in rows) == 59
    assert sum(1 - row["family_exposure"] for row in rows) == 1398

    state_counts = Counter(row["endpoint_state"] for row in rows)
    assert dict(sorted(state_counts.items())) == results["measurement"]["endpoint_state_counts_primary"]
    denominators = Counter(row["family_exposure"] for row in rows)
    decided = Counter(row["family_exposure"] for row in rows if row["endpoint_state"] in DECIDED)
    coverage = {str(value): decided[value] / denominators[value] for value in (0, 1)}
    difference = abs(coverage["1"] - coverage["0"])
    assert coverage == results["measurement"]["coverage"]
    close(difference, results["measurement"]["absolute_coverage_difference"])
    assert min(coverage.values()) >= 0.85 and difference <= 0.10

    all_strata = sorted({row["fixed_stratum"] for row in rows})
    fixed_strata = [
        stratum
        for stratum in all_strata
        if any(row["fixed_stratum"] == stratum and row["family_exposure"] == 1 for row in rows)
        and any(row["fixed_stratum"] == stratum and row["family_exposure"] == 0 for row in rows)
    ]
    assert len(all_strata) == 36
    assert fixed_strata == results["population"]["fixed_estimable_strata"]
    primary = primary_analysis(rows, fixed_strata)
    expected = results["primary_analysis"]
    for key in (
        "estimate",
        "standard_error_hc3",
        "one_sided_95_lower",
        "one_sided_95_upper",
        "harmonic_weight_sum",
    ):
        close(primary[key], expected[key])
    assert primary["retained_person_count"] == expected["retained_person_count"]
    assert primary["estimable_stratum_count"] == expected["estimable_stratum_count"]
    permutation = permutation_from_frozen_draws(draws, primary["cells"], primary["estimate"])
    assert permutation == {
        "statistics_sha256": expected["permutation"]["statistics_float64_le_sha256"],
        "exceed_or_equal_count": expected["permutation"]["exceed_or_equal_count"],
        "one_sided_p": expected["permutation"]["one_sided_p"],
    }

    observed_manski = manski(rows)
    for key, value in observed_manski.items():
        expected_value = results["manski_missingness_bounds"][key]
        if isinstance(value, float):
            close(value, expected_value)
        else:
            assert value == expected_value

    mdes, powers = conditional_power(primary["cells"], results["conditional_power_and_mde"])
    for observed, expected_row in zip(mdes, results["conditional_power_and_mde"]["mde_by_base_rate"], strict=True):
        assert observed["q0"] == expected_row["q0"]
        close(observed["mde"], expected_row["mde"])
    for observed, expected_row in zip(powers, results["conditional_power_and_mde"]["power_by_base_rate_at_delta_ref"], strict=True):
        assert observed["q0"] == expected_row["q0"]
        close(observed["q1"], expected_row["q1"])
        close(observed["power"], expected_row["power"])
    minimum_power = min(row["power"] for row in powers)
    close(minimum_power, results["conditional_power_and_mde"]["minimum_power_at_delta_ref"])

    decoy_rows = decoys["rows"]
    assert len(decoy_rows) == 98 == len({row["decoy_id"] for row in decoy_rows})
    assert all(row["status"] == "ESTIMABLE" for row in decoy_rows)
    exceed = sum(row["estimate"] >= primary["estimate"] for row in decoy_rows)
    decoy_p = (1 + exceed) / 99
    assert exceed == results["decoy_specificity"]["exceed_or_equal_count"]
    close(decoy_p, results["decoy_specificity"]["empirical_one_sided_p"], 0.0)

    positive = permutation["one_sided_p"] < 0.05 and primary["one_sided_95_lower"] > 0
    if positive:
        terminal = "PASS_ONE_CORRECTED_ROUTE_FAMILY" if decoy_p <= 0.05 else "POSITIVE_ASSOCIATION_NOT_ROUTE_SPECIFIC"
    elif minimum_power >= 0.80 and primary["one_sided_95_upper"] < results["conditional_power_and_mde"]["delta_ref"]:
        terminal = "ADEQUATELY_POWERED_PRIMARY_NULL"
    else:
        terminal = "INSUFFICIENT_POWER_OR_SUPPORT"
    assert terminal == results["terminal_outcome"]
    print(json.dumps({
        "result": "PASS",
        "primary_people": len(rows),
        "estimate": primary["estimate"],
        "permutation_p": permutation["one_sided_p"],
        "decoy_p": decoy_p,
        "minimum_power_at_delta_ref": minimum_power,
        "terminal_outcome": terminal,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
