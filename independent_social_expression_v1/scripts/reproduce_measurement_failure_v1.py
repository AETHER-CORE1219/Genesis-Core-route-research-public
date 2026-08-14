#!/usr/bin/env python3
"""Reproduce the frozen AKSQ measurement decision from public anonymous data."""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
POSITIVE = {"SUPPORTED", "PARTIAL"}
PROCEDURES = ("PROCEDURE_A", "PROCEDURE_B")
EXPECTED_FILES = {
    "candidate_summary_v1.json",
    "measurement_truth_anonymized_v1.json",
    "measurement_ratings_anonymized_v1.json",
    "target_evidence_reference_v1.json",
    "measurement_expected_result_v1.json",
    "model_proof_v1.json",
    "measurement_raw_responses_v1.jsonl",
    "source_manifest_v1.json",
}


def load_json(name: str) -> dict[str, Any]:
    value = json.loads((DATA / name).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssertionError(f"JSON object required: {name}")
    return value


def close(actual: float, expected: float) -> bool:
    return math.isclose(actual, expected, rel_tol=0.0, abs_tol=1e-12)


def metric(rows: list[dict[str, Any]], truth_by: dict[str, dict[str, str]]) -> dict[str, float | int]:
    tp = fp = fn = 0
    for row in rows:
        actual = truth_by[row["subject_id_sha256"]][row["function"]] in POSITIVE
        predicted = row["state"] in POSITIVE
        tp += int(actual and predicted)
        fp += int(not actual and predicted)
        fn += int(actual and not predicted)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"tp": tp, "fp": fp, "fn": fn, "precision": precision, "recall": recall, "f1": f1}


def assert_metrics(actual: dict[str, Any], expected: dict[str, Any], prefix: str) -> None:
    for key in ("tp", "fp", "fn"):
        if key in expected and actual[key] != expected[key]:
            raise AssertionError(f"{prefix}.{key}: {actual[key]} != {expected[key]}")
    for key in ("precision", "recall", "f1"):
        if not close(float(actual[key]), float(expected[key])):
            raise AssertionError(f"{prefix}.{key}: {actual[key]} != {expected[key]}")


def main() -> int:
    if not EXPECTED_FILES.issubset({path.name for path in DATA.iterdir() if path.is_file()}):
        raise AssertionError("public data bundle is incomplete")

    candidate = load_json("candidate_summary_v1.json")
    truth = load_json("measurement_truth_anonymized_v1.json")
    ledger = load_json("measurement_ratings_anonymized_v1.json")
    reference = load_json("target_evidence_reference_v1.json")
    expected = load_json("measurement_expected_result_v1.json")
    source_manifest = load_json("source_manifest_v1.json")

    functions = tuple(truth["functions"])
    truth_by = {row["subject_id_sha256"]: row["truth_states"] for row in truth["rows"]}
    ratings = ledger["ratings"]
    subjects = tuple(sorted(truth_by))
    rating_keys = {(r["subject_id_sha256"], r["procedure"], r["function"]) for r in ratings}
    expected_rating_keys = {(s, p, f) for s in subjects for p in PROCEDURES for f in functions}
    if len(subjects) != 12 or len(functions) != 5 or len(ratings) != 120 or rating_keys != expected_rating_keys:
        raise AssertionError("12-person x 5-function x 2-procedure rating surface is incomplete")
    if candidate["candidate_count"] != 5 or {row["function"] for row in candidate["candidates"]} != set(functions):
        raise AssertionError("the five frozen candidates do not match the measurement functions")
    if not any(row["function"] == "EMBODIED_COMPETITIVE_PERFORMANCE" for row in candidate["candidates"]):
        raise AssertionError("embodied competitive performance candidate is absent")

    raw = [json.loads(line) for line in (DATA / "measurement_raw_responses_v1.jsonl").read_text(encoding="utf-8").splitlines()]
    if [row["sequence"] for row in raw] != list(range(len(raw))):
        raise AssertionError("raw sequence is not exact and contiguous")
    for row in raw:
        digest = hashlib.sha256(str(row["exact_raw_response"]).encode()).hexdigest()
        if digest != row["exact_raw_sha256"]:
            raise AssertionError(f"raw response hash mismatch at sequence {row['sequence']}")
    state_raw = [row for row in raw if row["response_type"] == "STATE"]
    citation_raw = [row for row in raw if row["response_type"] == "CITATION"]
    state_keys = {(r["subject_id_sha256"], r["procedure"], r["function"]) for r in state_raw}
    citation_keys = {(r["subject_id_sha256"], r["procedure"], r["function"]) for r in citation_raw}
    positive_rows = [row for row in ratings if row["state"] in POSITIVE]
    positive_keys = {(r["subject_id_sha256"], r["procedure"], r["function"]) for r in positive_rows}
    raw_state_exact = len(state_raw) == 120 and state_keys == rating_keys
    raw_citation_exact = len(citation_raw) == len(positive_rows) and citation_keys == positive_keys

    procedure_function: dict[str, dict[str, float | int]] = {}
    for procedure in PROCEDURES:
        for function in functions:
            rows = [r for r in ratings if r["procedure"] == procedure and r["function"] == function]
            procedure_function[f"{procedure}:{function}"] = metric(rows, truth_by)
    overall = metric(ratings, truth_by)
    by_key = {(r["subject_id_sha256"], r["procedure"], r["function"]): r for r in ratings}
    agreement = sum(
        (by_key[(subject, "PROCEDURE_A", function)]["state"] in POSITIVE)
        == (by_key[(subject, "PROCEDURE_B", function)]["state"] in POSITIVE)
        for subject in subjects
        for function in functions
    ) / 60
    target_references = {
        (row["subject_id_sha256"], row["function"], row["evidence_id"])
        for row in reference["rows"]
    }
    grounding = sum(
        (row["subject_id_sha256"], row["function"], row["evidence_id"]) in target_references
        for row in positive_rows
    ) / len(positive_rows)
    abstention = {
        procedure: sum(r["state"] == "UNADJUDICATED" for r in ratings if r["procedure"] == procedure) / 60
        for procedure in PROCEDURES
    }

    computed_metrics = {
        "overall_precision": overall["precision"],
        "overall_recall": overall["recall"],
        "overall_f1": overall["f1"],
        "binary_agreement": agreement,
        "positive_target_citation_grounding": grounding,
        "abstention_by_procedure": abstention,
        "procedure_function_metrics": procedure_function,
        "state_counts": dict(Counter(f"{r['procedure']}:{r['state']}" for r in ratings)),
    }
    for key in ("overall_precision", "overall_recall", "overall_f1", "binary_agreement", "positive_target_citation_grounding"):
        if not close(float(computed_metrics[key]), float(expected["metrics"][key])):
            raise AssertionError(f"metric mismatch: {key}")
    if computed_metrics["abstention_by_procedure"] != expected["metrics"]["abstention_by_procedure"]:
        raise AssertionError("abstention mismatch")
    if computed_metrics["state_counts"] != expected["metrics"]["state_counts"]:
        raise AssertionError("state-count mismatch")
    for key, value in procedure_function.items():
        assert_metrics(value, expected["metrics"]["procedure_function_metrics"][key], key)

    gates = {
        "schema_complete_120": rating_keys == expected_rating_keys,
        "raw_state_count_and_identity_exact_120": raw_state_exact,
        "raw_citation_count_and_identity_exact": raw_citation_exact,
        "raw_sequence_hash_exact": True,
        "overall_precision_min_0_80": overall["precision"] >= 0.80,
        "overall_recall_min_0_80": overall["recall"] >= 0.80,
        "overall_f1_min_0_80": overall["f1"] >= 0.80,
        "each_procedure_function_precision_min_0_75": all(v["precision"] >= 0.75 for v in procedure_function.values()),
        "each_procedure_function_recall_min_0_75": all(v["recall"] >= 0.75 for v in procedure_function.values()),
        "binary_agreement_min_0_90": agreement >= 0.90,
        "positive_target_citation_subject_marker_grounding_1": grounding == 1.0,
        "abstention_each_procedure_max_0_10": all(value <= 0.10 for value in abstention.values()),
        "truth_access_after_all_model_responses": True,
        "protected_access_zero": source_manifest["protected_access_counts"] == {
            "akq72": 0,
            "aks575": 0,
            "charts_routes_akd_confirmation": 0,
        },
    }
    if gates != expected["gates"]:
        raise AssertionError("recomputed gates differ from the frozen decision")
    terminal = "PASS_FREEZE_INSTRUMENT_FOR_ONE_AKQ72_APPLICATION" if all(gates.values()) else "MEASUREMENT_FAILURE"
    boundary = expected["publication_claim_boundary"]
    if terminal != "MEASUREMENT_FAILURE" or expected["status"] != terminal:
        raise AssertionError("terminal outcome is not the frozen measurement failure")
    if boundary != {
        "candidate_rejection_count": 0,
        "external_route_validation_count": 0,
        "route_null_claim": False,
        "route_test_performed": False,
        "terminal_outcome": "MEASUREMENT_FAILURE",
    }:
        raise AssertionError("publication claim boundary changed")

    print(json.dumps({
        "result": "PASS",
        "terminal_outcome": terminal,
        "candidate_count": 5,
        "external_route_validation_count": 0,
        "route_test_performed": False,
        "overall_precision": overall["precision"],
        "overall_recall": overall["recall"],
        "overall_f1": overall["f1"],
        "binary_agreement": agreement,
        "positive_target_citation_grounding": grounding,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
