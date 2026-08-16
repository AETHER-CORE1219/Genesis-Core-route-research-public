# 発現経路研究 GitHub公開 README v1

## 最新: 独立・社会的発現経路研究 v3

2026年8月17日、旧16経路とは別の社会的発現研究について、未使用AKS575名を用いた一回の人物外検証まで完了しました。

- 訂正後portable面では、五機能のうち「著作・象徴制作」だけが事前の検出力基準を通過しました。
- 結果blindに凍結したJyotish 25単位のANY機構群は、AKS575で218名該当・357名非該当でした。
- 固定資料上の著作行為を解析できた該当127名・非該当212名の年代標準化差は `-0.02562`、Holm補正pは `1.0` でした。
- よって、この25単位集約は人物外再現しませんでした。他4機能は検出力不足であり、否定していません。
- 個別515規則、西洋・インド収束、因果、職業予測の検証結果ではありません。

現在の主入口は [独立・社会的発現経路研究 v3](independent_social_expression_v3/README_JA.md) です。匿名575名ledger、訂正後25単位manifest、固定解析の再現スクリプトを公開しています。

## 以前の独立研究: 社会的発現5機能

2026年8月に、下記の固定16経路とは別の研究として、社会的発現を職業名ではなく5つの意味機能で扱う研究線を固定しました。

- development420では、西洋・インド両体系が収束する5候補（公益・擁護、著作・象徴制作、集団的実現、技術・製品実装、身体的競争・遂行）が残りました。
- 外部検証前の現実側測定canaryは事前基準を満たさず、`MEASUREMENT_FAILURE` で終了しました。
- したがって、5候補は開発候補であり、外部検証済みでも棄却済みでもありません。AKQ72、AKS575、出生図・経路とのlate joinは未実行です。

開発研究の入口は [独立・社会的発現経路研究 v2](independent_social_expression_v2/README_JA.md) です。匿名420名の人物単位matrix、五機能に関係する固定515規則、311名/109名の部分群別反復、最終actor gate、再現手順、主張境界を確認できます。ただし旧515規則は後続のportable parity監査によりfresh人物へ直接適用できないと判明したため、v3では訂正後機構面を使用しています。

[v1](independent_social_expression_v1/README_JA.md) は最初の12名canaryによる測定失敗を固定した履歴面として不変保存しています。v2も候補の人物外検証成功を主張せず、外部検証0・棄却0・`MEASUREMENT_CONSTRUCT_LIMITATION`を終端とします。

以下は2026年7月24日に固定した旧16経路研究であり、新しい5候補とは別の公開面です。

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
