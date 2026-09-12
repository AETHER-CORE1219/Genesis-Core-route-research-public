# Reproducing the v7 public result

## Requirements

- Python 3.10 or newer
- NumPy 2.2.6
- Repository text checked out with LF line endings

From the repository root:

```bash
python -m pip install -r requirements-public.txt
python independent_social_expression_v7/scripts/reproduce_v7.py
python independent_social_expression_v7/scripts/validate_public_v7_privacy.py
```

To verify all public versions and checksum manifests, run:

```bash
python scripts/verify_public_release.py
```

## Inputs

- `RESULTS.json` — canonical stored results.
- `CLAIM_BOUNDARY.json` — supported and unsupported claims.
- `data/development420_external_factor_matrix_v7.json.gz` — anonymous 420-person analysis matrix.
- `data/development420_observation_opportunity_v7.json.gz` — partial observation-opportunity measures.
- `data/development420_adversarial_decoy_memberships_v7.json.gz` — decoy rows and unique exposure sets.
- `data/PUBLIC_PROJECTION_ATTESTATION_V7.json` — public projection and privacy assertions.

## Recalculated outputs

`reproduce_v7.py` recalculates and compares at least:

- M0–M3 risk differences and HC3 standard errors;
- direction within birth-era and source-evidence strata;
- leave-one-source-out direction;
- observation-opportunity adjustment in the 311- and 109-person subcohorts;
- 9,999 within-era permutations;
- 9,999 within-source permutations;
- the 9,999-draw person-package maxT distribution across the fixed family;
- simultaneous p-values and one-sided lower bounds;
- 7,634 adversarial-decoy rows and 708 unique exposure sets;
- Western-only, Jyotish-only, and full both-system estimates;
- sensitivity quantities for unmeasured confounding;
- the final machine-readable claim boundary.

## Privacy validation

`validate_public_v7_privacy.py` checks the declared public JSON surfaces for prohibited identifying or private fields. The current public projection contains opaque release IDs and does not persist an identity mapping.

The validator is a deterministic schema and prohibited-field check. It is not a mathematical proof of anonymity.

## Expected result

The reproduction command should end with JSON containing:

```json
{
  "people": 420,
  "fixed_surfaces": 22,
  "estimable_surfaces": 18,
  "max_t_draws": 9999,
  "result": "PASS"
}
```

The actual output also contains factor classifications and all five selection-aware result objects.

The privacy validator should report `result: PASS`, `people: 420`, and `decoy_rows: 7634`.

## Meaning of PASS

`PASS` means that the public script reproduced the canonical result and its declared public checks from the released projections.

It does not mean:

- that a new sample confirmed the result;
- that the source classifications were independently repeated;
- that the complete raw-source pipeline was reproduced;
- that astrology as a whole was validated.

See [Reproducibility Boundary](../docs/REPRODUCIBILITY_BOUNDARY.md).
