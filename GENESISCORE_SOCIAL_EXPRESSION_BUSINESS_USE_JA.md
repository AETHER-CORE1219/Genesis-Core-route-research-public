# GenesisCore向け社会的発現経路研究の事業利用境界

更新日: 2026-08-21

## 結論

この社会的発現研究は、GenesisCoreへ「職業を当てる48本の新ルート」として置き換えるものではありません。現時点で利用できるのは、個人の出生図に現れる意味構造を、五つの非排他的な社会機能、複数のmechanism family、人物固有の実現枝として説明する研究レイヤーです。

製品へ導入する価値はあります。ただし用途は、検証済みの予測器ではなく、根拠と限界を表示する解釈・仮説生成・対話支援です。

## 利用できる五機能

1. `ADVOCACY_OR_PUBLIC_CAUSE_ACTION`
   - 公益、権利、保護、改革目的へ働きかける。
2. `AUTHORED_SYMBOLIC_PRODUCTION`
   - 文章、理論、作品、象徴体系を本人の著作物として固定する。
3. `ORGANIZED_COLLECTIVE_REALIZATION`
   - 組織、集団、制度、制作体制を作り、複数人の活動を現実化する。
4. `TECHNOLOGY_OR_PRODUCT_IMPLEMENTATION`
   - 装置、製品、治療、方法、工程を作動可能な形へ実装する。
5. `EMBODIED_COMPETITIVE_PERFORMANCE`
   - 身体を用いる競争、記録、試合、反復遂行へ出力する。

これらは職業ではありません。一人が複数機能を持ち、同じ機能へ複数の占星術的経路から到達できます。

## 現在の科学status

| レイヤー | 現在利用できること | 利用してはいけないこと |
|---|---|---|
| 五機能 | development420での候補関連と311/109の内部方向反復を説明 | 外部確認済み、因果、成功確率と表示 |
| mechanism family | 同じ機能へ至る異なる担い手・関係・carrierを提示 | 有意な一意ルート、唯一の原因と表示 |
| exact branch | 個人の全図文脈を説明する | 一枝を機能全体の代表予測器にする |
| v3-v5 | 特定ANY、二枝family、完全一枝の人物外ストレス結果を表示 | そのnullを他の機能・枝・占星術全体へ拡張 |

外部で正に確認済みの経路は現在0です。一方、developmentで観測された五機能の構造は削除されておらず、検証された範囲と未確認範囲を分ければ、研究情報として利用できます。

公開v6では、五機能に136の訂正済みmeaning familyを整理し、そのうち134が311名側と109名側の双方に人物支持を持つことを再現可能にしました。ただし136は診断精度でも検証済みroute数でもありません。GenesisCoreへ載せる際は、136 familyを一律スコア化せず、該当する上位meaning familyと有限branchを説明候補として返します。

## GenesisCoreでの推奨出力

一人へ一つのroute labelを返さず、次の階層を返します。

```json
{
  "research_layer": "SOCIAL_EXPRESSION_V6",
  "functions": [
    {
      "function_id": "TECHNOLOGY_OR_PRODUCT_IMPLEMENTATION",
      "interpretive_strength": "MODERATE",
      "matched_mechanism_families": ["..."],
      "exact_branches": ["..."],
      "modifiers": ["..."],
      "western_reading": {"status": "...", "chain": ["..."]},
      "jyotish_reading": {"status": "...", "chain": ["..."]},
      "cross_system_relation": "COMPLEMENTARY",
      "scientific_status": "DEVELOPMENT_SIGNAL_NOT_EXTERNALLY_CONFIRMED",
      "counterevidence": ["..."],
      "unknowns": ["..."]
    }
  ]
}
```

### 必須表示

- `scientific_status`
- WesternとJyotishの別々のchain
- 同じ機能へ至る代替mechanism
- modifierと個人差
- counterevidence
- unknowns
- 「職業・成功・因果を一意予測しない」という表示

### 禁止表示

- 「この人は起業家になる」のような一意な職業断定
- `85% accurate`のような未検証の精度表示
- symbolic fitを科学的確率へ変換した数値
- WesternとJyotishを二票として加点
- exact branchがないことを機能不在とする判定
- v3-v5の限定nullから占星術全体を否定する文言

## 既存48経路との関係

既存48経路を直ちに置き換えません。両者を混在させず、別version・別namespaceにします。

- 既存48経路: 現行製品の歴史的診断レイヤー
- 新しい社会的発現研究: `social_expression_v6`研究レイヤー

移行する場合は、最初にread-onlyの比較表示を行います。同じ人物について、48経路結果と五機能・mechanism family結果を並べますが、相互変換や自動統合はしません。

## 導入段階

### 段階1: 研究モード

- 開発者・検証者だけに表示
- 五機能、意味連鎖、代替枝、科学statusを表示
- user-facing scoreやランキングは出さない

### 段階2: 説明支援

- 対話AIが複数の可能な発現方法を説明
- 本人の現実状況を聞き、どの枝が現れているかを共同で確認
- 現実情報から出生図側の答えを後付け変更しない

### 段階3: 一般向けbeta

- claim boundaryを画面内に常設
- feedbackは研究データと製品ログを分離
- feedbackで研究ruleを自動更新しない

## 事業価値

現時点の強みは、単純な職業当てではなく、次を一つの診断で扱えることです。

- 一人の複数出力
- 同じ出力へ至る代替経路
- 西洋・インド両体系の一致、補完、矛盾
- 個人固有のmodifier
- 反例と未説明状態
- 研究statusを伴う説明

これはGenesisCoreの「AI×ホロスコープ」に適しています。AIは断定器ではなく、全図の意味構造と複数の現実化可能性を整理する対話層として使えます。

## 現時点のGo/No-Go

### Go

- 研究モードでの実装
- 五機能の非排他的表示
- mechanism familyとexact branchの説明
- Western/Jyotishの別表示
- 科学status、反例、unknownの表示
- ユーザーとの仮説確認

### No-Go

- 48経路の即時削除・置換
- 検証済み予測器として販売
- 職業・成功・人生の確率表示
- 一つの経路への強制分類
- 科学statusを隠したマーケティング

## 採用判断

> GenesisCoreへは、五機能の多経路解釈を独立した研究betaとして導入できる。ただし、外部確認済みの診断器ではなく、出典・代替枝・反証・不確実性を伴う説明システムとして提供する。

この境界は、今後の研究で正の人物外再現が得られた場合だけ、該当function family単位で更新します。他のfunction、mechanism、branchへ自動昇格させません。

研究根拠と再現手順は [占星術的社会発現経路研究 v6](independent_social_expression_v6/README_JA.md) を正本とします。
