# v7 public data dictionary

## Shared identifiers

**`release_id`**

Opaque identifier used to join the released v7 projections. It is not a real-world identity and no identity mapping is persisted in the public release.

**`analysis_order`**

Opaque deterministic order used to reproduce random assignments. It is not an identity key.

## External-factor matrix

File: `data/development420_external_factor_matrix_v7.json.gz`

### Top-level fields

| Field | Meaning |
|---|---|
| `schema_id` | Versioned schema identifier |
| `person_count` | Number of anonymous person rows; expected 420 |
| `declared_surface_count` | Fixed surface family size; expected 22 |
| `estimable_surface_count` | Surfaces with estimable exposure variation; expected 18 |
| `structural_zero_surface_count` | Fixed surfaces preserved without an estimate; expected 4 |
| `release_id_mapping_persisted` | Whether an identity map exists in the release; expected false |
| `identity_source_text_birth_date_or_chart_included` | Whether prohibited identifying/source/chart material is included; expected false |
| `rows` | Anonymous person-level records |

### Person-row fields

| Field | Meaning |
|---|---|
| `birth_decade` | Coarse decade used for continuous-era sensitivity checks |
| `birth_era` | Fixed five-level birth-era category |
| `collection_source_group` | Fixed six-level collection-source category |
| `development_subcohort` | Internal 311- or 109-person development partition |
| `source_evidence_regime` | Fixed reality-side measurement regime |
| `field_state` | Whether field information is available on the selected descriptive surface |
| `field_values_transport_only` | Field values retained for descriptive transport analysis, not entry labels |
| `observed_functions` | Non-exclusive functions supported by fixed source material |
| `surfaces` | Function-by-exposure Boolean matrix |

### Surface fields

| Field | Meaning |
|---|---|
| `primary_western` | Membership in the primary Western exposure |
| `primary_jyotish` | Membership in the primary Jyotish exposure |
| `pp_both_system` | Intersection of the two primary system exposures |
| `any_tier_western` | Membership in any fixed Western tier for the surface |
| `any_tier_jyotish` | Membership in any fixed Jyotish tier for the surface |
| `any_tier_both_system` | Both-system intersection using any fixed tier |

## Observation-opportunity file

File: `data/development420_observation_opportunity_v7.json.gz`

| Field | Meaning |
|---|---|
| `opportunity_type` | Which observation-opportunity measure applies to the row |
| `source_depth_band` | Five-level source-depth band for the 311-person subcohort |
| `candidate_evidence_sentence_count` | Evidence-sentence count used with `log1p` in the 109-person subcohort |

## Adversarial-decoy file

File: `data/development420_adversarial_decoy_memberships_v7.json.gz`

| Field | Meaning |
|---|---|
| `row_count` | Number of predicate-level decoy rows; expected 7,634 |
| `unique_exposure_set_count` | Number of unique exposure sets; expected 708 |
| `exposure_set_id` | Opaque identifier for one unique released exposure membership set |
| `release_ids` | Anonymous people belonging to that exposure set |

The decoys are outcome-selected comparison challenges and must not be treated as a random null distribution.

## Canonical result files

**`RESULTS.json`** contains the stored models, secondary checks, simultaneous results, decoy comparisons, ablations, sensitivity quantities, and terminal interpretation.

**`CLAIM_BOUNDARY.json`** is the authoritative machine-readable list of supported and unsupported interpretations.

**`PUBLIC_PROJECTION_ATTESTATION_V7.json`** records the public privacy and projection assertions used by the validator.
