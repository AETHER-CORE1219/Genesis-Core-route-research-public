# 発現経路研究 GitHub公開 README v1

## 概要

- 本ディレクトリは、占星術における発現経路研究の現時点の公開固定面をまとめたものである。
- 本研究は、西洋占星術とインド占星術の両体系を用いて、著名人物の出生データから反復する発現経路を抽出し、blind ingress と人物単位再読で検証した。
- 第一段階では、著名人物の表での発現が占星術的配置と反復的に一致することを、経路単位の科学的な一致パターンとして発見した。
- 第二段階では、その発見を壊さずに数百人規模へ拡張し、現時点のデータで正確に発現を記述できる経路だけを公開固定面へ残した。
- 現在の公開主張面は `16本` の固定経路である。

## 現在の研究スナップショット

- master subjects: `1030`
- exact-like subjects: `795`
- subject-level discovery traces: `761`
- fixed route claims: `16`
- unified non-claim rows: `14`
- science nonfixed rows: `16`
- surviving narrow packet candidate: `1`
- watch-packet provisional subbranches: `8`

## 研究は二段階で構成される

### 第一段階

- publication 台帳 `188 rows / 151 unique people` を母体に、分野ごとの発現経路そのものを発見した。
- ここでいう発見とは、著名人物の表での発現と占星術的配置の間に、反復して観測できる一致パターンがあることを確認した、という意味である。
- この段階で、現在の fixed route inventory の原型が形成された。

### 第二段階

- publication 外の人物を現在の経路 inventory に blind に流し、数百人単位で拡張した。
- この段階では、第一段階で見つかった一致をそのまま誇張せず、現時点の exact 母集団でどこまで正確に発現を記述できるかを監査した。
- 目的は、新経路の乱立ではなく、
  - 既存経路が太るか
  - 共通因子が露出するか
  - 保留群が固定へ進むか
  - packet-level 候補が残るか
  を確認することだった。

## この公開で主張していること

- 固定 `16本` の route family / route branch が、現時点の公開主張面である。
- この 16 本は、現時点のデータと監査手順に基づき、発現をもっとも正確に記述できる公開用手法である。
- これらは deterministic な職業予測ルールではない。
- blind ingress の top route は最終ラベルではなく、route pressure observation として扱う。

## この公開で主張していないこと

- unified 側の保留 `14本` は未固定である。
- science 側の `16本` は clue / holdout / underfilled 群であり、固定 route ではない。
- surviving narrow packet candidate `1本` は provisional であり、まだ fixed route ではない。
- watch-packet provisional subbranches `8本` は内部 split signal であり、新経路ではない。

## 最初に読むべきファイル

### 1. 全体把握

- `route_research_full_report_ja_v1.md`
- `route_research_publication_freeze_package_v1.md`

### 2. 固定経路の把握

- `route_research_fixed_route_public_summary_ja_v1.md`
- `route_research_fixed_route_stage_history_appendix_ja_v1.md`
- `route_research_fixed_route_appendix_v1.md`

### 3. claim boundary の確認

- `route_research_publication_freeze_package_v1.json`
- `all_field_unified_route_freeze_registry_v1.json`
- `science_route_family_freeze_registry_v2.csv`

### 4. 再現

- `route_research_reproduction_protocol_v1.md`
- `mass_route_research_compact_index_v1.json`

### 5. 次段計画

- `route_research_master_next_plan_ja_v1.md`
- ここには、公開固定面の維持、公開後の exact 拡張、hold 面再評価、第三段階の deeper split 研究までの順序を一枚にまとめてある。

## 推奨公開順

1. `route_research_full_report_ja_v1.md` を研究本文として置く
2. `route_research_fixed_route_public_summary_ja_v1.md` を短い公開説明として置く
3. `route_research_fixed_route_stage_history_appendix_ja_v1.md` を経路別の二段階根拠として添付する
4. `route_research_publication_freeze_package_v1.json` を claim boundary として明示する
5. `route_research_reproduction_protocol_v1.md` を再現手順として置く
6. `route_research_master_next_plan_ja_v1.md` を公開後の研究計画として添付する

## 注意

- この研究は「何が fixed で、何が hold か」を厳密に分けることを重視している。
- したがって、固定 `16本` 以外を fixed route として引用しないこと。
- 特に、science 群、narrow packet 候補、watch subbranch は将来研究対象であり、現時点の主張面ではない。
