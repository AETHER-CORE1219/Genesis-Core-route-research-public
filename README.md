# GenesisCore Social-Expression Research

English | [日本語の研究概要](README_JA.md)

Can structures defined from birth charts be associated with documented real-world actions?

> **New to astrology or statistics?** Begin with the [five-minute plain-language guide](docs/PLAIN_LANGUAGE_SUMMARY.md).

## What this project actually does

Imagine replacing a personal astrological reading with a checklist that gives the same answer whenever the same birth data are entered. Then compare that checklist with public records of what people actually did. That is the core of this research.

1. **Calculate:** date, time, and place of birth are converted into Western and Jyotish (Indian astrology) charts. The two traditions are calculated separately.
2. **Compare:** fixed chart conditions are compared with five broad kinds of documented activity—public advocacy, authored work, organizing people, building technology or products, and physical competition.
3. **Challenge:** the patterns are tested against alternative explanations, multiple comparisons, and different groups of people. Positive, failed, and non-positive results are all kept in the public record.

Here, an **association** means that a documented activity appeared at different rates between people who did and did not meet a fixed chart condition. It does not by itself establish cause, personal prediction, or scientific proof.

**Current position:** five broad associations remained positive inside a fixed 420-person development analysis, while three narrower formulations did not receive positive confirmation in separate-person tests. The latest v7 result tests the robustness of the five development associations; it is not an independent replication.

This repository publishes the evidence, calculations, and limits behind that work. **AETHERCORE** conducts the research and operates **GenesisCore**, its public analysis service.

## Research at a glance

| Public research surface | Size | What it represents |
|---|---:|---|
| Broader legacy route-research master ledger | 1,030 people | Multi-field corpus of notable public figures |
| Exact-like birth records in that ledger | 795 people | Records with exact or equivalent birth-time precision |
| Public subject-level legacy traces | 761 people | Named traces with field, birth-data provenance, chart snapshots, and route observations |
| Five-function development analysis | 420 people | Separate fixed analysis used to develop and test five non-exclusive social functions |
| Person-out stress tests | 575 / 1,457 / 313 | Different people, hypotheses, and test boundaries in v3, v4, and v5 |

These counts describe different research surfaces. They must not be added together, and the public files do not establish a simple identity mapping between the 761 named legacy traces and the anonymous 420-person analysis.

Read the [study map](docs/STUDY_MAP.md) before comparing results across releases.

## Research trajectory

The latest result is meaningful only alongside the tests that preceded it.

- **v1 — Measurement canary:** the first outcome-measurement design failed before an external route test was performed.
- **v2 — Candidate construction:** five non-exclusive functions and their candidate rules were built in the fixed 420-person development analysis.
- **v3–v5 — Separate-person stress tests:** three specific formulations were tested on 575-, 1,457-, and 313-person surfaces. None met its declared positive-confirmation rule. These were different hypotheses and were not all fully untouched cohorts.
- **v6 — Synthesis:** the development structures and non-positive tests were reorganized into more defensible levels of function, meaning family, finite branch, and person interpretation. No new inferential test was run.
- **v7 — Development robustness:** the analysis returned to the original development420 surface to ask whether measured external factors or fixed-family multiplicity explained the five aggregate associations.

Read the [study map](docs/STUDY_MAP.md) for the exact population and independence boundary of each release.

## Latest result: five functions under development-sample robustness testing

The five functions are non-exclusive. One person may have documented activity in more than one function.

| Social function | Adjusted risk difference | Simultaneous maxT p-value |
|---|---:|---:|
| Public advocacy and public-cause action | +33.60 percentage points | 0.0001 |
| Authored or symbolic production | +39.08 percentage points | 0.0001 |
| Organized collective realization | +27.95 percentage points | 0.0001 |
| Technology or product implementation | +32.49 percentage points | 0.0008 |
| Embodied competitive performance | +32.14 percentage points | 0.0047 |

All five remained positive after sequential adjustment for birth era, the way real-world evidence was measured, and collection-source group. They also remained positive in the declared factor-specific checks. A 9,999-draw simultaneous test across 22 predefined comparisons prevents the five headline results from being treated as five isolated tests.

### What this result supports

- Within the fixed development dataset and the declared 22-surface test family, the three measured external factors do not explain away the five associations.
- Chance alone is an implausible explanation under the declared simultaneous null.
- The reported statistics can be recalculated from the released anonymous matrices and code.

### Boundary of the result

- It is not independent replication in a new population, causal proof, or evidence of individual predictive accuracy.
- It does not validate all 515 development rules, all 136 meaning families, or a Western-by-Jyotish interaction.
- It does not remove every earlier researcher choice or every unmeasured confound.

Read the [v7 English overview](independent_social_expression_v7/README.md), [methods](independent_social_expression_v7/METHODS_EN.md), [failures and limits](independent_social_expression_v7/FAILURES_AND_LIMITS_EN.md), and [machine-readable claim boundary](independent_social_expression_v7/CLAIM_BOUNDARY.json).

## Why continue reading?

- **General readers:** see what was tested, what was found, and why a positive result can remain unresolved in the [plain-language summary](docs/PLAIN_LANGUAGE_SUMMARY.md).
- **Practicing astrologers:** inspect how MC-ruler, A10-lord, Amatya, relation, house, and varga structures enter candidate definitions in [astrological structure examples](docs/ASTROLOGICAL_STRUCTURE_EXAMPLES.md).
- **Researchers and skeptical editors:** compare development evidence with the non-positive person-out tests through the [study map](docs/STUDY_MAP.md), [methods](independent_social_expression_v7/METHODS_EN.md), and [reproducibility boundary](docs/REPRODUCIBILITY_BOUNDARY.md).
- **Developers:** run the complete released calculation suite with the [public reproduction guide](PUBLIC_REPRODUCTION.md).
- **Data reviewers:** inspect people, source coverage, anonymous schemas, and unresolved provenance in [data provenance](docs/DATA_PROVENANCE.md).
- **Editors and institutions:** use the [English research report](REPORT_EN.md), [citation metadata](CITATION.cff), and [disclosures](docs/DISCLOSURES.md).
- **Any reader encountering an internal term:** use the [glossary](docs/GLOSSARY.md).

## Recalculate the public results

With Python 3.10 or newer:

```bash
git -c core.autocrlf=false clone https://github.com/AETHER-CORE1219/Genesis-Core-route-research-public.git
cd Genesis-Core-route-research-public
python -m pip install -r requirements-public.txt
python scripts/verify_public_release.py
```

The repository also includes `.gitattributes` to preserve LF line endings. The explicit clone option protects older Git configurations that might otherwise rewrite checksum-tracked text. The verifier checks the published checksum manifests, runs the public v1–v7 reproduction scripts, and runs the available privacy validators. A full run takes roughly one minute on a typical current computer.

The public package recalculates results from released fixed or anonymous projections. It does not regenerate every birth chart, evidence judgment, and classification from raw source material. Read the [reproducibility boundary](docs/REPRODUCIBILITY_BOUNDARY.md) before describing the repository as end-to-end reproducible.

## Research operator and product relationship

The research is published by **AETHERCORE**, which also develops **GenesisCore**, a paid Western/Jyotish analysis service and a separate voluntary participant study. The commercial relationship is disclosed because research scrutiny, participant recruitment, and service awareness are connected activities.

- [AETHERCORE](https://aether-core.org/en)
- [GenesisCore](https://aether-core.org/en/genesiscore)
- [Free participant study](https://genesis-core-production.web.app/en)
- [Research participation terms](https://genesis-core-production.web.app/en/research/terms)

The repository does not ask readers to endorse the service. Research questions, criticism, failed reproductions, and documentation corrections are welcome through [GitHub Issues](https://github.com/AETHER-CORE1219/Genesis-Core-route-research-public/issues).

## Citation and license

Use the repository's [citation metadata](CITATION.cff) when citing the public package. Code and documentation are released under the [Apache License 2.0](LICENSE). Public biographical and birth-data source records retain their own source and rights context; the repository license does not relicense third-party source material.

Contact: [takatsusora@aether-core.org](mailto:takatsusora@aether-core.org)
