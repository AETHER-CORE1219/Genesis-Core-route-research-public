#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DECIDED = {"SUPPORTED", "NO_DIRECT_ANCHOR_OBSERVED_IN_ADEQUATE_FIXED_SOURCE"}
Z_ONE_SIDED_95 = 1.6448536269514722
SEED = 20260821
PERMUTATIONS = 9999
ROW_KEYS = {"release_id", "fixed_stratum", "primary_full_chain_exposure", "secondary_meaning_core_exposure", "endpoint_state"}


def load(relative: str):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def close(actual: float, expected: float, tolerance: float = 1e-12) -> None:
    assert math.isclose(actual, expected, rel_tol=0.0, abs_tol=tolerance), (actual, expected)


def design_matrix(exposure: np.ndarray, strata: list[str]) -> np.ndarray:
    levels = sorted(set(strata))
    columns = [np.ones(len(exposure)), exposure.astype(float)]
    for level in levels[1:]:
        columns.append(np.asarray([float(value == level) for value in strata]))
    return np.column_stack(columns)


def adjusted_rd(y: np.ndarray, exposure: np.ndarray, strata: list[str]):
    x = design_matrix(exposure, strata)
    inverse = np.linalg.pinv(x.T @ x)
    coefficients = inverse @ x.T @ y
    residual = y - x @ coefficients
    leverage = np.clip(np.diag(x @ inverse @ x.T), 0.0, 0.999999)
    scaled = residual / (1.0 - leverage)
    covariance = inverse @ (x.T @ ((scaled * scaled)[:, None] * x)) @ inverse
    se = math.sqrt(max(0.0, float(covariance[1, 1])))
    estimate = float(coefficients[1])
    return {
        "estimate": estimate,
        "hc3_se": se,
        "one_sided_95_lower": estimate - Z_ONE_SIDED_95 * se,
        "one_sided_95_upper": estimate + Z_ONE_SIDED_95 * se,
        "rank": int(np.linalg.matrix_rank(x)),
        "n": len(y),
    }


def adjusted_estimate(y: np.ndarray, exposure: np.ndarray, strata: list[str]) -> float:
    centered_y = np.empty(len(y), dtype=float)
    centered_exposure = np.empty(len(exposure), dtype=float)
    groups = defaultdict(list)
    for index, value in enumerate(strata):
        groups[value].append(index)
    for group in groups.values():
        positions = np.asarray(group, dtype=int)
        centered_y[positions] = y[positions] - float(np.mean(y[positions]))
        centered_exposure[positions] = exposure[positions] - float(np.mean(exposure[positions]))
    return float(centered_exposure @ centered_y / (centered_exposure @ centered_exposure))


def analyze(rows, field: str, permutation: bool):
    decided = [row for row in rows if row["endpoint_state"] in DECIDED]
    y = np.asarray([float(row["endpoint_state"] == "SUPPORTED") for row in decided])
    exposure = np.asarray([int(row[field]) for row in decided], dtype=int)
    strata = [row["fixed_stratum"] for row in decided]
    result = adjusted_rd(y, exposure, strata)
    n1 = sum(int(row[field]) for row in rows)
    n0 = len(rows) - n1
    d1 = int(exposure.sum())
    d0 = len(exposure) - d1
    s1 = int(((exposure == 1) & (y == 1)).sum())
    s0 = int(((exposure == 0) & (y == 1)).sum())
    u1, u0 = n1 - d1, n0 - d0
    result.update({
        "population_exposed": n1,
        "population_unexposed": n0,
        "decided_exposed": d1,
        "decided_unexposed": d0,
        "supported_exposed": s1,
        "supported_unexposed": s0,
        "supported_rate_exposed_decided": s1 / d1,
        "supported_rate_unexposed_decided": s0 / d0,
        "raw_decided_risk_difference": s1 / d1 - s0 / d0,
        "coverage_exposed": d1 / n1,
        "coverage_unexposed": d0 / n0,
        "absolute_coverage_difference": abs(d1 / n1 - d0 / n0),
        "unknown_exposed": u1,
        "unknown_unexposed": u0,
        "manski_lower": s1 / n1 - (s0 + u0) / n0,
        "manski_upper": (s1 + u1) / n1 - s0 / n0,
    })
    if permutation:
        rng = np.random.default_rng(SEED)
        groups = defaultdict(list)
        for index, value in enumerate(strata):
            groups[value].append(index)
        values = []
        for _ in range(PERMUTATIONS):
            shuffled = exposure.copy()
            for group in groups.values():
                positions = np.asarray(group)
                shuffled[positions] = rng.permutation(shuffled[positions])
            values.append(adjusted_estimate(y, shuffled, strata))
        statistics = np.asarray(values, dtype="<f8")
        result.update({
            "stratified_permutation_p_one_sided": (1 + int(np.count_nonzero(statistics >= result["estimate"] - 1e-15))) / 10000,
            "permutation_statistic_sha256": hashlib.sha256(statistics.tobytes()).hexdigest(),
            "permutation_count": PERMUTATIONS,
            "seed": SEED,
        })
    return result


def compare(actual, expected, keys):
    for key in keys:
        if isinstance(expected[key], float):
            close(actual[key], expected[key])
        else:
            assert actual[key] == expected[key], (key, actual[key], expected[key])


def main() -> int:
    results = load("RESULTS.json")
    ledger = load("data/legacy313_anonymous_primary_v5.json")
    decoys = load("data/decoy_summary_v5.json")
    assert results["schema_id"] == "INDEPENDENT_SOCIAL_EXPRESSION_PUBLIC_RESULTS_V5"
    assert ledger["schema_id"] == "INDEPENDENT_SOCIAL_EXPRESSION_LEGACY1030_PRIMARY_LEDGER_V5"
    assert decoys["schema_id"] == "INDEPENDENT_SOCIAL_EXPRESSION_LEGACY1030_DECOY_SUMMARY_V5"
    rows = ledger["rows"]
    assert len(rows) == 313
    assert [row["release_id"] for row in rows] == [f"R{index:04d}" for index in range(1, 314)]
    assert all(set(row) == ROW_KEYS for row in rows)
    assert Counter(row["endpoint_state"] for row in rows) == Counter(results["population"]["primary_endpoint_state_counts"])

    primary = analyze(rows, "primary_full_chain_exposure", True)
    secondary = analyze(rows, "secondary_meaning_core_exposure", True)
    keys = [
        "population_exposed", "population_unexposed", "decided_exposed", "decided_unexposed",
        "supported_exposed", "supported_unexposed", "supported_rate_exposed_decided",
        "supported_rate_unexposed_decided", "raw_decided_risk_difference", "coverage_exposed",
        "coverage_unexposed", "absolute_coverage_difference", "unknown_exposed", "unknown_unexposed",
        "manski_lower", "manski_upper", "estimate", "hc3_se", "one_sided_95_lower",
        "one_sided_95_upper", "rank", "n", "stratified_permutation_p_one_sided",
        "permutation_statistic_sha256", "permutation_count", "seed",
    ]
    compare(primary, results["primary_full_chain"], keys)
    compare(secondary, results["secondary_same_meaning_core_without_carrier"], keys)

    assert decoys["decoy_count"] == len(decoys["rows"]) == 99
    assert [row["decoy_rank"] for row in decoys["rows"]] == list(range(1, 100))
    count = sum(row["adjusted_rd"] >= primary["estimate"] - 1e-15 for row in decoys["rows"])
    assert count == decoys["equal_or_greater_count"] == results["primary_full_chain"]["decoy_equal_or_greater_count"]
    close((1 + count) / 100, decoys["empirical_p"])
    close(decoys["empirical_p"], results["primary_full_chain"]["decoy_empirical_p"])

    positive = (
        primary["estimate"] > 0
        and primary["one_sided_95_lower"] > 0
        and primary["stratified_permutation_p_one_sided"] <= 0.05
        and decoys["empirical_p"] <= 0.05
    )
    secondary_positive = secondary["estimate"] > 0 and secondary["one_sided_95_lower"] > 0 and secondary["stratified_permutation_p_one_sided"] <= 0.05
    screen = results["outcome_blind_power_screen"]
    adequate_null = (
        not positive
        and primary["one_sided_95_upper"] < results["development_reference"]["fifty_percent_shrunk_risk_difference_for_null_power_reference"]
        and screen["power_at_fifty_percent_shrunk_development_effect"] >= 0.80
    )
    if positive:
        terminal = "PERSON_OUT_POSITIVE_ROUTE_ASSOCIATION" if primary["manski_lower"] > 0 else "POSITIVE_OBSERVED_ENDPOINT_BUT_MISSINGNESS_SENSITIVE"
    elif secondary_positive:
        terminal = "FUNCTION_LEVEL_ASSOCIATION_ROUTE_SPECIFICITY_NOT_ESTABLISHED"
    elif adequate_null:
        terminal = "ADEQUATELY_POWERED_CANDIDATE_NULL_AT_OR_ABOVE_MDE"
    else:
        terminal = "INCONCLUSIVE_STRICT_ROUTE_WITH_DIRECTION_AND_LIMITS_REPORTED"
    assert terminal == results["terminal_state"]
    print(json.dumps({
        "result": "PASS",
        "terminal_state": terminal,
        "primary_adjusted_rd": primary["estimate"],
        "primary_permutation_p": primary["stratified_permutation_p_one_sided"],
        "primary_decoy_p": decoys["empirical_p"],
        "secondary_adjusted_rd": secondary["estimate"],
        "secondary_permutation_p": secondary["stratified_permutation_p_one_sided"],
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
