# Methods

## Analysis population and outcomes

- Unit of analysis: one person.
- Population: fixed `development420`, with no duplicate person rows.
- Outcomes: public advocacy, authored or symbolic production, organized collective realization, technology or product implementation, and embodied competitive performance.
- The five functions are non-exclusive. One person may support several outcomes.
- Outcomes describe actions documented in the fixed source material. Non-observation in that material is not interpreted as absence from the person's whole life.

Field and occupation are treated only as manifestation, covariate, moderator, or transport variables. They are not used as labels that define entry into a social function.

## Astrology-side surfaces

Each social function has predefined Western, Jyotish, and both-system exposure surfaces.

- The primary exposure for the first four functions is `pp_both_system`, meaning **Primary-Western plus Primary-Jyotish**: the person meets both fixed primary system definitions.
- The strict primary-plus-primary intersection was structurally zero for embodied competition. Before the v7 result was inspected, the declared primary surface for that function was therefore fixed as `any_tier_both_system`, meaning that at least one fixed exposure tier is met in each system.
- The selection family contains 11 functions multiplied by two both-system surfaces, for 22 fixed surfaces.
- Eighteen surfaces are estimable. Four remain structural-zero surfaces and are preserved without an estimate.

Western and Jyotish are not counted as two votes. A both-system surface represents a defined intersection of separately structured chart classifications.

Concrete public examples of the underlying MC-ruler, A10-lord, Amatya, relation, house, and varga structures are provided in [Astrological Structure Examples](../docs/ASTROLOGICAL_STRUCTURE_EXAMPLES.md).

## Sequential external-factor model

For person `i`:

- `Y_i` indicates support for a documented social function in the fixed reality-side material.
- `E_i` indicates membership in the fixed chart-structure exposure for the surface.

A linear probability model reports the coefficient of `E_i` as a risk difference. HC3 standard errors are used.

```text
M0: Y ~ 1 + E
M1: M0 + birth era
M2: M1 + measurement regime
M3: M2 + collection source
```

The factors contain five birth-era levels, three reality-measurement regimes, and six collection-source groups. The analysis adds them sequentially so that changes associated with each factor remain visible rather than reporting only one fully adjusted model.

## Factor-specific secondary checks

### Birth era

- raw differences within each estimable era level;
- 9,999 exposure-label permutations within era;
- an adjusted model containing continuous birth decade and its quadratic term.

### Reality-measurement regime

Direction is inspected separately in the two main regimes. A 17-person repair surface is retained as a descriptive stratum and is not assigned a standalone p-value.

### Collection source

- differences within source group;
- M3 estimates after leaving out one source group at a time;
- 9,999 permutations within source group.

### Observation opportunity

The 311-person development subcohort uses a fixed five-level source-depth measure. The 109-person subcohort uses the log-transformed count of candidate evidence sentences. Adjustment is performed separately within the two subcohorts.

### Field

Field values are observed for only 84 people in a selected descriptive surface. They are not used for candidate selection or the primary analysis.

## Simultaneous fixed-family test

For each of the 18 estimable surfaces, the procedure constructs the M3 null-score HC3 influence contribution.

Each of 9,999 draws assigns one Rademacher sign to a person and shares that sign across all 11 function outcomes for that person. The maximum t statistic across the 18 estimable surfaces is retained for each draw.

This person-package maxT procedure addresses:

- multiplicity within the fixed 22-surface family; and
- correlation among several functions observed for the same person.

The simultaneous one-sided 95% lower bound and adjusted p-value are reported for each primary surface.

## Adversarial-decoy comparison

The release reconstructs 7,634 weak or reverse-direction predicate rows representing 708 unique exposure sets. The same M3 analysis is applied.

These decoys were selected using outcome information. They are therefore not treated as a random null distribution. The comparison is limited to a necessary specificity challenge: a primary candidate must exceed the 95th percentile of both the predicate-weighted and unique-exposure decoy distributions.

## Western/Jyotish ablation

Each primary surface is compared descriptively in three forms:

- full both-system exposure;
- Western-only exposure;
- Jyotish-only exposure.

A full estimate larger than both single-system estimates is descriptive specificity, not a formal interaction test. If one single-system estimate is larger than the full estimate, the release describes that system as a single-system carrier rather than claiming synergy.

## Sensitivity to unmeasured confounding

The analysis reports the product of hypothetical exposure imbalance and outcome difference required to move either the point estimate or simultaneous lower bound to zero.

This is a sensitivity quantity. It is not proof that unmeasured confounding has been removed.

## Frozen decisions

- No new people, sources, charts, routes, or held-out outcomes were accessed for v7.
- No candidate or threshold was changed after the v7 result.
- Version 7 tests robustness of the fixed development associations; it is not a rescue analysis on the v3–v5 person-out surfaces.

See [CLAIM_BOUNDARY.json](CLAIM_BOUNDARY.json) for the machine-readable supported and unsupported claims.
