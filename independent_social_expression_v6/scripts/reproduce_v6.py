#!/usr/bin/env python3
"""Reproduce the v6 synthesis from public, frozen v2-v5 surfaces."""

from __future__ import annotations

import json
import hashlib
import math
from collections import Counter
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
V6 = REPO / "independent_social_expression_v6"


def load(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def close(actual: float, expected: float, tolerance: float = 1e-12) -> None:
    if not math.isclose(actual, expected, rel_tol=0.0, abs_tol=tolerance):
        raise AssertionError(f"numeric mismatch: {actual} != {expected}")


def main() -> None:
    manifest = load(V6 / "BUNDLE_MANIFEST.json")
    for relative, expected_sha in manifest["frozen_public_dependencies"].items():
        dependency = V6 / relative
        actual_sha = sha256_file(dependency)
        if actual_sha != expected_sha:
            raise AssertionError(f"frozen dependency hash mismatch: {relative}")

    v2_results = load(REPO / "independent_social_expression_v2" / "RESULTS.json")
    v2_registry = load(REPO / "independent_social_expression_v2" / "data" / "five_candidate_rule_registry_v2.json")
    v3 = load(REPO / "independent_social_expression_v3" / "RESULTS.json")
    v4 = load(REPO / "independent_social_expression_v4" / "RESULTS.json")
    v5 = load(REPO / "independent_social_expression_v5" / "RESULTS.json")
    atlas = load(V6 / "data" / "corrected_meaning_family_atlas_v6.json")
    people = load(V6 / "data" / "person_trace_summary_v6.json")
    result = load(V6 / "RESULTS.json")

    if v2_registry["rule_count"] != 515 or len(v2_registry["rules"]) != 515:
        raise AssertionError("v2 registry is not the fixed 515-rule development surface")
    mechanism_count = len({row["mechanism_family_id"] for row in v2_registry["rules"]})
    if mechanism_count != 120:
        raise AssertionError(f"v2 public mechanism ID count mismatch: {mechanism_count}")

    expected_rule_counts = {
        "ADVOCACY_OR_PUBLIC_CAUSE_ACTION": 97,
        "AUTHORED_SYMBOLIC_PRODUCTION": 147,
        "ORGANIZED_COLLECTIVE_REALIZATION": 129,
        "TECHNOLOGY_OR_PRODUCT_IMPLEMENTATION": 88,
        "EMBODIED_COMPETITIVE_PERFORMANCE": 54,
    }
    actual_rule_counts = Counter(row["social_output_meaning_function"] for row in v2_registry["rules"])
    if dict(actual_rule_counts) != expected_rule_counts:
        raise AssertionError(f"v2 function rule counts mismatch: {actual_rule_counts}")

    candidates = v2_results["candidate_summary"]["candidates"]
    by_function = {row["function"]: row for row in candidates}
    for expected in result["development420"]["five_functions"]:
        observed = by_function[expected["function"]]
        if observed["predicted_person_count"] != expected["predicted"]:
            raise AssertionError("development predicted count mismatch")
        if observed["supported_person_count"] != expected["supported"]:
            raise AssertionError("development supported count mismatch")
        close(observed["support_rate"], expected["support_rate"])
        close(observed["observed_prevalence"], expected["base_rate"])
        close(observed["descriptive_enrichment_ratio"], expected["enrichment_ratio"])
        if not all(x["direction_above_prevalence"] for x in observed["subcohorts"]):
            raise AssertionError("a development subcohort does not have the frozen positive direction")

    if atlas["family_count"] != 136 or len(atlas["rows"]) != 136:
        raise AssertionError("corrected five-function family count mismatch")
    cross_count = sum(bool(row["cross_subcohort_support"]) for row in atlas["rows"])
    if cross_count != 134 or atlas["cross_subcohort_supported_family_count"] != 134:
        raise AssertionError("cross-subcohort family count mismatch")
    expected_family_counts = {
        ("ADVOCACY_OR_PUBLIC_CAUSE_ACTION", "JYOTISH"): 22,
        ("ADVOCACY_OR_PUBLIC_CAUSE_ACTION", "WESTERN"): 6,
        ("AUTHORED_SYMBOLIC_PRODUCTION", "JYOTISH"): 22,
        ("AUTHORED_SYMBOLIC_PRODUCTION", "WESTERN"): 7,
        ("ORGANIZED_COLLECTIVE_REALIZATION", "JYOTISH"): 22,
        ("ORGANIZED_COLLECTIVE_REALIZATION", "WESTERN"): 7,
        ("TECHNOLOGY_OR_PRODUCT_IMPLEMENTATION", "JYOTISH"): 22,
        ("TECHNOLOGY_OR_PRODUCT_IMPLEMENTATION", "WESTERN"): 6,
        ("EMBODIED_COMPETITIVE_PERFORMANCE", "JYOTISH"): 20,
        ("EMBODIED_COMPETITIVE_PERFORMANCE", "WESTERN"): 2,
    }
    actual_family_counts = Counter((row["function"], row["system"]) for row in atlas["rows"])
    if dict(actual_family_counts) != expected_family_counts:
        raise AssertionError(f"meaning family counts mismatch: {actual_family_counts}")

    if people["person_count"] != 6 or len(people["people"]) != 6:
        raise AssertionError("person trace count mismatch")
    if len({row["name"] for row in people["people"]}) != 6:
        raise AssertionError("person traces are not unique")

    held_v3 = v3["heldout"]
    close(held_v3["era_standardized_risk_difference"], -0.025621558392630476)
    close(held_v3["conservative_raw_p"], 0.6923015384923076)
    if held_v3["claim_unit"] != "FIXED_25_PRIMARY_CORRECTED_MECHANISM_UNITS_AGGREGATED_BY_ANY_MATCH":
        raise AssertionError("v3 tested-unit boundary changed")

    close(v4["primary_analysis"]["estimate"], 0.0710069495149408)
    close(v4["primary_analysis"]["permutation"]["one_sided_p"], 0.1357)
    close(v4["decoy_specificity"]["empirical_one_sided_p"], 0.13131313131313133)
    close(v4["conditional_power_and_mde"]["delta_ref"], 0.1993299573270514)
    if v4["terminal_outcome"] != "ADEQUATELY_POWERED_PRIMARY_NULL":
        raise AssertionError("v4 terminal outcome changed")

    close(v5["primary_full_chain"]["estimate"], -0.052742635139418625)
    if (v5["primary_full_chain"]["supported_exposed"], v5["primary_full_chain"]["decided_exposed"]) != (0, 7):
        raise AssertionError("v5 strict branch counts changed")
    close(v5["secondary_same_meaning_core_without_carrier"]["estimate"], 0.03379125878935242)
    close(v5["secondary_same_meaning_core_without_carrier"]["stratified_permutation_p_one_sided"], 0.5276)

    if result["external_positive_route_count"] != 0:
        raise AssertionError("v6 may not promote an external positive route")
    if result["individual_515_rule_validation_count"] != 0:
        raise AssertionError("v6 may not promote an individual rule")
    if result["post_result_rescue_count"] != 0:
        raise AssertionError("v6 records no post-result rescue")

    print("PASS: independent social expression v6 synthesis reproduced")
    print("development people: 420")
    print("public development rules / mechanism IDs: 515 / 120")
    print("corrected meaning families / cross-subcohort supported: 136 / 134")
    print("person traces: 6")
    print("external stress units: v3 ANY25, v4 one two-branch family, v5 one strict branch")
    print(f"terminal outcome: {result['terminal_outcome']}")


if __name__ == "__main__":
    main()
