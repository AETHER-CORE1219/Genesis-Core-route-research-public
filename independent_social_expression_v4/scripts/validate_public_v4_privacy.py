#!/usr/bin/env python3
"""Fail-closed privacy validator for the narrow public v4 bundle.

This validator deliberately validates only the materialized v4 publication
surface.  It does not read the private research worktree or attempt to validate
the scientific truth of the published result.
"""

from __future__ import annotations

import argparse
import gzip
import json
import os
import re
import shutil
import sys
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any


EXPECTED_PRIMARY_ROWS = 1_457
PRIMARY_RELATIVE_PATH = Path("data/confirmation1457_anonymous_primary_v4.json")
DECOY_RELATIVE_PATH = Path("data/decoy_summary_v4.json")
PERMUTATION_RELATIVE_PATH = Path("data/primary_permutation_draws_v4.json.gz")
RESULTS_RELATIVE_PATH = Path("RESULTS.json")
EXPECTED_DECOY_ROWS = 98
EXPECTED_PERMUTATION_DRAWS = 9_999
MAX_GZIP_DECOMPRESSED_BYTES = 16 * 1024 * 1024
PRIMARY_ROW_KEYS = {
    "release_id",
    "fixed_stratum",
    "family_exposure",
    "endpoint_state",
}
ALLOWED_FILE_SUFFIXES = {".json", ".md", ".py", ".sha256", ".txt"}

RELEASE_ID = re.compile(r"^(?P<prefix>[A-Z][A-Z0-9_-]*?)(?P<number>[0-9]+)$")
FIXED_STRATUM = re.compile(
    r"^(?:EN|FR|OTHER)\|(?:BEFORE_1900|1900_1924|1925_1949|1950_AND_LATER)"
    r"\|TEXT_(?:SHORT|MEDIUM|LONG)$"
)
ENDPOINT_STATES = {
    "SUPPORTED",
    "PARTIAL",
    "NO_DIRECT_ANCHOR_OBSERVED_IN_ADEQUATE_FIXED_SOURCE",
    "UNKNOWN_NO_ANALYSIS_ELIGIBLE_EVIDENCE",
}
FIXED_STRATA_DOMAIN = tuple(
    f"{language}|{era}|TEXT_{length}"
    for language in ("EN", "FR", "OTHER")
    for era in ("BEFORE_1900", "1900_1924", "1925_1949", "1950_AND_LATER")
    for length in ("SHORT", "MEDIUM", "LONG")
)

DATA_TEXT_PATTERNS = (
    ("qid", re.compile(r"(?<![A-Z0-9])Q[1-9][0-9]{1,11}(?![A-Z0-9])", re.I)),
    ("url", re.compile(r"(?:https?|ftp)://|www\.", re.I)),
    ("private_path", re.compile(r"/(?:home|Users)/|[A-Z]:\\\\Users\\\\|file://", re.I)),
    ("private_workspace", re.compile(r"\.research_(?:worktrees|sources)|\\\\\\\\wsl", re.I)),
)

# These patterns look for credential *values*, not general documentation words
# such as "credential" or "source".  This keeps ordinary methods prose usable.
CREDENTIAL_PATTERNS = (
    (
        "credential_assignment",
        re.compile(
            r"(?i)\b(?:api[_-]?key|access[_-]?token|secret|password)\s*[:=]\s*"
            r"[\"']?[A-Za-z0-9_./+=-]{8,}"
        ),
    ),
    ("authorization_header", re.compile(r"(?i)\bAuthorization\s*:\s*Bearer\s+\S+")),
    ("bearer_token", re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/-]{16,}")),
    ("private_key", re.compile(r"-----BEGIN\s+(?:RSA\s+|EC\s+|OPENSSH\s+)?PRIVATE\s+KEY-----")),
    ("aws_access_key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("github_token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b")),
    ("openai_token", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("slack_token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{12,}\b")),
    ("google_api_key", re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b")),
)

PRIVATE_PATH_PATTERNS = (
    ("unix_home", re.compile(r"/" + r"home/[^\s\"'<>]+", re.I)),
    ("mac_home", re.compile(r"/" + r"Users/[^\s\"'<>]+", re.I)),
    ("windows_home", re.compile(r"[A-Z]:\\\\Users\\\\[^\s\"'<>]+", re.I)),
    ("file_uri", re.compile(r"file" + r":/{2,3}[^\s\"'<>]+", re.I)),
    ("private_research_path", re.compile(r"\.research_" + r"(?:worktrees|sources)", re.I)),
    ("wsl_unc", re.compile(r"\\\\" + r"wsl(?:\$)?\\", re.I)),
)

FORBIDDEN_FILENAMES = {
    ".env",
    ".env.local",
    "id_rsa",
    "id_ed25519",
    "credentials.json",
}
FORBIDDEN_SUFFIXES = {".key", ".pem", ".p12", ".pfx"}


class DuplicateJsonKey(ValueError):
    """Raised when JSON contains duplicate object keys."""


def _object_without_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJsonKey(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _load_json(path: Path, text: str) -> Any:
    try:
        return json.loads(text, object_pairs_hook=_object_without_duplicates)
    except (json.JSONDecodeError, DuplicateJsonKey) as exc:
        raise ValueError(f"invalid JSON {path}: {exc}") from exc


def _iter_paths_without_following_symlinks(root: Path) -> tuple[list[Path], list[str]]:
    files: list[Path] = []
    errors: list[str] = []
    if root.is_symlink():
        return files, [f"bundle root is a symlink: {root}"]
    if not root.is_dir():
        return files, [f"bundle root is not a directory: {root}"]

    for current, directories, filenames in os.walk(root, followlinks=False):
        current_path = Path(current)
        for name in list(directories):
            path = current_path / name
            if path.is_symlink():
                errors.append(f"symlink is forbidden: {path.relative_to(root)}")
                directories.remove(name)
        for name in filenames:
            path = current_path / name
            if path.is_symlink():
                errors.append(f"symlink is forbidden: {path.relative_to(root)}")
            elif not path.is_file():
                errors.append(f"non-regular file is forbidden: {path.relative_to(root)}")
            else:
                files.append(path)
    return sorted(files), errors


def _scan_bundle_text(relative: Path, text: str, errors: list[str]) -> None:
    for marker, pattern in PRIVATE_PATH_PATTERNS:
        if pattern.search(text):
            errors.append(f"{relative}: absolute/private path marker: {marker}")
    for marker, pattern in CREDENTIAL_PATTERNS:
        if pattern.search(text):
            errors.append(f"{relative}: credential marker: {marker}")


def _exact_object_keys(
    value: Any, expected: set[str], location: str, errors: list[str]
) -> bool:
    if not isinstance(value, dict):
        errors.append(f"{location}: expected JSON object")
        return False
    if set(value) != expected:
        errors.append(
            f"{location}: exact keys required; found={sorted(value)}, expected={sorted(expected)}"
        )
        return False
    return True


def _validate_primary(document: Any, relative: Path, errors: list[str]) -> int:
    wrapper_keys = {
        "schema_id",
        "release_id_scope",
        "identity_mapping_saved",
        "shuffle_seed_saved",
        "row_count",
        "rows",
    }
    if not _exact_object_keys(document, wrapper_keys, str(relative), errors):
        return 0
    if document["schema_id"] != "INDEPENDENT_SOCIAL_EXPRESSION_PRIMARY_LEDGER_V4":
        errors.append(f"{relative}: unexpected schema_id")
    if document["release_id_scope"] != "V4_ONLY_UNLINKABLE":
        errors.append(f"{relative}: release_id_scope must be V4_ONLY_UNLINKABLE")
    if document["identity_mapping_saved"] is not False:
        errors.append(f"{relative}: identity_mapping_saved must be false")
    if document["shuffle_seed_saved"] is not False:
        errors.append(f"{relative}: shuffle_seed_saved must be false")
    if document["row_count"] != EXPECTED_PRIMARY_ROWS:
        errors.append(f"{relative}: row_count must be {EXPECTED_PRIMARY_ROWS}")
    if not isinstance(document["rows"], list):
        errors.append(f"{relative}: rows must be an array")
        return 0
    rows = document["rows"]
    if len(rows) != EXPECTED_PRIMARY_ROWS:
        errors.append(
            f"{relative}: expected {EXPECTED_PRIMARY_ROWS} rows, found {len(rows)}"
        )
        return len(rows)

    identifiers: list[str] = []
    parsed: list[tuple[str, int, int]] = []
    for index, row in enumerate(rows):
        location = f"{relative}:rows[{index}]"
        if not isinstance(row, dict):
            errors.append(f"{location}: row must be an object")
            continue
        if set(row) != PRIMARY_ROW_KEYS:
            errors.append(
                f"{location}: exact keys required; found={sorted(row)}, "
                f"expected={sorted(PRIMARY_ROW_KEYS)}"
            )
            continue
        release_id = row["release_id"]
        if not isinstance(release_id, str):
            errors.append(f"{location}: release_id must be a string")
        else:
            identifiers.append(release_id)
            match = RELEASE_ID.fullmatch(release_id)
            if not match:
                errors.append(f"{location}: release_id is not an opaque sequential ID")
            else:
                parsed.append(
                    (match.group("prefix"), int(match.group("number")), len(match.group("number")))
                )
        if not isinstance(row["fixed_stratum"], str) or not FIXED_STRATUM.fullmatch(
            row["fixed_stratum"]
        ):
            errors.append(f"{location}: fixed_stratum is outside the frozen public domain")
        if type(row["family_exposure"]) is not int or row["family_exposure"] not in (0, 1):
            errors.append(f"{location}: family_exposure must be integer 0 or 1")
        if row["endpoint_state"] not in ENDPOINT_STATES:
            errors.append(f"{location}: endpoint_state is outside the frozen domain")

    if len(identifiers) != len(set(identifiers)):
        errors.append(f"{relative}: release_id values are not unique")
    expected_identifiers = [f"R{number:04d}" for number in range(1, EXPECTED_PRIMARY_ROWS + 1)]
    if identifiers != expected_identifiers:
        errors.append(f"{relative}: release_id values must be exact R0001..R1457 in row order")
    if len(parsed) == EXPECTED_PRIMARY_ROWS:
        prefixes = {item[0] for item in parsed}
        widths = {item[2] for item in parsed}
        numbers = [item[1] for item in parsed]
        if len(prefixes) != 1 or len(widths) != 1:
            errors.append(f"{relative}: release_id prefix/width is not constant")
        if numbers != list(range(1, EXPECTED_PRIMARY_ROWS + 1)):
            errors.append(f"{relative}: release_id values are not sequential in frozen row order")
    observed_strata = {row.get("fixed_stratum") for row in rows if isinstance(row, dict)}
    if observed_strata != set(FIXED_STRATA_DOMAIN):
        errors.append(f"{relative}: primary rows must cover the exact frozen 36-stratum domain")
    observed_endpoints = {row.get("endpoint_state") for row in rows if isinstance(row, dict)}
    if observed_endpoints != ENDPOINT_STATES:
        errors.append(f"{relative}: primary rows must contain the exact four endpoint states")
    return len(rows)


def _validate_decoys(document: Any, relative: Path, errors: list[str]) -> None:
    wrapper_keys = {
        "schema_id",
        "decoy_count",
        "person_level_decoy_vectors_published",
        "rows",
    }
    if not _exact_object_keys(document, wrapper_keys, str(relative), errors):
        return
    if document["schema_id"] != "INDEPENDENT_SOCIAL_EXPRESSION_DECOY_SUMMARY_V4":
        errors.append(f"{relative}: unexpected schema_id")
    if document["decoy_count"] != EXPECTED_DECOY_ROWS:
        errors.append(f"{relative}: decoy_count must be {EXPECTED_DECOY_ROWS}")
    if document["person_level_decoy_vectors_published"] is not False:
        errors.append(f"{relative}: person-level decoy vectors must not be published")
    rows = document["rows"]
    if not isinstance(rows, list) or len(rows) != EXPECTED_DECOY_ROWS:
        errors.append(f"{relative}: expected {EXPECTED_DECOY_ROWS} aggregate decoy rows")
        return
    expected_keys = {
        "decoy_id",
        "estimable_stratum_count",
        "estimate",
        "exposed_decided_person_count",
        "status",
    }
    expected_ids = [f"DECOY_SET_{number:03d}" for number in range(EXPECTED_DECOY_ROWS)]
    observed_ids: list[str] = []
    for index, row in enumerate(rows):
        location = f"{relative}:rows[{index}]"
        if not _exact_object_keys(row, expected_keys, location, errors):
            continue
        observed_ids.append(row["decoy_id"])
        if row["status"] not in {"ESTIMABLE", "NON_ESTIMABLE"}:
            errors.append(f"{location}: invalid status")
        for key in ("estimable_stratum_count", "exposed_decided_person_count"):
            if type(row[key]) is not int or row[key] < 0:
                errors.append(f"{location}: {key} must be a nonnegative integer")
        if row["estimate"] is not None and type(row["estimate"]) not in {int, float}:
            errors.append(f"{location}: estimate must be numeric or null")
    if observed_ids != expected_ids:
        errors.append(f"{relative}: decoy IDs must be unique and sequential")


def _validate_permutations(document: Any, relative: Path, errors: list[str]) -> None:
    wrapper_keys = {
        "schema_id",
        "draw_count",
        "draw_representation",
        "exceed_or_equal_count",
        "fixed_strata",
        "one_sided_p",
        "rng",
        "seed",
        "statistics_float64_le_sha256",
        "y1_supported_draws",
    }
    if not _exact_object_keys(document, wrapper_keys, str(relative), errors):
        return
    if document["schema_id"] != "INDEPENDENT_SOCIAL_EXPRESSION_PERMUTATION_DRAWS_V4":
        errors.append(f"{relative}: unexpected schema_id")
    if document["draw_count"] != EXPECTED_PERMUTATION_DRAWS:
        errors.append(f"{relative}: draw_count must be {EXPECTED_PERMUTATION_DRAWS}")
    if document["draw_representation"] != "SUPPORTED_COUNT_IN_EXPOSED_ARM_BY_FIXED_STRATUM":
        errors.append(f"{relative}: unexpected draw representation")
    if document["rng"] != "NumPy Generator(PCG64(primary_seed))":
        errors.append(f"{relative}: unexpected RNG declaration")
    if type(document["seed"]) is not int:
        errors.append(f"{relative}: seed must be an integer")
    if not isinstance(document["statistics_float64_le_sha256"], str) or not re.fullmatch(
        r"[0-9a-f]{64}", document["statistics_float64_le_sha256"]
    ):
        errors.append(f"{relative}: invalid statistics digest")
    if type(document["exceed_or_equal_count"]) is not int:
        errors.append(f"{relative}: exceed_or_equal_count must be an integer")
    if type(document["one_sided_p"]) not in {int, float}:
        errors.append(f"{relative}: one_sided_p must be numeric")

    strata = document["fixed_strata"]
    strata_keys = {
        "exposed_decided",
        "fixed_stratum",
        "harmonic_weight",
        "total_supported",
        "unexposed_decided",
    }
    if not isinstance(strata, list) or len(strata) != 24:
        errors.append(f"{relative}: fixed_strata must contain 24 rows")
        return
    for index, row in enumerate(strata):
        location = f"{relative}:fixed_strata[{index}]"
        if not _exact_object_keys(row, strata_keys, location, errors):
            continue
        if not isinstance(row["fixed_stratum"], str) or not FIXED_STRATUM.fullmatch(
            row["fixed_stratum"]
        ):
            errors.append(f"{location}: invalid fixed_stratum")
        for key in ("exposed_decided", "total_supported", "unexposed_decided"):
            if type(row[key]) is not int or row[key] < 0:
                errors.append(f"{location}: {key} must be a nonnegative integer")
        if type(row["harmonic_weight"]) not in {int, float}:
            errors.append(f"{location}: harmonic_weight must be numeric")

    draws = document["y1_supported_draws"]
    if not isinstance(draws, list) or len(draws) != EXPECTED_PERMUTATION_DRAWS:
        errors.append(f"{relative}: expected {EXPECTED_PERMUTATION_DRAWS} draw rows")
        return
    for index, draw in enumerate(draws):
        if (
            not isinstance(draw, list)
            or len(draw) != len(strata)
            or any(type(value) is not int or value < 0 for value in draw)
        ):
            errors.append(f"{relative}: invalid permutation draw at index {index}")
            break


def _validate_results_consistency(
    results: Any, primary: Any, permutations: Any, errors: list[str]
) -> None:
    location = str(RESULTS_RELATIVE_PATH)
    if not isinstance(results, dict) or not isinstance(primary, dict) or not isinstance(
        permutations, dict
    ):
        errors.append(f"{location}: cross-file consistency inputs are not objects")
        return
    try:
        rows = primary["rows"]
        population = results["population"]
        measurement = results["measurement"]
        fixed_permutation_strata = [
            row["fixed_stratum"] for row in permutations["fixed_strata"]
        ]
    except (KeyError, TypeError) as exc:
        errors.append(f"{location}: missing cross-file field: {exc}")
        return

    exposure_counts = Counter(row["family_exposure"] for row in rows)
    endpoint_counts = Counter(row["endpoint_state"] for row in rows)
    checks = (
        (
            population.get("primary_independent_person_pages") == EXPECTED_PRIMARY_ROWS,
            "primary_independent_person_pages mismatch",
        ),
        (population.get("all_primary_stratum_count") == 36, "all_primary_stratum_count mismatch"),
        (population.get("primary_exposed") == exposure_counts[1], "primary_exposed mismatch"),
        (population.get("primary_unexposed") == exposure_counts[0], "primary_unexposed mismatch"),
        (
            measurement.get("endpoint_state_counts_primary") == dict(endpoint_counts),
            "endpoint_state_counts_primary mismatch",
        ),
        (
            population.get("fixed_estimable_stratum_count") == 24,
            "fixed_estimable_stratum_count mismatch",
        ),
        (
            population.get("fixed_estimable_strata") == fixed_permutation_strata,
            "fixed_estimable_strata mismatch",
        ),
    )
    for passed, message in checks:
        if not passed:
            errors.append(f"{location}: {message}")


def validate_bundle(root: Path) -> dict[str, Any]:
    root = root.absolute()
    files, errors = _iter_paths_without_following_symlinks(root)
    documents: dict[Path, Any] = {}

    for path in files:
        relative = path.relative_to(root)
        if path.name in FORBIDDEN_FILENAMES or path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"{relative}: credential-bearing filename is forbidden")
        is_permutation_gzip = relative == PERMUTATION_RELATIVE_PATH
        if path.suffix.lower() not in ALLOWED_FILE_SUFFIXES and not is_permutation_gzip:
            errors.append(f"{relative}: unsupported/binary file type is forbidden")
            continue
        try:
            if is_permutation_gzip:
                with gzip.open(path, "rb") as stream:
                    payload = stream.read(MAX_GZIP_DECOMPRESSED_BYTES + 1)
                if len(payload) > MAX_GZIP_DECOMPRESSED_BYTES:
                    errors.append(f"{relative}: decompressed JSON exceeds safety limit")
                    continue
                text = payload.decode("utf-8")
            else:
                text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError) as exc:
            errors.append(f"{relative}: file is not valid UTF-8 text")
            continue
        _scan_bundle_text(relative, text, errors)
        if path.suffix.lower() == ".json" or is_permutation_gzip:
            try:
                document = _load_json(relative, text)
                documents[relative] = document
            except ValueError as exc:
                errors.append(str(exc))

        if relative.parts and relative.parts[0] == "data":
            for marker, pattern in DATA_TEXT_PATTERNS:
                if pattern.search(text):
                    errors.append(f"{relative}: forbidden data marker: {marker}")

    expected_data = {
        PRIMARY_RELATIVE_PATH,
        DECOY_RELATIVE_PATH,
        PERMUTATION_RELATIVE_PATH,
    }
    observed_data_files = {
        path.relative_to(root)
        for path in files
        if path.relative_to(root).parts and path.relative_to(root).parts[0] == "data"
    }
    unexpected_data = observed_data_files - expected_data
    missing_data = expected_data - observed_data_files
    for relative in sorted(unexpected_data):
        errors.append(f"unexpected data file is forbidden: {relative}")
    for relative in sorted(missing_data):
        errors.append(f"required data file missing: {relative}")

    primary_rows = 0
    if PRIMARY_RELATIVE_PATH not in documents:
        errors.append(f"required primary data missing or invalid: {PRIMARY_RELATIVE_PATH}")
    else:
        primary_rows = _validate_primary(
            documents[PRIMARY_RELATIVE_PATH], PRIMARY_RELATIVE_PATH, errors
        )
    if DECOY_RELATIVE_PATH not in documents:
        errors.append(f"required decoy summary missing or invalid: {DECOY_RELATIVE_PATH}")
    else:
        _validate_decoys(documents[DECOY_RELATIVE_PATH], DECOY_RELATIVE_PATH, errors)
    if PERMUTATION_RELATIVE_PATH not in documents:
        errors.append(f"required permutation JSON missing or invalid: {PERMUTATION_RELATIVE_PATH}")
    else:
        _validate_permutations(
            documents[PERMUTATION_RELATIVE_PATH], PERMUTATION_RELATIVE_PATH, errors
        )
    if RESULTS_RELATIVE_PATH not in documents:
        errors.append(f"required results JSON missing or invalid: {RESULTS_RELATIVE_PATH}")
    elif (
        PRIMARY_RELATIVE_PATH in documents
        and PERMUTATION_RELATIVE_PATH in documents
    ):
        _validate_results_consistency(
            documents[RESULTS_RELATIVE_PATH],
            documents[PRIMARY_RELATIVE_PATH],
            documents[PERMUTATION_RELATIVE_PATH],
            errors,
        )

    return {
        "schema_id": "PUBLIC_V4_PRIVACY_VALIDATION_V1",
        "status": "PASS" if not errors else "FAIL",
        "bundle_root": str(root),
        "checked_file_count": len(files),
        "parsed_json_count": len(documents),
        "primary_row_count": primary_rows,
        "errors": sorted(set(errors)),
    }


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_gzip_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as stream:
        json.dump(value, stream, separators=(",", ":"), sort_keys=True)


def _make_self_test_fixture(root: Path) -> None:
    (root / "scripts").mkdir(parents=True, exist_ok=True)
    shutil.copy2(Path(__file__), root / "scripts" / Path(__file__).name)
    (root / "README.md").write_text("# Public v4 test bundle\n", encoding="utf-8")
    strata = list(FIXED_STRATA_DOMAIN)
    endpoint_cycle = list(sorted(ENDPOINT_STATES))
    rows = [
        {
            "release_id": f"R{number:04d}",
            "fixed_stratum": strata[(number - 1) % len(strata)],
            "family_exposure": int(number <= 59),
            "endpoint_state": endpoint_cycle[(number - 1) % len(endpoint_cycle)],
        }
        for number in range(1, EXPECTED_PRIMARY_ROWS + 1)
    ]
    _write_json(
        root / PRIMARY_RELATIVE_PATH,
        {
            "schema_id": "INDEPENDENT_SOCIAL_EXPRESSION_PRIMARY_LEDGER_V4",
            "release_id_scope": "V4_ONLY_UNLINKABLE",
            "identity_mapping_saved": False,
            "shuffle_seed_saved": False,
            "row_count": EXPECTED_PRIMARY_ROWS,
            "rows": rows,
        },
    )
    _write_json(
        root / DECOY_RELATIVE_PATH,
        {
            "schema_id": "INDEPENDENT_SOCIAL_EXPRESSION_DECOY_SUMMARY_V4",
            "decoy_count": EXPECTED_DECOY_ROWS,
            "person_level_decoy_vectors_published": False,
            "rows": [
                {
                    "decoy_id": f"DECOY_SET_{number:03d}",
                    "estimable_stratum_count": 24,
                    "estimate": 0.0,
                    "exposed_decided_person_count": 50,
                    "status": "ESTIMABLE",
                }
                for number in range(EXPECTED_DECOY_ROWS)
            ],
        },
    )
    permutation_strata = [
        {
            "exposed_decided": 1,
            "fixed_stratum": stratum,
            "harmonic_weight": 1.0 / 24,
            "total_supported": 1,
            "unexposed_decided": 1,
        }
        for stratum in strata[:24]
    ]
    _write_gzip_json(
        root / PERMUTATION_RELATIVE_PATH,
        {
            "schema_id": "INDEPENDENT_SOCIAL_EXPRESSION_PERMUTATION_DRAWS_V4",
            "draw_count": EXPECTED_PERMUTATION_DRAWS,
            "draw_representation": "SUPPORTED_COUNT_IN_EXPOSED_ARM_BY_FIXED_STRATUM",
            "exceed_or_equal_count": 0,
            "fixed_strata": permutation_strata,
            "one_sided_p": 0.0001,
            "rng": "NumPy Generator(PCG64(primary_seed))",
            "seed": 20260817,
            "statistics_float64_le_sha256": "0" * 64,
            "y1_supported_draws": [
                [0 for _ in permutation_strata]
                for _ in range(EXPECTED_PERMUTATION_DRAWS)
            ],
        },
    )
    endpoint_counts = dict(Counter(row["endpoint_state"] for row in rows))
    _write_json(
        root / RESULTS_RELATIVE_PATH,
        {
            "schema_id": "INDEPENDENT_SOCIAL_EXPRESSION_RESULTS_V4_TEST",
            "population": {
                "primary_independent_person_pages": EXPECTED_PRIMARY_ROWS,
                "all_primary_stratum_count": 36,
                "primary_exposed": 59,
                "primary_unexposed": EXPECTED_PRIMARY_ROWS - 59,
                "fixed_estimable_stratum_count": 24,
                "fixed_estimable_strata": [row["fixed_stratum"] for row in permutation_strata],
            },
            "measurement": {"endpoint_state_counts_primary": endpoint_counts},
        },
    )


def run_self_test() -> dict[str, Any]:
    failures: list[str] = []
    with tempfile.TemporaryDirectory(prefix="public-v4-privacy-") as temporary:
        base = Path(temporary)

        good = base / "good"
        _make_self_test_fixture(good)
        if validate_bundle(good)["status"] != "PASS":
            failures.append("valid fixture did not pass")

        cases: dict[str, Any] = {
            "extra_primary_key": lambda root: _mutate_primary_extra_key(root),
            "duplicate_release_id": lambda root: _mutate_primary_duplicate_id(root),
            "data_url": lambda root: _write_json(
                root / "data/leak.json", {"schema_id": "LEAK", "note": "https://example.invalid"}
            ),
            "private_path": lambda root: (root / "README.md").write_text(
                "internal location: " + "/" + "home/example/private.json\n", encoding="utf-8"
            ),
            "credential": lambda root: (root / "README.md").write_text(
                "api_" + "key = " + "abcdefghijklmnopqrstuvwxyz\n", encoding="utf-8"
            ),
            "malformed_json": lambda root: (root / "data/broken.json").write_text(
                "{not json}\n", encoding="utf-8"
            ),
            "malformed_gzip_json": lambda root: _overwrite_bad_gzip(root),
            "symlink": lambda root: os.symlink(
                root / "README.md", root / "data/publication-link"
            ),
        }
        for name, mutate in cases.items():
            root = base / name
            _make_self_test_fixture(root)
            mutate(root)
            if validate_bundle(root)["status"] != "FAIL":
                failures.append(f"negative case unexpectedly passed: {name}")

    return {
        "schema_id": "PUBLIC_V4_PRIVACY_SELF_TEST_V1",
        "status": "PASS" if not failures else "FAIL",
        "positive_cases": 1,
        "negative_cases": len(cases),
        "failures": failures,
    }


def _read_primary(root: Path) -> dict[str, Any]:
    return json.loads((root / PRIMARY_RELATIVE_PATH).read_text(encoding="utf-8"))


def _mutate_primary_extra_key(root: Path) -> None:
    document = _read_primary(root)
    document["rows"][0]["person_id"] = "P1"
    _write_json(root / PRIMARY_RELATIVE_PATH, document)


def _mutate_primary_duplicate_id(root: Path) -> None:
    document = _read_primary(root)
    document["rows"][1]["release_id"] = document["rows"][0]["release_id"]
    _write_json(root / PRIMARY_RELATIVE_PATH, document)


def _overwrite_bad_gzip(root: Path) -> None:
    with gzip.open(root / PERMUTATION_RELATIVE_PATH, "wt", encoding="utf-8") as stream:
        stream.write("{not json}\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--bundle-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="narrow v4 bundle root (defaults to this script's bundle)",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="run positive and negative synthetic privacy checks",
    )
    args = parser.parse_args()

    result = run_self_test() if args.self_test else validate_bundle(args.bundle_root)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
