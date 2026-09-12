# Data provenance and public coverage

## Two different public data surfaces

This repository contains a named legacy route-research surface and anonymous versioned test surfaces. They serve different purposes.

### Legacy route-research corpus

The broader public snapshot reports:

- 1,030 master subjects;
- 795 exact-like subjects;
- 761 subject-level discovery traces;
- 16 fixed public route-family or route-branch claims.

The 1,030-person master ledger spans several primary fields.

| Primary field | Master count | Public subject-trace count |
|---|---:|---:|
| Arts | 228 | 163 |
| Science, technology, and invention | 198 | 171 |
| Business and entrepreneurship | 135 | 111 |
| Sports | 129 | 113 |
| Religion and spirituality | 82 | 60 |
| Institutions and politics | 59 | 42 |
| Crime, controversy, and outlaws | 59 | 9 |
| Exploration and extreme achievement | 51 | 26 |
| Revolution, activism, and ideology | 45 | 27 |
| Humanities | 39 | 34 |
| Mixed public figures | 5 | 5 |

The named public trace includes internationally known figures such as Alan Turing, Angelina Jolie, Al Gore, Audrey Hepburn, Barack Obama, Bill Gates, Carl Sagan, and Bob Dylan. These examples show the range of the legacy material; they do not identify members of the anonymous v7 development420 release.

### Five-function development and stress-test surfaces

The five-function line uses release-specific anonymous data.

- v2 and v7 use the fixed 420-person development surface.
- v3 uses a separate 575-person person-out surface for one authored-production aggregate.
- v4 uses a 1,495-person frame and 1,457-person primary surface for one organized-realization family.
- v5 uses a separate 313-person legacy surface for one strict embodied-competition branch.
- v6 integrates the public results and corrected meaning-family projections without running a new inferential test.

The public releases deliberately prevent direct identity linkage for their anonymous rows. Counts across releases must not be summed as if they were unique people.

## Birth-data provenance

The legacy route research reuses exact chart facts and source-backed records from sources that include Astro-Databank, Astrotheme, birth or civil records cited by those sources, autobiographical or remembered times, and previously collected local research records.

The 761 public subject traces contain the following release precision labels:

| Public precision label | Count |
|---|---:|
| `A_exact` | 632 |
| `exact_fixed_offset_from_source_snippet` | 79 |
| `AA_external_screening` | 24 |
| `AA_external_screening_fixed_offset` | 18 |
| `AA_external_screening_LMT_fixed` | 7 |
| `AA_external_screening_pending_label` | 1 |

`Exact-like` is a repository grouping, not a statement that all records have identical documentary strength. Each person's source note and precision label must be considered when auditing a specific trace.

## Real-world activity provenance

The five functions use activity documented in fixed source material. The intended evidence unit separates:

- the actor;
- the action;
- the object or output;
- the carrier or social setting.

Supported, partial, contested, source-thin, and unknown states are preserved where the relevant release provides them. An activity not found in the fixed material is not automatically treated as absent from the person's whole life.

The public v7 matrix contains anonymous release IDs, observed functions, birth-era bands, collection-source groups, source-evidence regimes, development subcohorts, and fixed astrology-side surfaces. It does not contain names, full source text, birth dates, locations, or raw chart details.

## v7 public data files

### `development420_external_factor_matrix_v7.json.gz`

Contains 420 anonymous person rows. Important row fields include:

- `release_id`
- `analysis_order`
- `birth_decade`
- `birth_era`
- `collection_source_group`
- `development_subcohort`
- `field_state`
- `field_values_transport_only`
- `source_evidence_regime`
- `observed_functions`
- `surfaces`

Each function under `surfaces` contains Boolean exposure fields. `primary_western` and `primary_jyotish` represent the fixed primary definitions in each system. `pp_both_system` means **Primary-Western plus Primary-Jyotish**: both primary definitions are met. `any_tier_western` and `any_tier_jyotish` indicate at least one fixed tier in that system, while `any_tier_both_system` requires at least one fixed tier in each system. See [Astrological Structure Examples](ASTROLOGICAL_STRUCTURE_EXAMPLES.md) for concrete public candidate forms.

### `development420_observation_opportunity_v7.json.gz`

Contains observation-opportunity information for the same 420 release IDs, including source-depth bands or candidate-evidence sentence counts for the two development subcohorts.

### `development420_adversarial_decoy_memberships_v7.json.gz`

Contains 7,634 decoy rows and 708 unique exposure sets. These decoys are outcome-selected comparison challenges, not a random null distribution.

### `PUBLIC_PROJECTION_ATTESTATION_V7.json`

Records the privacy and projection assertions for the released v7 surface.

## Public coverage limitations

An audit of the 761-row named legacy trace found:

- 90 rows without a public biography URL;
- 42 rows without a public birth-source URL;
- 761 rows containing historical absolute `chart_fact_file` paths;
- 761 rows containing historical absolute `scoring_file` paths.

The absolute paths identify locations in the private build environment and are not resolvable public links. They should not be presented as public evidence access. They are preserved in the historical file, but a future cleaned projection should replace them with public artifact identifiers or an explicit `not_in_public_release` state.

Missing URLs do not by themselves prove that the underlying birth or activity record is invalid. They do mean that source coverage is incomplete from the perspective of an external reader. Any future claim about full source traceability must first resolve or categorize those rows.

## Relationship between named traces and anonymous analysis

The public materials do not persist an identity mapping from the anonymous v7 release IDs to real people. The 761 named legacy traces therefore cannot be used as a lookup table for development420.

This design protects the release boundary and avoids publishing a direct v7 membership map. It also limits independent auditing of how raw birth and biographical evidence became each anonymous v7 classification. That tradeoff must be stated explicitly rather than hidden behind the word reproducible.

## Third-party rights and privacy

The repository's Apache-2.0 license applies to the repository's code and original documentation. It does not relicense third-party biographical text, birth records, database entries, or linked source material.

Do not add private individuals, nonpublic birth information, copied copyrighted source text, or identity mappings to GitHub Issues. Use lawful public links and short factual descriptions when reporting a provenance problem.

## Relevant files

- [Public subject-level legacy trace](../supporting/subject_level_route_trace__mass_route_discovery_ledger_v1.json)
- [Legacy source-manifest example](../supporting/latest_source_manifest_example__mass_intake_source_backed_exact_round10_v1_source_manifest_v1.json)
- [v7 data directory](../independent_social_expression_v7/data/)
- [Reproducibility Boundary](REPRODUCIBILITY_BOUNDARY.md)
- [Study Map](STUDY_MAP.md)
