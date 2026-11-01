# Research Q&A: Empirical Inquiries, Evidence Layers, and Open Boundaries

English | [日本語](RESEARCH_QA_JA.md)

**Published:** November 1, 2026  
**Associated Repository:** `AETHER-CORE1219/Genesis-Core-route-research-public`  
**Evidence Dataset:** [`docs/RESEARCH_QA_EVIDENCE_20261101.json`](./RESEARCH_QA_EVIDENCE_20261101.json)  

---

### Q1: What is the core question and primary discovery of this research? Is it a test of predictive astrology?
**Answer:** No. It is not a test of predictive astrology, nor an attempt to classify individuals into single occupational boxes. The research investigates a specific structural question:  
*Do astrological chart configurations correspond to tangible human social activities in repeatable, testable ways that cannot be explained away by chance, occupational stereotypes, document volume, or historical era?*

The central finding during the discovery and model-building phases was a **convergence structure**: rather than assuming an oversimplified one-to-one link between a single sign and a career, multiple distinct astrological realization conditions (spanning role actors, capabilities, semantic relations, and configurations) were observed to converge onto shared, overarching social functions. Objective achievements of public figures across eras and fields were cataloged without inspecting birth charts, and parallel Western and Jyotish symbolic frameworks were examined against these records. This convergence pattern is an empirical observation from the development cohort, not an established universal law of nature. The goal is to determine whether the population-level relationship is strictly zero, or whether a finite, robust correspondence exists.

---

### Q2: Famous figures are versatile and have long biographies. Doesn't that explain away the observed differences?
**Answer:** In the specific control models evaluated, the rate differences do not disappear, indicating that dismissing the findings as mere biographical length is insufficient. However, this does not prove complete statistical independence or the absence of all confounding.

1. **Descriptive Rank Correlations:** Across 410 individuals with full biographical text corpora, the rank correlation between biographical character volume and chart relationship counts is Spearman's $\rho = -0.064$, and with path counts is $\rho = -0.018$. These small marginal correlations describe the sample but do not constitute proof of independence.
2. **Differences After Specified Additional Adjustments:** Character volume shows a weak-to-moderate rank correlation with the count of recorded activity functions ($\rho = 0.267$ across the cohort; $\rho = 0.192$ within the 301-figure subset; $\rho = 0.303$ within the 109 cohort). To test this directly, an additional regression model controlled for character volume, continuous birth year, spherical geographic coordinates ($x, y, z$), collection source, and measurement pipeline. The differences across four primary functions shifted as follows:
   - **Public Advocacy:** 14.29 percentage points (unadjusted) $\rightarrow$ 12.38 percentage points (specified additional adjustment)
   - **Authored & Symbolic Production:** 26.15 percentage points $\rightarrow$ 23.67 percentage points
   - **Organized Collective Realization:** 25.83 percentage points $\rightarrow$ 27.33 percentage points
   - **Technical & Product Implementation:** 29.55 percentage points $\rightarrow$ 19.49 percentage points

These regression estimates are descriptive models evaluated on fixed selections, not exploration-corrected proofs of significance. They show that the observed differences do not simply vanish under these controls, though they do not control for all cultural, geographic, or unmeasured facets of versatility.

---

### Q3: Why are there different sample counts (1,030, 793, 731, and 420)? Are cohorts being aggregated to inflate numbers?
**Answer:** No. These figures represent distinct methodological layers and must not be added together:
- **1,030:** Total upstream legacy master records collected.
- **795 / 793:** 795 exact-like records yielding 793 unique historical persons after resolving two recognized aliases.
- **731:** The historical discovery and blind activity-inventory development surface.
- **420:** The common quantitative development cohort used for internal comparative analysis, consisting of 311 figures from a detailed citation pipeline and 109 figures whose previously preserved full text was systematically reconnected to summary anchors.
- **761:** Publicly named legacy trace records.

The latest internal comparative analyses discussed in this Q&A (such as cross-validation and adjustment models) are conducted strictly within the 420-person development cohort.

---

### Q4: With 136 groups across 420 people, isn't overfitting and capturing noise inevitable?
**Answer:** The criticism that 136 groups represents 136 free regression coefficients is mathematically incorrect, but the concern regarding overfitting during exploration is entirely valid and requires direct empirical measurement.

The 136 groupings represent a semantic hierarchy of rule families, not unconstrained model parameters. However, demonstrating that 136 groups is not a parameter count does not dismiss the risk of overfitting. In a rule-mining framework, mining extensive rule spaces can capture noise. In permutation baselines exchanging 11-function activity profiles across individuals within clusters over 999 runs, the selection algorithm selected a median of 782 rules (range: 690–870) compared to 741 empirical rules. That count comparison is a diagnostic baseline, not evidence of validity. Evaluating the true impact of candidate selection requires embedding the selection process itself inside cross-validation, the results of which are detailed in Q8.

---

### Q5: What is the relationship between earlier non-positive out-of-cohort tests (v3–v5) and the large differences reported in v7 (+28 to +39 percentage points)?
**Answer:** Earlier in the research history (v3–v5), prior to the v7 release, three restricted tests conducted on individuals outside the development cohort across specific branches yielded zero positive confirmations. These earlier tests and the subsequent v7 cohort observations represent different empirical stages and narrow definitions.

In the historical v7 release, adjusted rate differences between +27.95 and +39.08 percentage points across the five primary functions were reported within the 420-person development cohort (and remain reproducible from archived matrices). The earlier non-positive tests cautioned against treating these branches as confirmed universal laws, but because they tested narrow definitions on restricted subsets, they did not mathematically invalidate the entire multi-condition inquiry. Both the positive cohort differences and the earlier negative checks are recorded as empirical data points, neither establishing universal confirmation nor constituting a blanket refutation.

---

### Q6: Why did match counts for Embodied Performance collapse from 25 to 1 to 0 across graph revisions? Was data manipulated?
**Answer:** No. The collapse was not caused by data suppression, but by a combination of removing ungrounded placeholder evidence and the unintended loss of semantic connections during representation changes.

Across historical saved versions (original AIT, role-corrected AJH, yoga-comprehensive AJY, and input-corrected AJY), the number of individuals meeting joint dual-system criteria for Embodied Performance shifted: 25 $\rightarrow$ 1 $\rightarrow$ 0 $\rightarrow$ 0.
1. **Placeholder Relations:** In a counterfactual diagnostic on an AIT copy, removing relations where the witness evidence was solely the string `__MISSING__` shifted matches from 25 to 12.
2. **Representation Disambiguation and Meaning Recovery:** Disambiguating directed ordered chains and requiring complete participant planets in yoga configurations caused match counts to fall prior to input corrections. However, recent recovery of mutual aspects and full connection sets from original generation logic separated 3,792 previously unresolved cells across 83 rules into 165 condition matches (distributed across 105 individuals and 35 rules) and 3,627 non-matches. Similarly, tracking 1,262 Western dispositor links confirmed that 823 retained concrete paths under corrected inputs (576 of which had been unmapped in intermediate states).

When evaluating the repaired grammar across all 420 individuals, an any-tier dual-system rule aggregation surface identified 21 matching individuals (13 recorded, a difference of +42.86 percentage points). However, under a 5-fold cross-validation scheme that isolates individuals from candidate selection, this surface yielded only 4 matching individuals and 0 recorded activities. The correspondence was reconstructed within the development sample under repaired grammars, but transferring this to held-out partitions under selection cross-validation has not been achieved.

---

### Q7: Were the 50 two-layer status discrepancies resolved arbitrarily to favor astrological claims?
**Answer:** No. Historical frozen analysis labels were preserved, while an updated, alternative measurement ledger was generated incorporating verified evidence for 28 links. No claims are made that all 1,594 links have undergone independent human re-adjudication.

Among the 50 discrepancies between component-level facts and function-edge status (48 of which entered legacy analysis as `OUTPUT` edges, and 2 were non-output overlays):
- **28 links** were verified as directly supporting documented, attributable personal actions;
- **12 links** exhibited persistent ambiguity regarding whether the action fit the specific social function definition;
- **7 links** confirmed formal titles or offices where tangible day-to-day operational scope was missing from the citation;
- **1 link** involved disputed historical attribution; and
- **2 links** were non-output overlay elements.

Updating the 28 verifiable links in the alternative measurement version brought the ledger to 1,457 supported links and 137 uncertain links across 1,594 component-function links (and 4,306 citation hashes). This review confirmed that legacy `PARTIAL` ratings frequently conflated brief duration or secondary vocation with evidentiary weakness. Unrecorded activity is strictly classified as unrecorded, not as life-wide negative proof.

---

### Q8: What did the latest 5-fold cross-validation and 999-run permutation tests show? Is the effect globally significant?
**Answer:** In this family-wise comparison across 132 surfaces, the test did not achieve positive confirmation exceeding the permutation control baseline, though specific local imbalances remain under observation.

Under a protocol confining candidate and branch selection to training folds across 132 evaluation surfaces (11 functions × 6 graph surfaces × 2 recording endpoints):
- **Permutation Baselines:** In 999-run permutations swapping profiles within source clusters, the maximum standardized difference yielded a reference p-value of **p = .260** (source-only) and **p = .298** (source × era × document volume). Maximum unstandardized risk differences yielded reference p-values of **p = .633** and **p = .690**. Global statistical significance was not confirmed.
- **Local Observation:** Within the held-out test evaluations, *Transmission of Belief & Thought Systems* (Jyotish primary surface) was recorded in 6 of 18 exposed individuals (compared to 38 of 402 non-exposed, an unadjusted difference of +23.88 percentage points). The local single-facet reference p-value was **p = .008 / .015**, while the family-wise corrected p-value was **p = .260 / .298**. In all 6 individuals, 10th-lord Jupiter (knowledge, judgment, and institutional legitimacy) and active configuration membership were shared.

This local imbalance remains an observation within internal cross-validation and is not promoted as an independent confirmation.

---

### Q9: How do the morning research update and the latest evening calculations differ?
**Answer:** They evaluate different representations and testing targets within the reconstruction pipeline and should not be treated as a single uniform result:
- **Morning Release (`research_update_20261101`):** Established a standalone reproduction pipeline replaying historical 741-rule selection (999 permutations) and in-fold evaluation across an earlier repaired query representation (199 permutations, yielding maximum standardized difference p = .785).
- **Latest Evening Calculations:** Restored the original AISR granularity contract (treating specific Yoga names as modifiers rather than branching IDs, preserving 53,648 branch evidences without fragmenting shared IDs), resolved 3,792 previously unmapped cells (identifying 165 condition matches), tracked 1,262 Western dispositor links (retaining 823 exact paths under corrected inputs), and executed the full 999-iteration two-tier permutation test across 132 surfaces.

Restoring the original contract structural units does not constitute a full recovery of all original 741 rule meanings, but rather tests a disambiguated representation against a rigorous permutation baseline.

---

### Q10: What can an independent reader reproduce right now, and what remains to be done?
**Answer:** Readers can independently verify the mechanical rule selection algorithms, permutation baselines, and cross-validation mechanics using the public repository, while the raw birth data and identity mapping tables for the 420-person development cohort are withheld.

- **Reproducible Now:** Running `python research_update_20261101/scripts/reproduce.py` from the root of `AETHER-CORE1219/Genesis-Core-route-research-public` re-executes rule selection and permutation baselines using standard Python without external dependencies. While the repository contains 761 publicly named legacy trace records, the raw birth timestamps, locations, and personal identity mapping tables for the 420 development individuals are withheld from public datasets.
- **Status of Latest Evening Data:** The latest evening multi-factor controls and full 999-run cross-validation suite are documented as aggregate data in [`docs/RESEARCH_QA_EVIDENCE_20261101.json`](./RESEARCH_QA_EVIDENCE_20261101.json). They are published here as numerical evidence, not as an immediate executable reproduction script.
- **Future Challenges:** The primary tasks ahead are independent verification of activity coding, methodological handling of unrecorded activity, and testing whether fixed candidate structures generalize out-of-cohort.

---

### Q11: If even a single robust correspondence exists, wouldn't that be profoundly important? Why evaluate the entire system so critically?
**Answer:** That intuition is central to this research. The project does not assume that all five pathways must succeed simultaneously for a finding to have scientific value; establishing even a single non-trivial, repeatable correspondence between chart structures and human activity would be a profound result.

However, observing a non-zero rate difference in a finite sample is not equivalent to establishing a true correspondence. When complex rule spaces are searched, random variance naturally yields local separations; distinguishing genuine signals from search artifacts requires testing those separations against control baselines that undergo the identical candidate-selection process.

Conversely, failing to achieve statistical significance across an entire family of surfaces (as reflected in the reference p-values in Q8) does not mathematically prove that the underlying correspondence in nature is strictly zero. The hypothesis of a true null effect must not be conflated with the observation that an empirical pipeline did not exceed its permutation controls. The project maintains focus on specific surviving local imbalances—such as the Jyotish 10th-lord Jupiter configuration in Transmission of Belief & Thought Systems (Q8)—not as premature proofs, but as concrete, falsifiable hypotheses to be carried into future independent evaluations. Taking this inquiry seriously demands resisting both premature celebration of noisy positives and premature dismissal based on exploratory hurdles.
