#!/usr/bin/env python3
import hashlib
import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
ERAS = ("BEFORE_1900", "1900_1949", "1950_1974", "1975_OR_LATER")
PERMUTATIONS = 200_000
DESIGN_EFFECT = 1.1
SEED_TEXT = "AKUW_AKS575_AUTHORED_CORRECTED_SINGLE_LATE_JOIN_V1"


def load(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def main():
    results = load("RESULTS.json")
    ledger = load("data/aks575_anonymous_late_join_v3.json")
    units = load("data/authored_corrected_unit_manifest_v3.json")
    heldout = results["heldout"]
    rows = ledger["rows"]
    assert len(rows) == 575 == len({row["subject_id_sha256"] for row in rows})
    assert units["unit_count"] == len(units["units"]) == 25
    stats = {era: {"n1": 0, "y1": 0, "n0": 0, "y0": 0, "unknown1": 0, "unknown0": 0} for era in ERAS}
    for row in rows:
        arm = "1" if row["candidate_exposed"] else "0"
        if row["analyzable"]:
            stats[row["era_stratum"]]["n" + arm] += 1
            stats[row["era_stratum"]]["y" + arm] += int(row["supported_outcome"])
        else:
            stats[row["era_stratum"]]["unknown" + arm] += 1
    assert stats == heldout["era_stats"]
    weights = heldout["era_weights"]
    rd = sum(weights[era] * (stats[era]["y1"] / stats[era]["n1"] - stats[era]["y0"] / stats[era]["n0"]) for era in ERAS)
    assert math.isclose(rd, heldout["era_standardized_risk_difference"], abs_tol=1e-15)
    seed = int(hashlib.sha256(SEED_TEXT.encode()).hexdigest()[:16], 16)
    rng = np.random.default_rng(seed)
    null = np.zeros(PERMUTATIONS, dtype=np.float64)
    for era in ERAS:
        s = stats[era]
        total_n, total_y = s["n1"] + s["n0"], s["y1"] + s["y0"]
        y1 = rng.hypergeometric(total_y, total_n - total_y, s["n1"], size=PERMUTATIONS)
        null += weights[era] * (y1 / s["n1"] - (total_y - y1) / s["n0"])
    permutation_p = (1 + int(np.count_nonzero(null >= rd - 1e-15))) / (PERMUTATIONS + 1)
    variance = 0.0
    for era in ERAS:
        s = stats[era]
        p1, p0 = s["y1"] / s["n1"], s["y0"] / s["n0"]
        variance += weights[era] ** 2 * (p1 * (1 - p1) / s["n1"] + p0 * (1 - p0) / s["n0"])
    se = math.sqrt(variance * DESIGN_EFFECT)
    cluster_p = 0.5 * math.erfc((rd / se) / math.sqrt(2))
    holm_p = min(1.0, 5 * max(permutation_p, cluster_p))
    assert math.isclose(permutation_p, heldout["permutation_one_sided_p"], abs_tol=1e-15)
    assert math.isclose(cluster_p, heldout["cluster_adjusted_one_sided_p"], abs_tol=1e-15)
    assert math.isclose(holm_p, heldout["holm_adjusted_p"], abs_tol=1e-15)
    print(json.dumps({
        "result": "PASS",
        "people": len(rows),
        "units": len(units["units"]),
        "exposed_analyzable": heldout["exposed_analyzable"],
        "unexposed_analyzable": heldout["unexposed_analyzable"],
        "era_standardized_risk_difference": rd,
        "permutation_p": permutation_p,
        "cluster_adjusted_p": cluster_p,
        "holm_adjusted_p": holm_p,
        "terminal_outcome": heldout["terminal_outcome"]
    }, sort_keys=True))


if __name__ == "__main__":
    main()
