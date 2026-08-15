#!/usr/bin/env python3
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FUNCTIONS = (
    "ADVOCACY_OR_PUBLIC_CAUSE_ACTION", "AUTHORED_SYMBOLIC_PRODUCTION",
    "ORGANIZED_COLLECTIVE_REALIZATION", "TECHNOLOGY_OR_PRODUCT_IMPLEMENTATION",
    "EMBODIED_COMPETITIVE_PERFORMANCE",
)

def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))

def main():
    summary = load("data/candidate_summary_v2.json")
    matrix = load("data/development420_anonymous_matrix_v2.json")
    registry = load("data/five_candidate_rule_registry_v2.json")
    actor = load("data/measurement_actor_gate_v2.json")
    boundary = load("CLAIM_BOUNDARY.json")
    rules = {row["common_tendency_rule_id"]: row for row in registry["rules"]}
    assert len(matrix["people"]) == 420 == summary["development_person_count"]
    assert len(rules) == 515 == registry["rule_count"]
    expected = {row["function"]: row for row in summary["candidates"]}
    for function in FUNCTIONS:
        row = expected[function]
        totals = Counter()
        by_cohort = {}
        for person in matrix["people"]:
            tiers = {"WESTERN": set(), "JYOTISH": set()}
            for rule_id in person["matched_rule_ids_by_function"][function]:
                rule = rules[rule_id]
                assert rule["social_output_meaning_function"] == function
                system = rule["chart_meaning_core"]["system"]
                tier = "P" if rule["theory_tier"] == "PRIMARY_THEORY_COHERENT_TRAINING_RULE" else "A"
                tiers[system].add(tier)
            predicted = ("P" in tiers["WESTERN"] and "P" in tiers["JYOTISH"]) if row["prediction_surface"] == "PP" else bool(tiers["WESTERN"] and tiers["JYOTISH"])
            observed = function in person["observed_functions"]
            totals.update(person=1, predicted=int(predicted), observed=int(observed), supported=int(predicted and observed))
        assert totals["predicted"] == row["predicted_person_count"]
        assert totals["supported"] == row["supported_person_count"]
        assert totals["observed"] == row["observed_person_count"]
        assert totals["supported"] / totals["predicted"] == row["support_rate"]
        assert totals["observed"] / totals["person"] == row["observed_prevalence"]
        for cohort in row["subcohorts"]:
            people = [p for p in matrix["people"] if p["development_subcohort"] == cohort["development_subcohort"]]
            values = Counter()
            for person in people:
                tiers = {"WESTERN": set(), "JYOTISH": set()}
                for rule_id in person["matched_rule_ids_by_function"][function]:
                    rule = rules[rule_id]
                    system = rule["chart_meaning_core"]["system"]
                    tier = "P" if rule["theory_tier"] == "PRIMARY_THEORY_COHERENT_TRAINING_RULE" else "A"
                    tiers[system].add(tier)
                predicted = ("P" in tiers["WESTERN"] and "P" in tiers["JYOTISH"]) if row["prediction_surface"] == "PP" else bool(tiers["WESTERN"] and tiers["JYOTISH"])
                observed = function in person["observed_functions"]
                values.update(person=1, predicted=int(predicted), observed=int(observed), supported=int(predicted and observed))
            assert values["person"] == cohort["person_count"]
            assert values["predicted"] == cohort["predicted_person_count"]
            assert values["supported"] == cohort["supported_person_count"]
            assert values["observed"] == cohort["observed_person_count"]
    assert actor["correct_self_count"] / actor["known_reference_count"] == actor["actor_known_precision"]
    assert actor["known_reference_count"] / actor["self_action_count"] == actor["actor_reference_coverage"]
    assert actor["selected_linked_count"] / actor["linked_reference_count"] == actor["linked_action_selection_recall"]
    assert actor["failed_frozen_gates"] == ["actor_known_precision", "actor_reference_coverage"]
    assert boundary["terminal_outcome"] == actor["terminal_outcome"] == "MEASUREMENT_CONSTRUCT_LIMITATION"
    assert boundary["external_route_validation_count"] == 0
    print(json.dumps({
        "result": "PASS", "development_people": 420, "candidate_count": 5,
        "rule_count": 515, "actor_known_precision": actor["actor_known_precision"],
        "actor_reference_coverage": actor["actor_reference_coverage"],
        "linked_action_selection_recall": actor["linked_action_selection_recall"],
        "terminal_outcome": actor["terminal_outcome"], "external_route_validation_count": 0,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
