# 方法

## 解析単位

解析単位は人物です。一人物は複数の社会機能を持てます。職業・分野は機能の入口に使わず、manifestation、covariate、moderator、transport boundaryとしてのみ扱います。

## 四つの主張階層

1. **Function group**: 本人が現実に何を行ったか。
2. **Meaning mechanism family**: 体系、公的役割、担い手能力、社会機能が共通する上位意味核。
3. **Finite route branch**: connected capability、方向付きrelation、carrier、house/varga modifierを保持した実現枝。
4. **Person interpretation**: 全図と複数行為を統合した人物固有説明。

上位familyの反復を個別枝の検証済み効果と呼びません。個別枝のnullを上位機能群へ拡張しません。

## 現実側

五機能は非排他的です。

- `ADVOCACY_OR_PUBLIC_CAUSE_ACTION`
- `AUTHORED_SYMBOLIC_PRODUCTION`
- `ORGANIZED_COLLECTIVE_REALIZATION`
- `TECHNOLOGY_OR_PRODUCT_IMPLEMENTATION`
- `EMBODIED_COMPETITIVE_PERFORMANCE`

人物証拠はactor、action、object/output、carrierを分けます。SUPPORTED、PARTIAL、CONTESTED、SOURCE_THIN、unknownを保持し、未観測を人生上の陰性へ変換しません。

## 占星術側

WesternとJyotishを二票として足しません。

- Westernは主にMC rulerを通じた公的方向・投射の断面を記述します。
- JyotishはA10 lord、Amatya candidate、10th lordを別の公的役割として保持します。

担い手能力、connected capability、方向付きrelationを分け、house/vargaは原則としてmodifierとして扱います。

## developmentと人物外stress

development420は発見・意味統合の面です。311/109は内部反復で、独立再現ではありません。

v3-v5はそれぞれ異なる人物外面と異なる候補粒度を使いました。結果後に候補、閾値、人物を交換していません。v6は再検定を行わず、公開済み結果を正しい階層へ統合します。

## v6 corrected atlas

`data/corrected_meaning_family_atlas_v6.json`は、固定済みAJM/AJNから個人識別子、出生情報、chart詳細、source textを除いて投影した136 familyの集約面です。各rowはfamily identity、人物支持数、部分群支持、variant relation、反復branch/carrier、train-only specificity countを持ちます。

支持人数は効果量ではありません。family間で人物が重複するため合算しません。specificity countはdevelopment内監査であり、p値や人物外確認ではありません。

## 再現

`scripts/reproduce_v6.py`は、公開v2-v5とv6の固定projectionを読み、主要人数、family数、五機能結果、三つのstress結果、主張境界を再計算・照合します。新しい候補探索や出生図計算は行いません。
