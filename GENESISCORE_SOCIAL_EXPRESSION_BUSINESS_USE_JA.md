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

公開v7で、development420の五機能は、年代、現実資料の測定形態、収集元を順に加えたM0→M3でもすべて正方向を維持し、固定22面のperson-package maxTでも同時補正後p=`0.0001`～`0.0047`でした。したがって、GenesisCoreの研究betaでは科学statusを`DEVELOPMENT_MEASURED_CONFOUND_ROBUST`へ更新できます。ただし同じdevelopment420内の結果であり、`EXTERNALLY_REPLICATED`や診断精度には昇格しません。

| レイヤー | 現在利用できること | 利用してはいけないこと |
|---|---|---|
| 五機能 | development420での候補関連、311/109方向反復、年代・資料形態・収集元調整、固定22面maxTを説明 | 外部確認済み、因果、成功確率と表示 |
| mechanism family | 同じ機能へ至る異なる担い手・関係・carrierを提示 | 有意な一意ルート、唯一の原因と表示 |
| exact branch | 個人の全図文脈を説明する | 一枝を機能全体の代表予測器にする |
| v3-v5 | 特定ANY、二枝family、完全一枝の人物外ストレス結果を表示 | そのnullを他の機能・枝・占星術全体へ拡張 |

外部で正に確認済みの経路は現在0です。一方、developmentで観測された五機能の構造は削除されておらず、検証された範囲と未確認範囲を分ければ、研究情報として利用できます。

公開v6では、五機能に136の訂正済みmeaning familyを整理し、そのうち134が311名側と109名側の双方に人物支持を持つことを再現可能にしました。ただし136は診断精度でも検証済みroute数でもありません。GenesisCoreへ載せる際は、136 familyを一律スコア化せず、該当する上位meaning familyと有限branchを説明候補として返します。

## 「再現可能」と「偶然ではない」の区別

公開v6とv7が達成したのは、次の三点です。

1. `COMPUTATIONALLY_REPRODUCIBLE`
   - 固定済みデータ、コード、manifest、checksumから、第三者が同じ人数・比率・外部ストレス結果を再生成できます。
2. `DEVELOPMENT_PATTERN_REPEATED`
   - development420では五機能すべてが各基礎率より高く、311名側と109名側の双方で上昇方向が反復しています。単発の人物例や一つの集計ミスだけではない、追跡可能な開発所見です。
3. `DEVELOPMENT_MEASURED_CONFOUND_ROBUST`
   - 五機能すべてが年代、資料形態、収集元を順に調整しても正で、固定22面maxTの同時補正後も残りました。
   - 固定22面という宣言範囲では、偶然だけでは説明しにくく、測定済み三要因だけでも説明されません。

まだ達成していないのは、次です。

- `CHANCE_EXCLUDED_BY_INDEPENDENT_CONFIRMATION`
  - 311名と109名は同じ候補開発面の内部部分群であり、独立した外部再現ではありません。
  - v3、v4、v5の人物外ストレスは、三つの限定された集約・family・branchを正に確認しませんでした。
  - v7は固定22面の多重性を扱いましたが、それ以前の741/515/136候補形成の全自由度や未測定交絡を排除していません。

したがって外部向けには、次の表現を使います。

> 固定development420と固定22面の範囲では、五機能の関連は測定済みの年代・資料形態・収集元だけでは説明されず、宣言した同時nullの偶然だけでも説明しにくい。独立人物外再現、因果、検証済み診断精度ではない。

「科学的手順を用いた再現可能な占星術研究」として公開・紹介することはできます。ただし「科学的に占星術を確認した」「偶然ではないことを証明した」とは表示しません。

## GenesisCore採用status

GenesisCoreでは、科学statusを次の有限値で保持し、ユーザーにも表示します。

| status | 意味 | 製品での扱い |
|---|---|---|
| `DEVELOPMENT_REPEATED_NOT_EXTERNALLY_CONFIRMED` | development内で人物支持と方向反復がある | 解釈候補として表示できる |
| `DEVELOPMENT_MEASURED_CONFOUND_ROBUST` | 年代・資料形態・収集元調整と固定22面maxTを通過した | research-betaで根拠値と同時下限を表示できる |
| `EXTERNAL_STRESS_NONPOSITIVE_LIMITED` | 特定の集約・family・branchが人物外で正に確認されなかった | その単位を昇格せず、限定nullを併記する |
| `UNTESTED_EXTERNALLY` | 人物外でまだ評価していない | 仮説・研究候補としてのみ表示する |
| `AMBIGUOUS_MULTI_ROUTE` | 複数のmeaning familyまたはbranchが同時に成立する | 一つへ強制せず、代替経路を並列表示する |
| `INSUFFICIENT_PERSON_LEVEL_EVIDENCE` | 個人の全図または現実側証拠が不足する | 不在判定をせずunknownとして返す |

これらを確率へ変換しません。`interpretive_strength`は説明上の優先度であり、発現確率・診断精度・成功確率ではありません。

## 実装前に必要な対応表

現在の公開面には、粒度の異なる三つの集合があります。

- 515件のdevelopment rule
- 120件のpublic mechanism ID
- 136件の訂正済みmeaning family

これらは同じものではなく、一対一対応でもありません。GenesisCoreへ実装する前に、研究結果を変更しないread-onlyの対応表を一度作ります。

```text
rule_id
→ mechanism_id
→ corrected_meaning_family_id
→ function_id（複数可）
→ system（Western / Jyotish）
→ actor / relation / carrier
→ scientific_status
→ supporting / counter / unknown evidence
```

対応不能、意味衝突、旧定義しかない項目は推測で接続せず、`UNMAPPED`または`CONFLICTING_DEFINITION`として保存します。この対応表は実装上の索引であり、新しい科学的発見や経路昇格ではありません。

## 診断時の処理順序

1. 出生図からWesternとJyotishを別々に意味鎖へ変換する。
2. 各体系で、担い手、方向付き関係、状態、carrier、modifierを保持したまま候補familyを照合する。
3. 一人につき複数の五機能と複数branchを許容する。
4. 両体系は加点票にせず、一致、補完、緊張、片側のみを記述する。
5. 科学status、反証、unknownを付けて説明候補を返す。
6. 本人の現実情報は、出力後の共同確認にだけ用いる。現実情報を見て出生図側のrule、score、順位を書き換えない。

診断の一次出力は「この職業になる」ではなく、「どの意味機能が、どの実現枝を通じて、どの社会的作用として現れ得るか」です。職業、分野、事業形態は、その後に現れるmanifestation、covariate、moderator、transport boundaryとして扱います。

## 一般向け表示例

> あなたの図では、情報や媒介を現実の仕組みへ変える枝と、構造を持続可能な組織へ固定する枝が、組織的実現という同じ上位機能へ接続する可能性があります。これは職業や成功を予測する確率ではなく、公開研究のdevelopment内で反復した解釈候補です。人物外で正に確認された診断器ではないため、代替枝、反証、未確認点も同時に表示します。

この形式なら、占星術の多義性を消さず、研究結果より強い断定も避けられます。

## GenesisCoreでの推奨出力

一人へ一つのroute labelを返さず、次の階層を返します。

```json
{
  "research_layer": "SOCIAL_EXPRESSION_V7",
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
      "scientific_status": "DEVELOPMENT_MEASURED_CONFOUND_ROBUST_NOT_EXTERNALLY_REPLICATED",
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
- 新しい社会的発現研究: `social_expression_v7`研究レイヤー

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
- `social_expression_v7`専用namespaceと科学statusの永続保存
- 515 rule・120 mechanism・136 familyのread-only対応表作成

### No-Go

- 48経路の即時削除・置換
- 検証済み予測器として販売
- 職業・成功・人生の確率表示
- 一つの経路への強制分類
- 科学statusを隠したマーケティング
- development内反復を「偶然を排除した外部確認」と表現すること
- 対応不能なruleを類似語だけでfamilyへ自動統合すること

## 採用判断

> GenesisCoreへは、五機能の多経路解釈を独立した研究betaとして導入できる。ただし、外部確認済みの診断器ではなく、出典・代替枝・反証・不確実性を伴う説明システムとして提供する。

この境界は、今後の研究で正の人物外再現が得られた場合だけ、該当function family単位で更新します。他のfunction、mechanism、branchへ自動昇格させません。

研究根拠と再現手順は [社会的発現経路・外部要因頑健性研究 v7](independent_social_expression_v7/README_JA.md) を最新正本とし、意味familyと人物例は [v6](independent_social_expression_v6/README_JA.md) を参照します。
