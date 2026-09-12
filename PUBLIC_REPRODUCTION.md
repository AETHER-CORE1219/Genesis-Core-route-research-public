# Public reproduction guide

## What the public package can reproduce

The public scripts recalculate frozen results from the released fixed or anonymous data projections. They check reported counts, estimators, permutation results, decision rules, and available privacy constraints.

The package does **not** regenerate every chart classification and every real-world action classification from raw birth and biographical source material. That distinction is described in [Reproducibility Boundary](docs/REPRODUCIBILITY_BOUNDARY.md).

## Requirements

- Python 3.10 or newer
- NumPy 2.2.6
- A fresh clone that preserves LF line endings

```bash
git -c core.autocrlf=false clone https://github.com/AETHER-CORE1219/Genesis-Core-route-research-public.git
cd Genesis-Core-route-research-public
python -m pip install -r requirements-public.txt
```

The repository includes `.gitattributes` so new Windows and Unix clones use LF for checksum-tracked text files. The explicit clone option also protects readers whose older global Git configuration would otherwise rewrite line endings.

## Verify every public research surface

```bash
python scripts/verify_public_release.py
```

The command:

1. verifies the root and versioned checksum manifests;
2. runs the public v1–v7 reproduction scripts;
3. runs the v4, v5, and v7 privacy validators;
4. returns a machine-readable summary and a nonzero exit code if any required check fails.

Use checksum-only mode when dependencies have not yet been installed:

```bash
python scripts/verify_public_release.py --checksums-only
```

## Verify only the latest v7 result

```bash
python independent_social_expression_v7/scripts/reproduce_v7.py
python independent_social_expression_v7/scripts/validate_public_v7_privacy.py
```

Expected headline output includes:

- `people: 420`
- `fixed_surfaces: 22`
- `estimable_surfaces: 18`
- `max_t_draws: 9999`
- `result: PASS`
- five entries under `selection_aware_results`

`PASS` means the script reproduced the stored public result and its declared checks. It does not mean that astrology as a whole was validated.

## Historical maintainer protocol

The root [REPRODUCTION.md](REPRODUCTION.md) is the preserved historical release-build protocol. It refers to private maintainer scripts and local research artifacts that are not included in this standalone repository. External users should run the commands in this public guide instead.

## Reporting a problem

Open a GitHub issue and include the commit, operating system, Python/NumPy versions, command, exit code, and final output. See [CONTRIBUTING.md](CONTRIBUTING.md).
