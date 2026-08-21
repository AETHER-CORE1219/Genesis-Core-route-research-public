#!/usr/bin/env python3
"""Fail closed if the public v7 bundle exposes private identity or source data."""
from __future__ import annotations

import gzip
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FORBIDDEN_KEYS = {
    "subject_id", "subject_id_sha256", "qid", "name", "url", "revision_id",
    "source_text", "quote", "birth_date", "birth_time", "chart", "longitude",
    "latitude", "raw_response", "prompt", "private_path",
}
PRIVATE_MARKERS = (
    "/home/", "expression_path_machine_discovery_v2_private_analysis", "wikidata.org/entity/",
    "wikipedia.org/wiki/", "Astro-Databank", "astro.com/astro-databank",
)
RELEASE_ID = re.compile(r"^R\d{4}$")


def load(path: Path):
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def walk(value, path="$"):
    if isinstance(value, dict):
        for key, child in value.items():
            if key.lower() in FORBIDDEN_KEYS:
                raise AssertionError(f"forbidden key {key} at {path}")
            walk(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            walk(child, f"{path}[{index}]")
    elif isinstance(value, str):
        for marker in PRIVATE_MARKERS:
            if marker.lower() in value.lower():
                raise AssertionError(f"private marker at {path}: {marker}")


def main() -> int:
    matrix = load(DATA / "development420_external_factor_matrix_v7.json.gz")
    if matrix["schema_id"] != "INDEPENDENT_SOCIAL_EXPRESSION_EXTERNAL_FACTOR_MATRIX_V7":
        raise AssertionError("matrix schema mismatch")
    rows = matrix["rows"]
    allowed = {
        "release_id", "analysis_order", "birth_decade", "birth_era", "source_evidence_regime",
        "collection_source_group", "development_subcohort", "field_state",
        "field_values_transport_only", "observed_functions", "surfaces",
    }
    if len(rows) != 420 or any(set(row) != allowed for row in rows):
        raise AssertionError("matrix row allowlist mismatch")
    identifiers = [row["release_id"] for row in rows]
    if len(set(identifiers)) != 420 or not all(RELEASE_ID.fullmatch(value) for value in identifiers):
        raise AssertionError("release IDs are not unique opaque IDs")
    if sorted(row["analysis_order"] for row in rows) != list(range(1, 421)):
        raise AssertionError("analysis order mismatch")
    decoys = load(DATA / "development420_adversarial_decoy_memberships_v7.json.gz")
    if decoys["row_count"] != 7634 or decoys["unique_exposure_set_count"] != 708:
        raise AssertionError("decoy counts mismatch")
    opportunity = load(DATA / "development420_observation_opportunity_v7.json.gz")
    if opportunity["person_count"] != 420 or {row["release_id"] for row in opportunity["rows"]} != set(identifiers):
        raise AssertionError("opportunity population mismatch")
    for path in list(ROOT.glob("*.json")) + list(DATA.glob("*.json")) + list(DATA.glob("*.json.gz")):
        walk(load(path))
    print(json.dumps({"result": "PASS", "people": 420, "decoy_rows": 7634, "json_surfaces_checked": len(list(ROOT.glob('*.json'))) + len(list(DATA.glob('*.json'))) + len(list(DATA.glob('*.json.gz')))}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
