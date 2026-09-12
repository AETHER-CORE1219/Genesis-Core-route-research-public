# Social-expression route external-factor robustness v7

[English](README.md) | [日本語](README_JA.md) | [Project overview](../.github/README.md) | [Study map](../docs/STUDY_MAP.md)

## Question and analysis surface

This release asks whether five aggregate associations found during development remain positive after measured external-factor adjustment and simultaneous correction across a fixed test family.

`development420` is a fixed 420-person development analysis. It is not the total size of the broader route-research corpus and is not an independent replication sample. Each person may support more than one documented social function. Field and occupation are not used as entry labels.

The public data are anonymous analysis projections. They permit recalculation of the reported statistics but do not provide an identity map or the complete raw-source-to-classification pipeline. Read the [reproducibility boundary](../docs/REPRODUCIBILITY_BOUNDARY.md).

## Result

In the fixed development420 dataset, all five predeclared aggregate social-function associations remained positive after adding birth era, reality-measurement regime, and collection source sequentially. The direction also remained positive in factor-specific secondary checks. A 9,999-draw person-package maxT analysis over the fixed 22-surface family retained all five primary associations after simultaneous correction.

Adjusted risk differences were +0.336 advocacy, +0.391 authored symbolic production, +0.280 organized realization, +0.325 technology implementation, and +0.321 embodied competition. Adjusted maxT p-values ranged from 0.0001 to 0.0047.

The supported claim is narrow: within fixed development420 and the frozen 22 surfaces, measured era, measurement regime, and collection source do not explain the five associations, and the declared joint null makes chance alone an implausible explanation. This is not an independent person-out replication, causal proof, validation of all 515 rules, or proof of a Western/Jyotish interaction.

Field and occupation are manifestation, covariate, moderator, or transport variables only—not entry labels.

## Read and reproduce

- [Methods in English](METHODS_EN.md)
- [Failures and limits in English](FAILURES_AND_LIMITS_EN.md)
- [Reproduction in English](REPRODUCTION_EN.md)
- [Public data dictionary](DATA_DICTIONARY_EN.md)
- [Machine-readable claim boundary](CLAIM_BOUNDARY.json)
- [Canonical results](RESULTS.json)
- [Japanese overview](README_JA.md)
- [Japanese methods](METHODS.md)
- [Japanese failures and limits](FAILURES_AND_LIMITS.md)
- [Japanese reproduction guide](REPRODUCTION.md)

From the repository root:

```bash
python -m pip install -r requirements-public.txt
python independent_social_expression_v7/scripts/reproduce_v7.py
python independent_social_expression_v7/scripts/validate_public_v7_privacy.py
```

A `PASS` confirms agreement with the stored public result. It does not establish independent replication or validate astrology as a whole.
