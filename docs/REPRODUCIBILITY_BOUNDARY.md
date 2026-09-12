# Reproducibility boundary

## Three different claims

The word reproducible can refer to three different levels. This repository does not claim the same level for every part of the research.

| Level | Current public status | What an external reader can do |
|---|---|---|
| Result recalculation | Available | Recompute stored counts, estimates, permutation results, decision rules, and privacy checks from released projections |
| Classification audit | Partial | Inspect selected named legacy traces, source manifests, person examples, anonymous schemas, and release rules |
| End-to-end regeneration | Not available | The public repository cannot rebuild every chart exposure and real-world outcome from the original raw birth and biographical sources |

## Level 1: result recalculation

The versioned scripts read frozen public files and compare the recomputed output with canonical result files.

The public surfaces currently include:

- v1 measurement-canary reproduction;
- v2 development-candidate reproduction;
- v3 authored-aggregate person-out reproduction;
- v4 organized-realization family reproduction and privacy validation;
- v5 strict embodied-route reproduction and privacy validation;
- v6 synthesis reproduction;
- v7 external-factor, maxT, decoy, ablation, and privacy reproduction.

Run all public checks with:

```bash
python -m pip install -r requirements-public.txt
python scripts/verify_public_release.py
```

A successful run demonstrates that the released code reproduces the released result from the released projection. It does not provide new empirical confirmation.

## Level 2: classification audit

The public repository provides several forms of supporting evidence:

- 761 named legacy subject traces;
- selected birth-data source URLs and source notes;
- Western and Jyotish chart snapshots for legacy traces;
- fixed route summaries and representative subjects;
- six person-level examples in v6;
- anonymous v2–v7 data schemas;
- machine-readable claim boundaries;
- failed-test and limitation records.

This material allows a reader to inspect examples and understand the structure of the classifications. It does not provide a complete public audit trail for every anonymous v7 row.

## Level 3: end-to-end regeneration

The following are not currently available as one public pipeline:

- a complete immutable snapshot of every raw birth source;
- the full raw biographical evidence used for every outcome decision;
- a public mapping from every source person to every anonymous release ID;
- all code and configuration that regenerated Western and Jyotish chart facts from raw birth data;
- all candidate-generation code and the complete history of researcher choices before the fixed v7 surfaces;
- independent human replication of the real-world activity ratings.

Accordingly, the public package must not be described as fully end-to-end reproducible.

## Why v7 is still useful

The absence of end-to-end regeneration does not make the released statistical checks meaningless. Version 7 can still test whether the five fixed development associations survive the declared measured factors and simultaneous fixed-family null when the released classifications are treated as the analysis input.

The appropriate claim is:

> The published statistics and declared robustness checks can be independently recalculated from the released anonymous projections; the complete raw-source-to-classification pipeline is not public.

## Independence boundaries by release

| Release | Independence description |
|---|---|
| v1 | Measurement canary; no external route test performed |
| v2 | Development construction; external validation count 0 |
| v3 | Separate people for one corrected authored aggregate; other functions underpowered |
| v4 | Conditional person-out outcome-blind test; some source, birth metadata, and older prediction surfaces had prior exposure |
| v5 | Person-separated legacy surface for one strict embodied branch |
| v6 | Synthesis of existing public results; no new test |
| v7 | Measured-factor and multiplicity robustness inside development420; not person-out |

## One public entrypoint and one archival build log

External users should use [PUBLIC_REPRODUCTION.md](../PUBLIC_REPRODUCTION.md). It is the authoritative runnable entrypoint for the standalone repository.

The root [REPRODUCTION.md](../REPRODUCTION.md) is clearly marked as an archival maintainer release-build protocol. It lists private `scripts/verification/` commands that are not included here and is retained only as provenance for how the original public bundle was built.

## Checksums and line endings

The research manifests hash raw file bytes. Changing LF text to CRLF changes those hashes even when the visible text is the same. The repository includes `.gitattributes` to keep tracked text in LF form on new clones. The public quickstart also uses `git -c core.autocrlf=false clone ...` so older global Git settings cannot silently rewrite the checkout.

The cross-platform verifier calculates SHA-256 directly in Python and does not require GNU `sha256sum`.

## What would be required for stronger reproducibility

A future end-to-end release would need a versioned source manifest, stable source snapshots where legally distributable, deterministic chart-generation code, frozen classification rules, blinded or independently repeated outcome ratings, and a public join protocol that does not expose protected personal data.

That would be a new research release. Documentation changes alone must not be presented as solving this boundary.
