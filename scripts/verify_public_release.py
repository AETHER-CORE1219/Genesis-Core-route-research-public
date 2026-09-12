#!/usr/bin/env python3
"""Cross-platform verification for the public GenesisCore research package."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]

REPRODUCTION_COMMANDS = [
    ("v1", "independent_social_expression_v1/scripts/reproduce_measurement_failure_v1.py"),
    ("v2", "independent_social_expression_v2/scripts/reproduce_v2.py"),
    ("v3", "independent_social_expression_v3/scripts/reproduce_v3.py"),
    ("v4", "independent_social_expression_v4/scripts/reproduce_v4.py"),
    ("v5", "independent_social_expression_v5/scripts/reproduce_v5.py"),
    ("v6", "independent_social_expression_v6/scripts/reproduce_v6.py"),
    ("v7", "independent_social_expression_v7/scripts/reproduce_v7.py"),
]

PRIVACY_COMMANDS = [
    ("v4_privacy", "independent_social_expression_v4/scripts/validate_public_v4_privacy.py"),
    ("v5_privacy", "independent_social_expression_v5/scripts/validate_public_v5_privacy.py"),
    ("v7_privacy", "independent_social_expression_v7/scripts/validate_public_v7_privacy.py"),
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_manifest(manifest: Path) -> dict[str, object]:
    failures: list[dict[str, str]] = []
    checked = 0
    base = manifest.parent
    for raw_line in manifest.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(maxsplit=1)
        if len(parts) != 2:
            failures.append({"file": str(manifest), "error": "invalid checksum line"})
            continue
        expected, relative = parts
        relative = relative.lstrip("*")
        target = base / relative
        checked += 1
        if not target.is_file():
            failures.append({"file": relative, "error": "missing"})
            continue
        actual = sha256(target)
        if actual != expected.lower():
            failures.append(
                {"file": relative, "error": "checksum mismatch", "expected": expected, "actual": actual}
            )
    return {
        "manifest": str(manifest.relative_to(ROOT)),
        "checked": checked,
        "result": "PASS" if not failures else "FAIL",
        "failures": failures,
    }


def run_python(label: str, relative_script: str) -> dict[str, object]:
    script = ROOT / relative_script
    if not script.is_file():
        return {"label": label, "script": relative_script, "result": "FAIL", "error": "missing script"}
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    completed = subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    output = [line for line in completed.stdout.splitlines() if line.strip()]
    error = [line for line in completed.stderr.splitlines() if line.strip()]
    return {
        "label": label,
        "script": relative_script,
        "exit_code": completed.returncode,
        "result": "PASS" if completed.returncode == 0 else "FAIL",
        "last_output_line": output[-1] if output else None,
        "last_error_line": error[-1] if error else None,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--checksums-only",
        action="store_true",
        help="verify checksum manifests without running the reproduction scripts",
    )
    args = parser.parse_args()

    manifests = [ROOT / "CHECKSUMS.sha256"]
    documentation_manifest = ROOT / "DOCUMENTATION_CHECKSUMS.sha256"
    if documentation_manifest.is_file():
        manifests.append(documentation_manifest)
    manifests.extend(sorted(ROOT.glob("independent_social_expression_v*/CHECKSUMS.sha256")))
    checksum_results = [verify_manifest(path) for path in manifests]

    run_results: list[dict[str, object]] = []
    if not args.checksums_only:
        run_results.extend(run_python(label, script) for label, script in REPRODUCTION_COMMANDS)
        run_results.extend(run_python(label, script) for label, script in PRIVACY_COMMANDS)

    passed = all(item["result"] == "PASS" for item in checksum_results + run_results)
    summary = {
        "repository": "AETHER-CORE1219/Genesis-Core-route-research-public",
        "python": sys.version.split()[0],
        "checksum_manifests": checksum_results,
        "runs": run_results,
        "result": "PASS" if passed else "FAIL",
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
