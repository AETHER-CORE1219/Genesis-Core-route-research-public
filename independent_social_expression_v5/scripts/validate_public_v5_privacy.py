#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROW_KEYS = {"release_id", "fixed_stratum", "primary_full_chain_exposure", "secondary_meaning_core_exposure", "endpoint_state"}
FORBIDDEN_KEYS = {
    "person_id", "subject_id", "qid", "name", "display_name", "source_url", "source_text",
    "quote", "birth_date", "birth_time", "latitude", "longitude", "chart", "raw_response",
}
FORBIDDEN_TEXT = [
    re.compile(re.escape("/" + "home/"), re.I),
    re.compile(re.escape("wikipedia" + ".org/wiki/"), re.I),
    re.compile(r"\bQ[1-9][0-9]{1,}\b"),
    re.compile(re.escape("." + "research_worktrees") + "|" + re.escape("private" + "_analysis"), re.I),
]


def walk(value):
    if isinstance(value, dict):
        for key, child in value.items():
            assert key not in FORBIDDEN_KEYS, key
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)
    elif isinstance(value, str):
        for pattern in FORBIDDEN_TEXT:
            assert pattern.search(value) is None, (pattern.pattern, value[:160])


def main() -> int:
    files = sorted(path for path in ROOT.rglob("*") if path.is_file() and "__pycache__" not in path.parts)
    assert files
    json_files = [path for path in files if path.suffix == ".json"]
    for path in files:
        raw = path.read_bytes()
        if path.suffix in {".md", ".json", ".py", ".txt", ".sha256"}:
            text = raw.decode("utf-8")
            for pattern in FORBIDDEN_TEXT:
                assert pattern.search(text) is None, (path.name, pattern.pattern)
    for path in json_files:
        value = json.loads(path.read_text(encoding="utf-8"))
        list(walk(value))
    ledger = json.loads((ROOT / "data/legacy313_anonymous_primary_v5.json").read_text(encoding="utf-8"))
    assert ledger["identity_mapping_saved"] is False
    rows = ledger["rows"]
    assert len(rows) == 313
    assert all(set(row) == ROW_KEYS for row in rows)
    assert [row["release_id"] for row in rows] == [f"R{index:04d}" for index in range(1, 314)]
    assert len({row["release_id"] for row in rows}) == 313
    print(json.dumps({"result": "PASS", "file_count": len(files), "json_count": len(json_files), "anonymous_person_rows": len(rows), "errors": 0}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
