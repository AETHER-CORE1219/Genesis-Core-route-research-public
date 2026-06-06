# Route Research Reproduction Protocol v1

## Goal

- Rebuild the current public release claim surface for the route research from local research artifacts.

## Required Outputs

- `scripts/verification/data/astrological_validation/all_field_unified_route_freeze_registry_v1.json`
- `scripts/verification/data/astrological_validation/science_route_family_freeze_registry_v2.csv`
- `scripts/verification/data/astrological_validation/route_mass_intake_master_ledger_v1.json`
- `scripts/verification/data/astrological_validation/mass_route_discovery_ledger_v1.json`
- `scripts/verification/data/astrological_validation/observed_route_signature_clusters_v1.json`
- `scripts/verification/data/astrological_validation/observed_packet_review_ledger_v1.json`
- `scripts/verification/data/astrological_validation/explicit_feature_packet_queue_v1.json`
- `scripts/verification/data/astrological_validation/provisional_packet_candidate_ledger_v1.json`
- `scripts/verification/data/astrological_validation/packet_resolution_layer_audit_v1.json`
- `scripts/verification/data/astrological_validation/watch_packet_branch_split_reading_v1.json`
- `scripts/verification/data/astrological_validation/watch_packet_provisional_subbranch_registry_v1.json`
- `scripts/verification/data/astrological_validation/route_research_visual_dashboard_v1.json`
- `scripts/verification/data/astrological_validation/mass_route_research_compact_index_v1.json`
- `scripts/verification/data/astrological_validation/mass_intake_source_backed_exact_round10_v1_source_manifest_v1.json`
- `scripts/verification/data/astrological_validation/route_research_fixed_route_appendix_v1.json`
- `scripts/verification/data/astrological_validation/route_research_fixed_route_appendix_v1.md`
- `scripts/verification/data/astrological_validation/route_research_fixed_route_stage_history_appendix_ja_v1.json`
- `scripts/verification/data/astrological_validation/route_research_fixed_route_stage_history_appendix_ja_v1.md`
- `scripts/verification/data/astrological_validation/route_research_fixed_route_public_summary_ja_v1.json`
- `scripts/verification/data/astrological_validation/route_research_fixed_route_public_summary_ja_v1.md`
- `scripts/verification/data/astrological_validation/route_research_full_report_ja_v1.md`
- `scripts/verification/data/astrological_validation/route_research_github_release_readme_ja_v1.md`
- `scripts/verification/data/astrological_validation/route_research_external_posting_pack_ja_v1.md`
- `scripts/verification/data/astrological_validation/route_research_master_next_plan_ja_v1.md`
- `scripts/verification/data/astrological_validation/route_research_release_bundle_manifest_v1.json`
- `scripts/verification/data/astrological_validation/route_research_release_bundle_manifest_v1.md`
- `route_research_public_release_v1/README.md`
- `route_research_public_release_v1/REPORT_JA.md`
- `route_research_public_release_v1/CLAIM_BOUNDARY.json`
- `route_research_public_release_v1/MASTER_NEXT_PLAN_JA.md`
- `route_research_public_release_v1/BUNDLE_MANIFEST.json`
- `route_research_public_release_v1/CHECKSUMS.sha256`
- `scripts/verification/data/astrological_validation/route_research_release_readiness_check_v1.json`
- `scripts/verification/data/astrological_validation/route_research_release_readiness_check_v1.md`
- `scripts/verification/data/astrological_validation/route_research_publication_freeze_package_v1.json`
- `scripts/verification/data/astrological_validation/route_research_reproduction_protocol_v1.md`

## Command Order

1. `python3 scripts/verification/build_all_field_unified_route_freeze_registry_v1.py`
2. `python3 scripts/verification/build_route_mass_intake_master_ledger_v1.py`
3. `python3 scripts/verification/build_mass_route_discovery_ledger_v1.py`
4. `python3 scripts/verification/build_observed_route_signature_clusters_v1.py`
5. `python3 scripts/verification/build_observed_packet_review_ledger_v1.py`
6. `python3 scripts/verification/build_explicit_feature_packet_queue_v1.py`
7. `python3 scripts/verification/build_packet_role_profile_audit_v1.py`
8. `python3 scripts/verification/build_packet_multilayer_feature_audit_v1.py`
9. `python3 scripts/verification/build_packet_evidence_stack_v1.py`
10. `python3 scripts/verification/build_packet_resolution_layer_audit_v1.py`
11. `python3 scripts/verification/build_watch_packet_branch_split_reading_v1.py`
12. `python3 scripts/verification/build_watch_packet_provisional_subbranch_registry_v1.py`
13. `python3 scripts/verification/build_route_research_visual_dashboard_v1.py`
14. `python3 scripts/verification/build_route_research_fixed_route_appendix_v1.py`
15. `python3 scripts/verification/build_route_research_fixed_route_stage_history_appendix_ja_v1.py`
16. `python3 scripts/verification/build_route_research_fixed_route_public_summary_ja_v1.py`
17. `python3 scripts/verification/build_route_research_publication_freeze_package_v1.py`
18. `python3 scripts/verification/build_route_research_release_bundle_manifest_v1.py`
19. `python3 scripts/verification/build_route_research_release_bundle_files_v1.py`
20. `python3 scripts/verification/build_route_research_release_readiness_check_v1.py`
21. `python3 scripts/verification/build_mass_route_research_compact_index_v1.py`

## Public Claim Boundary

- Publish current fixed routes as route families/branches only.
- Publish the surviving narrow packet as provisional only.
- Publish watch subbranches as provisional internal split signals only.
- Publish science underfilled rows as non-final collection targets.

## Verification Checks

- `route_mass_intake_master_ledger_v1.json` row_count and exact_like_count should match the publication freeze package snapshot.
- `mass_route_discovery_ledger_v1.json` subject_count should match the publication freeze package snapshot.
- `watch_packet_provisional_subbranch_registry_v1.json` row_count should match the publication freeze package snapshot.
- `route_research_publication_freeze_package_v1.json` should be rebuilt last so its snapshot reflects the regenerated ledgers.

