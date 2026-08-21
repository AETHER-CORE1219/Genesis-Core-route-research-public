#!/usr/bin/env python3
"""Reproduce the v7 development420 external-factor robustness results."""
from __future__ import annotations

import gzip
import json
import math
from collections import defaultdict
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "data/development420_external_factor_matrix_v7.json.gz"
OPPORTUNITY = ROOT / "data/development420_observation_opportunity_v7.json.gz"
DECOYS = ROOT / "data/development420_adversarial_decoy_memberships_v7.json.gz"
EXPECTED = ROOT / "RESULTS.json"

FUNCTIONS = (
    "ADVERSARIAL_OR_DESTRUCTIVE_REALIZATION",
    "ADVOCACY_OR_PUBLIC_CAUSE_ACTION",
    "AUTHORED_SYMBOLIC_PRODUCTION",
    "BELIEF_OR_SPIRITUAL_SYSTEM_MEDIATION",
    "EMBODIED_COMPETITIVE_PERFORMANCE",
    "KNOWLEDGE_OR_DISCOVERY_PRODUCTION",
    "ORGANIZED_COLLECTIVE_REALIZATION",
    "PERFORMED_SYMBOLIC_PRODUCTION",
    "RULE_OR_INSTITUTION_OPERATION",
    "TECHNOLOGY_OR_PRODUCT_IMPLEMENTATION",
    "VISUAL_OR_DIRECTORIAL_PRODUCTION",
)
PRIMARY = {
    "ADVOCACY_OR_PUBLIC_CAUSE_ACTION": "pp_both_system",
    "AUTHORED_SYMBOLIC_PRODUCTION": "pp_both_system",
    "ORGANIZED_COLLECTIVE_REALIZATION": "pp_both_system",
    "TECHNOLOGY_OR_PRODUCT_IMPLEMENTATION": "pp_both_system",
    "EMBODIED_COMPETITIVE_PERFORMANCE": "any_tier_both_system",
}
ERA = ("BEFORE_1900", "1900_1924", "1925_1949", "1950_1974", "1975_AND_LATER")
REGIME = (
    "SENTENCE_HASH_LINKED_PRIMARY_EVIDENCE",
    "REVISION_PINNED_PERSON_LEVEL_EVIDENCE",
    "ALTERNATE_SOURCE_REPAIR17_FIXED_EVIDENCE",
)
SOURCE = (
    "837fffa4f833059533faee19eca40e9574393d6d0ad0804ba98d0400de4b060b",
    "508b6ad9475247a5444073c88b8e012421f75a181fbd48c1ad36c49d0901bcf4",
    "38df601ee834acd54ebdda5d774a8c56f1bdf924eedf7bc163372bcd860c103e",
    "618aa3c10e4953fdd9d9bd1a09b029167dd5a33e1c8bc5aaf2ac9a1fe043baa3",
    "d93b462a4340999bd21db83a5a9ec0d3801d81c10c4a22c940c847c1fe801e9e",
    "OTHER",
)
DEPTH_SCORE = {"EMPTY": 0.0, "THIN_LT500": 1.0, "SHORT_500_1999": 2.0, "MEDIUM_2000_5999": 3.0, "RICH_GE6000": 4.0}
MAXT_DRAWS = 9999
SEED = 20260821
Z1 = 1.6448536269514722
TOL = 1e-9


def load(path: Path):
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def categorical(rows, key, levels, reference):
    present = {row[key] for row in rows}
    ref = reference if reference in present else next(level for level in levels if level in present)
    return [np.asarray([row[key] == level for row in rows], float) for level in levels if level in present and level != ref]


def design(rows, exposure, blocks):
    columns = [np.ones(len(rows)), exposure]
    if "era" in blocks:
        columns += categorical(rows, "birth_era", ERA, "1950_1974")
    if "regime" in blocks:
        columns += categorical(rows, "source_evidence_regime", REGIME, REGIME[0])
    if "source" in blocks:
        columns += categorical(rows, "collection_source_group", SOURCE, SOURCE[0])
    return np.column_stack(columns)


def fit_x(x, outcome):
    rank = int(np.linalg.matrix_rank(x))
    if rank != x.shape[1]:
        return {"estimable": False, "rank": rank, "column_count": int(x.shape[1])}
    inverse = np.linalg.pinv(x.T @ x)
    beta = inverse @ x.T @ outcome
    residual = outcome - x @ beta
    hat = np.sum((x @ inverse) * x, axis=1)
    adjusted = residual / np.maximum(1.0 - hat, 1e-12)
    covariance = inverse @ ((x * (adjusted * adjusted)[:, None]).T @ x) @ inverse
    standard_error = float(np.sqrt(max(covariance[1, 1], 0.0)))
    effect = float(beta[1])
    return {
        "estimable": True,
        "risk_difference": effect,
        "hc3_standard_error": standard_error,
        "one_sided_95_lower": effect - Z1 * standard_error,
        "t_statistic": effect / standard_error if standard_error else float("inf"),
    }


def fit(rows, exposure, outcome, blocks=("era", "regime", "source")):
    return fit_x(design(rows, exposure, blocks), outcome)


def null_score_influence(z, exposure, outcome):
    inverse = np.linalg.pinv(z.T @ z)
    residual_exposure = exposure - z @ (inverse @ z.T @ exposure)
    residual_outcome = outcome - z @ (inverse @ z.T @ outcome)
    hat = np.sum((z @ inverse) * z, axis=1)
    denominator = float(residual_exposure @ residual_exposure)
    contribution = (residual_exposure / denominator) * (residual_outcome / np.maximum(1.0 - hat, 1e-12))
    return contribution / np.sqrt(np.sum(contribution * contribution))


def stratified_permutation(rows, exposure, outcome, key, blocks, seed):
    observed = fit(rows, exposure, outcome, blocks)
    groups = {
        level: np.asarray([i for i, row in enumerate(rows) if row[key] == level], int)
        for level in sorted({row[key] for row in rows})
    }
    rng = np.random.default_rng(seed)
    greater_or_equal = 0
    valid = 0
    for _ in range(MAXT_DRAWS):
        permuted = exposure.copy()
        for indices in groups.values():
            permuted[indices] = rng.permutation(permuted[indices])
        current = fit(rows, permuted, outcome, blocks)
        if not current["estimable"]:
            continue
        valid += 1
        greater_or_equal += int(current["t_statistic"] >= observed["t_statistic"])
    return {"valid": valid, "one_sided_p": (greater_or_equal + 1) / (valid + 1)}


def raw_strata(rows, exposure, outcome, key, levels):
    result = []
    for level in levels:
        mask = np.asarray([row[key] == level for row in rows])
        exposed = mask & (exposure == 1)
        unexposed = mask & (exposure == 0)
        result.append(None if not (exposed.any() and unexposed.any()) else float(outcome[exposed].mean() - outcome[unexposed].mean()))
    return result


def leave_one_source_out(rows, exposure, outcome):
    result = []
    for level in SOURCE:
        keep = np.asarray([row["collection_source_group"] != level for row in rows])
        subset = [row for i, row in enumerate(rows) if keep[i]]
        result.append(fit(subset, exposure[keep], outcome[keep])["risk_difference"])
    return result


def opportunity_effect(rows, exposure, outcome, opportunity, cohort):
    indices = [i for i, row in enumerate(rows) if row["development_subcohort"] == cohort]
    e = exposure[indices]
    y = outcome[indices]
    if cohort == "SOURCE_REVIEWED311":
        values = np.asarray([DEPTH_SCORE[opportunity[rows[i]["release_id"]]["source_depth_band"]] for i in indices], float)
    else:
        values = np.asarray([math.log1p(opportunity[rows[i]["release_id"]]["candidate_evidence_sentence_count"]) for i in indices], float)
    return fit_x(np.column_stack((np.ones(len(indices)), e, values)), y)["risk_difference"]


def assert_close(actual, expected, label, tolerance=TOL):
    if not math.isclose(float(actual), float(expected), rel_tol=tolerance, abs_tol=tolerance):
        raise AssertionError(f"{label}: {actual} != {expected}")


def main() -> int:
    matrix = load(MATRIX)
    rows = sorted(matrix["rows"], key=lambda row: row["analysis_order"])
    if len(rows) != 420 or [row["analysis_order"] for row in rows] != list(range(1, 421)):
        raise AssertionError("public matrix does not contain the exact opaque analysis order")
    expected = load(EXPECTED)
    opportunity = {row["release_id"]: row for row in load(OPPORTUNITY)["rows"]}
    if set(opportunity) != {row["release_id"] for row in rows}:
        raise AssertionError("opportunity join is not exact420")

    outcomes = {function: np.asarray([function in row["observed_functions"] for row in rows], float) for function in FUNCTIONS}
    primary_exposure = {
        function: np.asarray([row["surfaces"][function][surface] for row in rows], float)
        for function, surface in PRIMARY.items()
    }

    factor_results = {}
    model_blocks = {"M0": (), "M1": ("era",), "M2": ("era", "regime"), "M3": ("era", "regime", "source")}
    for function_index, function in enumerate(PRIMARY):
        exposure = primary_exposure[function]
        outcome = outcomes[function]
        expected_function = expected["functions"][function]
        for model, blocks in model_blocks.items():
            current = fit(rows, exposure, outcome, blocks)
            target = expected_function["sequential_models"][model]
            assert_close(current["risk_difference"], target["risk_difference"], f"{function} {model} RD")
            assert_close(current["hc3_standard_error"], target["hc3_standard_error"], f"{function} {model} HC3")

        era_rd = raw_strata(rows, exposure, outcome, "birth_era", ERA)
        regime_rd = raw_strata(rows, exposure, outcome, "source_evidence_regime", REGIME)
        loo = leave_one_source_out(rows, exposure, outcome)
        opportunity_311 = opportunity_effect(rows, exposure, outcome, opportunity, "SOURCE_REVIEWED311")
        opportunity_109 = opportunity_effect(rows, exposure, outcome, opportunity, "RECOVERED109")
        classification = {
            "era": "ALL_ESTIMABLE_ERA_STRATA_POSITIVE" if all(value > 0 for value in era_rd if value is not None) else "ERA_LIMITED_OR_MODERATED",
            "measurement_regime": "BOTH_MAIN_REGIMES_POSITIVE" if all(value is not None and value > 0 for value in regime_rd[:2]) else "MEASUREMENT_REGIME_LIMITED",
            "collection_source": "ALL_LEAVE_ONE_SOURCE_OUT_POSITIVE" if all(value > 0 for value in loo) else "SOURCE_DEPENDENT",
            "partial_observation_opportunity": "BOTH_SUBCOHORT_ADJUSTED_EFFECTS_POSITIVE" if opportunity_311 > 0 and opportunity_109 > 0 else "OBSERVATION_OPPORTUNITY_LIMITED",
        }
        if classification != expected_function["factor_classification"]:
            raise AssertionError(f"{function} factor classification mismatch")
        era_permutation = stratified_permutation(rows, exposure, outcome, "birth_era", ("era",), SEED + 1000 + function_index)
        source_permutation = stratified_permutation(rows, exposure, outcome, "collection_source_group", ("era", "regime", "source"), SEED + 2000 + function_index)
        assert_close(era_permutation["one_sided_p"], expected_function["factor_second_tests"]["within_era_permutation"]["one_sided_p"], f"{function} era permutation", 1e-12)
        assert_close(source_permutation["one_sided_p"], expected_function["factor_second_tests"]["within_source_permutation"]["one_sided_p"], f"{function} source permutation", 1e-12)
        factor_results[function] = classification

    z = design(rows, np.zeros(len(rows)), ("era", "regime", "source"))[:, [0] + list(range(2, 13))]
    influences = []
    surface_fits = {}
    for function in FUNCTIONS:
        for surface in ("pp_both_system", "any_tier_both_system"):
            exposure = np.asarray([row["surfaces"][function][surface] for row in rows], float)
            key = (function, surface)
            if np.all(exposure == exposure[0]):
                surface_fits[key] = None
                continue
            fitted = fit(rows, exposure, outcomes[function])
            surface_fits[key] = fitted
            influences.append(null_score_influence(z, exposure, outcomes[function]))
    if len(influences) != 18:
        raise AssertionError("fixed 22-surface universe is not 18 estimable plus 4 structural zero")
    rng = np.random.default_rng(SEED)
    signs = rng.integers(0, 2, size=(MAXT_DRAWS, 420), dtype=np.int8).astype(float) * 2.0 - 1.0
    max_t = np.max(signs @ np.column_stack(influences), axis=1)
    critical = float(np.quantile(max_t, 0.95))
    assert_close(critical, expected["max_t"]["critical_95"], "maxT critical", 1e-12)

    decoys = load(DECOYS)
    release_index = {row["release_id"]: i for i, row in enumerate(rows)}
    exposure_sets = {row["exposure_set_id"]: row["release_ids"] for row in decoys["exposure_sets"]}
    decoy_t = defaultdict(list)
    decoy_unique = defaultdict(dict)
    for decoy in decoys["rows"]:
        exposure = np.zeros(420, float)
        for release_id in exposure_sets[decoy["exposure_set_id"]]:
            exposure[release_index[release_id]] = 1.0
        fitted = fit(rows, exposure, outcomes[decoy["function"]])
        if not fitted["estimable"]:
            continue
        value = fitted["t_statistic"]
        decoy_t[decoy["function"]].append(value)
        decoy_unique[decoy["function"]].setdefault(decoy["exposure_set_id"], value)

    selection_results = {}
    for function, surface in PRIMARY.items():
        fitted = surface_fits[(function, surface)]
        observed_t = fitted["t_statistic"]
        adjusted_p = float((1 + np.sum(max_t >= observed_t)) / (MAXT_DRAWS + 1))
        lower = fitted["risk_difference"] - critical * fitted["hc3_standard_error"]
        target = expected["functions"][function]["selection_aware"]
        assert_close(adjusted_p, target["max_t_adjusted_p"], f"{function} maxT p", 1e-12)
        assert_close(lower, target["max_t_simultaneous_one_sided_95_lower"], f"{function} simultaneous lower", 1e-12)
        q95_all = float(np.quantile(np.asarray(decoy_t[function]), 0.95))
        q95_unique = float(np.quantile(np.asarray(list(decoy_unique[function].values())), 0.95))
        decoy_pass = observed_t > q95_all and observed_t > q95_unique
        if decoy_pass != target["adversarial_decoy"]["candidate_exceeds_both_q95"]:
            raise AssertionError(f"{function} adversarial decoy decision mismatch")

        prefix = "primary" if surface == "pp_both_system" else "any_tier"
        ablation = {}
        for label, ablation_surface in {
            "full_both_system": surface,
            "western_only": f"{prefix}_western",
            "jyotish_only": f"{prefix}_jyotish",
        }.items():
            exposure = np.asarray([row["surfaces"][function][ablation_surface] for row in rows], float)
            ablation[label] = fit(rows, exposure, outcomes[function])["risk_difference"]
            assert_close(ablation[label], expected["functions"][function]["system_ablation"]["models"][label]["risk_difference"], f"{function} {label} ablation")
        selection_results[function] = {"adjusted_p": adjusted_p, "simultaneous_lower": lower, "decoy_pass": decoy_pass, "ablation_rd": ablation}

    print(json.dumps({
        "result": "PASS",
        "people": 420,
        "fixed_surfaces": 22,
        "estimable_surfaces": 18,
        "max_t_draws": 9999,
        "max_t_critical_95": critical,
        "factor_classifications": factor_results,
        "selection_aware_results": selection_results,
    }, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
