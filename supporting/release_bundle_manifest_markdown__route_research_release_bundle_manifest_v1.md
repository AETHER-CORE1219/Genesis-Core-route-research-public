# 発現経路研究 公開バンドル構成 v1

- purpose: 現在の研究を公開するとき、どのファイルを前面・根拠層・補助層に置くかを固定する
- fixed_route_count: 16
- unified_nonclaim_count: 14
- science_nonfixed_count: 16

## 推奨公開順

1. README.md <= route_research_github_release_readme_ja_v1.md
2. REPORT_JA.md <= route_research_full_report_ja_v1.md
3. FIXED_ROUTE_SUMMARY_JA.md <= route_research_fixed_route_public_summary_ja_v1.md
4. CLAIM_BOUNDARY.json <= route_research_publication_freeze_package_v1.json
5. REPRODUCTION.md <= route_research_reproduction_protocol_v1.md
6. MASTER_NEXT_PLAN_JA.md <= route_research_master_next_plan_ja_v1.md
7. FIXED_ROUTE_STAGE_HISTORY_JA.md <= route_research_fixed_route_stage_history_appendix_ja_v1.md
8. FIXED_ROUTE_APPENDIX.md <= route_research_fixed_route_appendix_v1.md
9. POSTING_PACK_JA.md <= route_research_external_posting_pack_ja_v1.md

## 前面に出すファイル

- scripts/verification/data/astrological_validation/route_research_fixed_route_public_summary_ja_v1.md | role=fixed_route_public_summary_markdown / root_alias=FIXED_ROUTE_SUMMARY_JA.md
- scripts/verification/data/astrological_validation/route_research_full_report_ja_v1.md | role=full_report_japanese / root_alias=REPORT_JA.md
- scripts/verification/data/astrological_validation/route_research_github_release_readme_ja_v1.md | role=github_release_readme_japanese / root_alias=README.md
- scripts/verification/data/astrological_validation/route_research_master_next_plan_ja_v1.md | role=master_next_plan / root_alias=MASTER_NEXT_PLAN_JA.md
- scripts/verification/data/astrological_validation/route_research_publication_freeze_package_v1.json | role=publication_freeze_package / root_alias=CLAIM_BOUNDARY.json
- scripts/verification/data/astrological_validation/route_research_reproduction_protocol_v1.md | role=reproduction_protocol / root_alias=REPRODUCTION.md

## 固定経路の根拠層

- scripts/verification/data/astrological_validation/all_field_unified_route_freeze_registry_v1.json | role=current_fixed_route_inventory
- scripts/verification/data/astrological_validation/route_research_fixed_route_appendix_v1.json | role=fixed_route_appendix
- scripts/verification/data/astrological_validation/route_research_fixed_route_appendix_v1.md | role=fixed_route_appendix_markdown / root_alias=FIXED_ROUTE_APPENDIX.md
- scripts/verification/data/astrological_validation/route_research_fixed_route_stage_history_appendix_ja_v1.json | role=fixed_route_stage_history_appendix
- scripts/verification/data/astrological_validation/route_research_fixed_route_stage_history_appendix_ja_v1.md | role=fixed_route_stage_history_appendix_markdown / root_alias=FIXED_ROUTE_STAGE_HISTORY_JA.md
- scripts/verification/data/astrological_validation/route_research_fixed_route_public_summary_ja_v1.json | role=fixed_route_public_summary

## 再現・追跡の補助層

- scripts/verification/data/astrological_validation/science_route_family_freeze_registry_v2.csv | role=science_route_nonfixed_inventory
- scripts/verification/data/astrological_validation/route_mass_intake_master_ledger_v1.json | role=mass_intake_master
- scripts/verification/data/astrological_validation/mass_route_discovery_ledger_v1.json | role=subject_level_route_trace
- scripts/verification/data/astrological_validation/route_research_visual_dashboard_v1.json | role=visual_dashboard_manifest
- scripts/verification/data/astrological_validation/mass_route_research_compact_index_v1.json | role=compact_index
- scripts/verification/data/astrological_validation/mass_intake_source_backed_exact_round10_v1_source_manifest_v1.json | role=latest_source_manifest_example

## 未主張境界と文脈層

- scripts/verification/data/astrological_validation/observed_route_signature_clusters_v1.json | role=observed_cluster_summary
- scripts/verification/data/astrological_validation/observed_packet_review_ledger_v1.json | role=packet_review_queue
- scripts/verification/data/astrological_validation/explicit_feature_packet_queue_v1.json | role=explicit_feature_packet_queue
- scripts/verification/data/astrological_validation/provisional_packet_candidate_ledger_v1.json | role=surviving_narrow_packet_candidate
- scripts/verification/data/astrological_validation/packet_resolution_layer_audit_v1.json | role=packet_resolution_audit
- scripts/verification/data/astrological_validation/watch_packet_branch_split_reading_v1.json | role=watch_packet_branch_split
- scripts/verification/data/astrological_validation/watch_packet_provisional_subbranch_registry_v1.json | role=watch_packet_provisional_subbranches
- scripts/verification/data/astrological_validation/route_research_external_posting_pack_ja_v1.md | role=external_posting_pack_japanese / root_alias=POSTING_PACK_JA.md

## その他

- scripts/verification/data/astrological_validation/route_research_release_bundle_manifest_v1.json | role=release_bundle_manifest
- scripts/verification/data/astrological_validation/route_research_release_bundle_manifest_v1.md | role=release_bundle_manifest_markdown
- route_research_public_release_v1/README.md | role=materialized_release_bundle_readme
- route_research_public_release_v1/REPORT_JA.md | role=materialized_release_bundle_report
- route_research_public_release_v1/CLAIM_BOUNDARY.json | role=materialized_release_bundle_claim_boundary
- route_research_public_release_v1/MASTER_NEXT_PLAN_JA.md | role=materialized_release_bundle_master_next_plan
- route_research_public_release_v1/BUNDLE_MANIFEST.json | role=materialized_release_bundle_manifest
- route_research_public_release_v1/CHECKSUMS.sha256 | role=materialized_release_bundle_checksums
- scripts/verification/data/astrological_validation/route_research_release_readiness_check_v1.json | role=release_readiness_check
- scripts/verification/data/astrological_validation/route_research_release_readiness_check_v1.md | role=release_readiness_check_markdown

## Guardrails

- Current fixed routes are route families or branches supported by existing exact cohorts; they are not universal deterministic career classifiers.
- The surviving narrow packet is not yet a fixed route claim. It remains a provisional packet candidate.
- Watch-packet subbranches are not route claims. They are repeated internal split signals waiting for fresh exact repeats.
- Science registry rows in NOT_FIXED or UNDERFILLED states must be published as retained clues or future collection targets, not as confirmed routes.
- Blind ingress and top-route assignment should be described as route pressure observation, not final classification.
