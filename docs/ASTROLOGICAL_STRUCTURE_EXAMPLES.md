# What the astrological structures look like

## Why this page exists

The v7 anonymous matrix stores fixed exposures as Boolean values so that the public statistical analysis can be recalculated without publishing an identity map. A Boolean such as `pp_both_system` is the endpoint of an astrological classification, not the astrological technique itself.

This page gives concrete examples from the public rule registries and versioned tests. They show the form of the candidate structures. They are not all validated routes, and the examples must not be treated as a definition of every v7 exposure.

## The role-based structure

The research does not search only for a planet in a sign. A candidate can combine:

1. a **system** — Western or Jyotish;
2. a **functional role** — for example, the Western MC ruler or Jyotish A10 lord;
3. an **actor-capability family** — the type of capacity represented by the role;
4. a **connected-capability family** — another capacity connected to the actor;
5. a **relation mode** — for example, dispositorship, lordship, or another directed relation;
6. a **carrier** — the house, varga, angular, or other structure through which the relation is expressed;
7. a **social-output function** — the documented activity being tested.

This hierarchy is intended to prevent a familiar occupational label from defining the astrological result after the fact.

## Public Western example

One public v2 development rule for authored or symbolic production uses:

- system: `WESTERN`;
- functional role: `MC_RULER`;
- role meaning: public direction and social-projection mediator;
- actor-capability family: initiation, conflict, and embodied execution;
- connected-capability family: authorization, centrality, and visible identity;
- relation family: dependency, governance, or mediated delivery;
- topology: traditional dispositor chain;
- carrier: a Western position in an angular, public-vocational, artha-output, or upachaya house class.

The public rule status is `FROZEN_TRAINING_RULE_AWAITING_FIXED_APPLICATION_NOT_VALIDATED_ROUTE`. It is a development hypothesis, not an externally confirmed rule.

## Public Jyotish example

Another public v2 authored-production rule uses:

- system: `JYOTISH`;
- functional role: `A10_LORD`;
- role meaning: visible status and public-image carrier;
- actor-capability family: mediation, analysis, language, and exchange;
- connected-capability family: separation, abstraction, and dematerialization;
- relation family: dependency, governance, or mediated delivery;
- topology: `sambandha`;
- relation mode: dispositor or lordship;
- carrier: D10 confirmation in a kendra or angular class.

This rule has the same development-only status. The repository exposes the structure so that a reader can see that `primary_jyotish` is not a Sun-sign label or an arbitrary number.

## Two candidate families tested on separate people

### v4: Mars–Mercury organized realization

Version 4 tested one frozen Jyotish Mars–Mercury two-branch family for documented organized collective realization. The two branches shared a Mars–Mercury capability pair but differed in role, direction, meaning core, and carrier.

The result did not meet the positive-confirmation rule, and the predeclared development-sized effect was not reproduced. This is a concrete example of a recognizable astrological candidate being tested rather than accepted because its symbolism appears persuasive.

### v5: Saturn-to-Jupiter embodied competition

Version 5 tested a strict Jyotish candidate linking:

- an Amatya Saturn-like duty and persistence actor;
- a directed dependency on Jupiter-like judgment and legitimation;
- a Dusthana carrier;
- documented embodied competitive performance.

The strict chain was non-positive on its separate-person surface. Removing only the Dusthana carrier returned a small positive but unconfirmed direction. This shows why adding more astrological conditions does not automatically improve a rule.

## Person-level examples explain multiple functions, not proof

The v6 public examples show why one occupational title is insufficient.

- Francesco Totti combines elite football, UNICEF and charity activity, and authored charity books or comic appearances.
- Jawaharlal Nehru combines anti-colonial mobilization, books and political philosophy, institutional coordination, and formal office.
- Charles E. Leiserson combines theory and algorithms, working technical architecture, and laboratory direction.
- Nancy Kerrigan combines measured competition, public-cause activity, and performed ice shows.

These are development interpretations. They demonstrate multi-function outcome design; they are not independent confirmations of the chart rules.

## How the Boolean v7 fields should be read

- `primary_western`: the person meets the fixed primary Western definition for that surface.
- `primary_jyotish`: the person meets the fixed primary Jyotish definition for that surface.
- `pp_both_system`: **Primary-Western plus Primary-Jyotish**; both primary definitions are met.
- `any_tier_western`: at least one fixed Western tier is met.
- `any_tier_jyotish`: at least one fixed Jyotish tier is met.
- `any_tier_both_system`: at least one fixed tier is met in each system.

The fields do not mean that Western and Jyotish are counted as two votes. They encode predefined intersections.

## What remains unavailable

The public v7 matrix does not expose every rule-to-person membership or the complete source-to-chart-to-rule pipeline. The public v2 registry exposes 515 development rules in abstracted structural form, while v4 and v5 expose particular test candidates. A complete end-to-end audit of every v7 Boolean classification is not possible from the current public files.

See [Reproducibility Boundary](REPRODUCIBILITY_BOUNDARY.md) and [v7 Data Dictionary](../independent_social_expression_v7/DATA_DICTIONARY_EN.md).

## Public source files

- [v2 five-candidate rule registry](../independent_social_expression_v2/data/five_candidate_rule_registry_v2.json)
- [v4 English overview](../independent_social_expression_v4/README.md)
- [v5 English overview](../independent_social_expression_v5/README.md)
- [v6 person-trace examples](../independent_social_expression_v6/PERSON_TRACE_EXAMPLES.md)
- [v7 public data dictionary](../independent_social_expression_v7/DATA_DICTIONARY_EN.md)
