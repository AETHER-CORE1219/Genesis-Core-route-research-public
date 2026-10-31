# Research Update (November 1, 2026): Representation Repair, Selection Dynamics, and Replicable Evaluation

English | [日本語](README_JA.md) | [Reproduction](REPRODUCTION.md)

## 1. Central Inquiry, Convergence Structures, and Population Layers

This project investigates an empirical question regarding classical astrological traditions:  
**Do astrological chart structures correspond to human social activities in measurable, repeatable ways that cannot be fully accounted for by chance, conventional occupational titles, biographical document volume, or historical era?**

This research investigates an empirical structural correspondence: whether multiple, distinct astrological realization conditions systematically converge onto the same overarching social activity functions. Drawing on biographical records of figures with documented birth times (though documentation standards historically vary), tangible life activities and concrete accomplishments were organized across multiple domains without inspecting natal charts. Western and Jyotish traditions were constructed as separate, parallel symbolic systems to examine how multi-condition rules—combining traditional role actors, connected capabilities, semantic relations, and realization conditions—correspond to documented societal outputs.

The research organizes its empirical material across distinct population layers that fulfill different methodological roles and must not be aggregated:
- **1,030 upstream collection records**;
- **793 deduplicated historical individuals** (derived from 795 exact-like records, accounting for two recognized alias records);
- **731 individuals in the blind activity-inventory development surface**; and
- **420 individuals in the common quantitative development cohort** (comprising a 311-figure pipeline cohort with detailed citations and a 109-figure pipeline cohort originally cataloged via summary anchors, whose full biographical texts have now been systematically reconnected).

Across 11 functional domains of social activity, five primary candidate pathways were identified as focal structural groupings: *Public Advocacy*, *Authored and Symbolic Production*, *Organized Collective Realization*, *Technical and Product Implementation*, and *Embodied Performance* (encompassing experimental piloting, spaceflight, physical navigation, and competitive athletics, rather than sports alone). A single individual frequently exhibits activities across several pathways, and multiple distinct astrological realization conditions connect to the same functional domain.

In the historical v7 release, adjusted rate differences between +27.95 and +39.08 percentage points across the five functions were reported within the 420-person development cohort. Earlier in the research trajectory (v3–v5), three restricted tests on individuals outside the development cohort across specific branches yielded zero positive confirmations. These earlier finite negative outcomes do not constitute a blanket refutation of all pathways or classical astrology, nor does the project currently claim out-of-cohort validation, established causality, or individual predictive power.

---

## 2. Preserving Symbolic Meaning and Disambiguating Graph Topologies

In this research update, rigorous verification required examining whether the symbolic meaning structures captured in the original research were faithfully preserved as the computational representation was refactored. As an empirical baseline for this evaluation, the response matrix of the original AIT graph and its 741 mined rules was first fully reproduced across all 420 individuals.

Evaluating the transition from the published AIZ representation to the portable AJY graph across the 515 rules associated with the five primary functions revealed representational divergences in 416 of 420 individuals, while subsequent birth-data input corrections introduced changes in 55 of 420 individuals (417 and 56 individuals, respectively, across all 741 rules).

In the embodied performance pathway, the number of individuals meeting joint dual-system criteria shifted across historical saved builds from 25 to 1 to 0 to 0 (progressing through the original AIT, role-corrected AJH, yoga-comprehensive AJY, and input-corrected AJY). This shift was driven by structural disambiguation rather than birth data corrections alone:
1. **Evidence from Placeholder Records**: In a separate diagnostic removing relational links where the witness evidence was solely the placeholder string `__MISSING__`, joint matches shifted from 25 to 12. This was an isolated diagnostic test on AIT copies, not an intermediate chronological version.
2. **Graph Topology Disambiguation**: The original model collapsed incoming dispositor chains, outgoing chains, self-terminal states, and relational witnesses into a single unranked field. Subsequent models separated role actors, directed ordered chains, self-terminal placements, and complete co-participating planets in yoga configurations. Translating source namespace and topology keys in the original-input AJY graph restored 313 person-rule links (309 in the input-corrected AJY graph), but yielded only a 0 to 1 shift in embodied performance.

Re-generating the AJY graphs from corrected inputs produced an exact context match with historical archives. The repaired representation explicitly preserves 881 incoming dispositor paths, outgoing dispositor paths, 62 self-terminal placements, and 226 cyclic dependencies as distinct typed structures. Across the 311,220 cells of the 741 rules × 420 individuals matrix, historical matches were partitioned into exact matches (2,952 out of 8,076 original hits), explicit namespace translations (145 hits), and known discrepancies or unresolved predicates. Unresolved predicates are preserved as unresolved rather than cast to false. While 158 rules maintained invariant non-empty person sets across all four historical graph revisions, this demonstrates representational invariance under refactoring, not independent empirical confirmation.

---

## 3. Selection Dynamics and Training-Only Selection with Held-Out Evaluation

To evaluate selection bias in historical workflows, the finite rule selection pipeline (AIU → AIV → AIX → AIY) was reconstructed from bitmasks, reproducing 786 rule leads, 741 selected rules, and all adopted branches. Across 999 permutations exchanging 11-function activity profiles within the 311 and 109 biographical pipeline clusters, the selection algorithm selected a median of 782 rules (range: 690–870) compared to 741 in the empirical data. Single-facet one-sided reference permutation p-values across the five primary pathways were .605, .115, .920, .598, and .429. Across all 66 evaluated facets, the maximum standardized difference yielded a reference p-value of .958, while the maximum unstandardized risk difference showed p = .034 (observed in a small facet with only four individuals exposed to a belief-related function, all four of whom held recorded activities). Both metrics are retained as descriptive baselines.

Next, a separate, finite set of queries derived from the repaired typed representations (incorporating directed paths, incoming influences, and actor capabilities) was evaluated under a strict 5-fold cross-validation scheme. In this protocol, candidate generation and candidate selection were strictly confined to training folds, while the selected queries and dual-system aggregation were evaluated on the held-out folds. Verification tests confirmed that reversing activity labels on the held-out folds did not alter candidate selection within the training folds, and that no candidates exclusive to the test set entered the query pool. Because the historical grammar and vocabulary were informed by observations across the 420 individuals, this setup constitutes an internal evaluation of selection dynamics rather than an out-of-cohort confirmation on unseen individuals.

In this evaluation, two recording endpoints were analyzed on the activity side. The first endpoint is the baseline presence of any recorded activity in the ledger, while the second requires that both the component and the function edge were recorded as `SUPPORTED` in historical records. The latter serves as a sensitivity analysis to assess the impact of stricter evidentiary thresholds, rather than defining a new ground-truth dataset. Under either endpoint, the absence of a record does not denote actual negative non-occurrence in an individual's lifetime.

Across 132 evaluation surfaces (11 functions × 6 graph surfaces × 2 recording endpoints) and 199 permutation runs re-running the selection mechanism, the maximum standardized difference across all surfaces yielded a reference p-value of .785, remaining within the expected null distribution.

---

## 4. Local Imbalances and Combinatorial Sparsity

While the family-wise standardized evaluation did not reject the global null, distinct local imbalances were observed within the held-out evaluation folds:
- **Embodied Performance (Jyotish-any)**: Recorded in 13 of 37 held-out individuals, representing an unadjusted rate difference of +15.29 percentage points (single-facet reference p = .025; corrected p = .785 across all 132 surfaces).
- **Organized Collective Realization (Dual-System, Legacy Both-Supported Endpoint)**: Recorded in 8 of 9 held-out individuals, representing an unadjusted rate difference of +33.90 percentage points (single-facet reference p = .010; corrected p = .860 across all 132 surfaces).
- **Embodied Performance and Technical Implementation (Dual-System Primary Facets)**: Produced zero held-out exposed individuals.

These local imbalances are empirical observations resulting from this specific finite query construction and training-only selection procedure. They are not claimed as confirmed universal laws, nor are they promoted as post-hoc proofs. Conversely, zero exposed individuals in dual-system primary facets reflects the combinatorial sparsity that arises when multiple multi-condition requirements are conjoined within a finite cohort, rather than empirical disproof of the traditional concepts themselves.

---

## 5. Activity Grounding, Document Volume, and Evidentiary Axes

On the empirical measurement side, 4,306 citation references spanning 1,594 component-function links were verified against archival hashes. For the 109-figure pipeline cohort, 3,002,408 characters of biographical text were reconnected from summary anchors to the full preserved text corpus and verified against adopted hashes.

A focused review was conducted on 50 links where component-level status diverged from function-edge status. Of these, 48 links had entered historical analysis as OUTPUT edges, and 2 were non-output overlays. Grounding these 50 links in the restored textual context yielded the following resolution:
- **28 links** directly supported documented, attributable personal actions;
- **12 links** exhibited persistent ambiguity at the boundary of the social function definition;
- **7 links** verified formal appointments or titles where the scope of tangible operational activity remained unclarified in the citation;
- **1 link** involved contested personal attribution; and
- **2 links** were non-output overlay elements.

Evidence-backed documentation was completed for all 50 discrepancies, while explicitly preserving remaining unclarified boundaries rather than treating them as fully resolved. Frozen analysis labels were not altered post-hoc based on review outcomes, and a complete independent human re-adjudication across all 1,594 links was not conducted. This review highlighted that legacy `PARTIAL` ratings frequently conflated limited duration or secondary vocational focus with evidentiary insufficiency. In the updated framework, personal agency, functional semantic fit, evidentiary sufficiency, substantive prominence, and historical duration are tracked as distinct axes.

Across the 410 individuals with full biographical text corpora, the Spearman's rank correlation $\rho$ between biographical character volume and the number of recorded activity functions was .267 ($\rho = .192$ within the 301-figure subset; $\rho = .303$ within the 109 cohort). In contrast, character volume showed rank correlations of $\rho = -.064$ with graph relationship counts and $\rho = -.018$ with graph path counts, while relationship counts and recorded activity functions yielded $\rho = -.082$. These figures document descriptive correlations within this dataset and do not demonstrate statistical independence or the complete absence of confounding. The remaining 10 individuals from the 311 cohort not included in the text-volume input have verified exact biographical spans preserved from prior repair work.

---

## 6. Open Artifacts and Standalone Reproduction

Historical releases v1–v7 remain available on GitHub (`AETHER-CORE1219/Genesis-Core-route-research-public`). The repository now includes the `research_update_20261101/` directory containing:
- Complete English and Japanese methodology documentation (`README.md` and `README_JA.md`);
- `data/historical_selection_input.json.gz` and `data/repaired_chain_input.json.gz`: Incidence matrices, activity profiles, and cluster/fold metadata omitting personal names, birth timestamps, geographic coordinates, and internal identification mappings (using opaque numeric identifiers);
- `scripts/reproduce.py`: A self-contained script using only the Python standard library, replaying historical 741-rule selection across 999 permutations, training-only selection across 5 folds, and 199 selection-inclusive permutation runs;
- `EXPECTED_REPLAY_RESULTS.json`, semantic/measurement aggregations, and checksums.

Researchers can execute the full reproduction pipeline locally from the repository root:
```bash
python research_update_20261101/scripts/reproduce.py
```
No third-party packages are required. This script allows users to independently run and inspect the mechanical rule selection algorithms, permutation baselines, and cross-validation procedures from pre-extracted incidence data. This replay of finite selection mechanisms is distinct from regenerating full astronomical charts and blind biographical codings from raw historical records.

By disambiguating graph topologies into typed structures and confining candidate selection strictly to training folds, this update establishes an explicit baseline for investigating how multi-condition astrological concepts behave under transparent computational evaluation.
