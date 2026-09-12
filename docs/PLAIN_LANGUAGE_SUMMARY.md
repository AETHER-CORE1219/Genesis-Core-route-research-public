# Plain-language summary

## The question

Astrology makes structured claims from birth data, but those claims are usually presented as individual interpretations. This research asks a narrower and more testable question:

> Are predefined Western and Jyotish chart structures associated with documented real-world actions?

The project does not begin by assuming that astrology is true. It treats astrological rules as candidates that must survive contact with recorded human activity, competing explanations, multiple testing, and new groups of people.

## The people and records

The wider route-research program tracks 1,030 notable public figures from several fields, including the arts, science and technology, business, sport, politics, humanities, religion, activism, and exploration. Of those records, 795 are classified as exact-like birth records. Public subject-level legacy materials contain 761 named traces with field information, birth-data provenance, selected Western and Jyotish chart facts, and route observations.

The newest five-function robustness result uses a separate fixed 420-person development analysis. The public release does not provide an identity mapping between those anonymous 420 rows and the 761 named legacy traces. These numbers describe different research surfaces and must not be treated as one cumulative sample.

## Why the study uses activities rather than occupations

A single occupational label compresses a life too aggressively. A politician may also write books, organize institutions, build a public movement, or compete in sport. An engineer may produce theory, build a working product, and lead an organization.

The study therefore treats five activities as non-exclusive outcomes:

1. **Public advocacy and public-cause action** — acting for rights, reform, protection, or a public cause.
2. **Authored or symbolic production** — creating books, theories, music, art, or other durable symbolic work.
3. **Organized collective realization** — forming, directing, or coordinating organizations and collective projects.
4. **Technology or product implementation** — turning a method, design, or technical idea into a working product or system.
5. **Embodied competitive performance** — using trained physical ability in measured competition.

One person may support several functions. The outcome is based on activity documented in fixed source material. A missing activity in that material is not treated as proof that the activity never occurred in the person's life.

## What was compared

The astrology side was structured separately under Western and Jyotish frameworks. The five headline tests used a both-system exposure definition fixed for the relevant function. Western and Jyotish were not simply counted as two votes.

The underlying candidate structures are more specific than the anonymous Boolean fields. Public examples use roles such as the Western MC ruler and the Jyotish A10 lord or Amatya candidate, together with directed relations, dispositor or lordship chains, angular or vocational house classes, and D10 or Dusthana carriers. Separate-person tests include a Jyotish Mars–Mercury organized-realization family and a strict Saturn-to-Jupiter embodied-competition chain. Both failed their declared positive-confirmation rules. See [Astrological Structure Examples](ASTROLOGICAL_STRUCTURE_EXAMPLES.md).

The reality side recorded whether a person's fixed source material supported each activity. The study then compared activity rates between people who did and did not meet the fixed chart-structure exposure for that function.

The latest v7 analysis added three measured external factors one at a time:

- birth era;
- the regime used to measure real-world evidence;
- the collection-source group.

It also checked results within factor levels, adjusted for partial observation opportunity, compared Western-only and Jyotish-only surfaces, and evaluated the fixed family of 22 surfaces with 9,999 person-package maxT draws.

## What was found

All five adjusted associations remained positive in the fixed 420-person development analysis.

| Function | Adjusted difference | Simultaneous p-value |
|---|---:|---:|
| Public advocacy | +33.60 percentage points | 0.0001 |
| Authored production | +39.08 percentage points | 0.0001 |
| Organized collective realization | +27.95 percentage points | 0.0001 |
| Technology or product implementation | +32.49 percentage points | 0.0008 |
| Embodied competition | +32.14 percentage points | 0.0047 |

Within this dataset and the declared test family, the measured factors did not explain away the five associations. The result also makes chance alone implausible under the declared simultaneous null.

## What the result does not prove

The same 420-person development material contributed to candidate formation. The result is therefore not an independent replication in new people.

It also does not prove:

- that astrology causes the documented actions;
- that every unmeasured confound has been removed;
- that all 515 development rules or 136 meaning families are valid;
- that Western and Jyotish have a formally tested interaction;
- that a chart can deterministically predict occupation, behavior, or the future;
- that the complete path from raw birth and biographical sources to every classification is publicly reproducible.

## The non-positive tests

The repository preserves results that did not confirm narrower hypotheses.

- A broad authored-production mechanism aggregate did not reproduce in a separate 575-person surface.
- A two-branch organized-realization family did not reproduce the predeclared development-sized effect in a 1,457-person primary analysis.
- A strict embodied-competition branch was non-positive in a separate 313-person surface; a less restrictive direction remained unconfirmed.

These tests do not cancel the five development associations, because they tested different candidate units. They do show that a positive development pattern cannot be converted automatically into a portable rule.

## What can be checked publicly

The repository provides anonymous analysis matrices, frozen result files, machine-readable claim boundaries, checksums, reproduction scripts, and privacy validators. A public verifier runs the versioned v1–v7 calculations and checks the released files:

```bash
python -m pip install -r requirements-public.txt
python scripts/verify_public_release.py
```

This is result recalculation from released projections. It is not complete regeneration from raw sources. See [Reproducibility Boundary](REPRODUCIBILITY_BOUNDARY.md).

## Why the project is public

A result about astrology is useful only if people with different expectations can inspect the same evidence. The public package is intended for astrologers, skeptical investigators, researchers, developers, and editors—not only for people who already agree with the conclusion.

AETHERCORE also develops GenesisCore, a paid analysis service, and operates a separate voluntary participant study. That commercial and research relationship is disclosed in [Disclosures](DISCLOSURES.md). The repository asks for scrutiny, not endorsement.

## Continue reading

- [Study Map](STUDY_MAP.md)
- [English Research Report](../REPORT_EN.md)
- [v7 Methods](../independent_social_expression_v7/METHODS_EN.md)
- [v7 Failures and Limits](../independent_social_expression_v7/FAILURES_AND_LIMITS_EN.md)
- [Data Provenance](DATA_PROVENANCE.md)
- [Public Reproduction Guide](../PUBLIC_REPRODUCTION.md)
- [Glossary](GLOSSARY.md)
