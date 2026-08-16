# 方法

## 1. 検証対象と主張階層

一次仮説は一つです。

- system: `JYOTISH`
- family: `JYOTISH_MARS_MERCURY_ORGANIZED_REALIZATION_TWO_BRANCH_FAMILY`
- social function: `ORGANIZED_COLLECTIVE_REALIZATION`
- unit: `ONE_FIXED_TWO_BRANCH_AGGREGATE_FAMILY`

二枝は同じ火星―水星能力対を共有し、role、relation、core、carrierが異なります。今回の検定単位は二枝をまとめたfamilyです。枝別risk differenceは記述目的だけであり、枝別p値、枝別昇格、個別routeの検証は行いません。

分野・職業は候補発見やendpointの入口にせず、manifestation、covariate、moderator、transport boundaryとしてのみ扱います。

## 2. 確認枠と分離

- 固定frame: 1,495名
- 固定資料あり: 1,471名
- 独立人物ページを持つ一次群: 1,457名
- family該当: 59名
- family非該当: 1,398名
- shared-page secondary: 14名、6群
- structural unknown: 24名

一次解析には独立人物ページ1,457名だけを使いました。候補所属と、固定資料から得た現実側endpointは別々に凍結し、人物集合とhashを照合して一度だけlate joinしました。shared-page人物は関連人物の混入を避けるため一次推定から外し、記述的secondaryとしました。

この枠は完全未接触ではありません。source、出生情報、旧予測は以前に露出しましたが、今回用いた社会行為のsemantic/outcomeは候補所属を見ずに凍結しました。したがって確認面は `CONDITIONAL_PERSON_OUT_SEMANTIC_OUTCOME_BLIND_CONFIRMATION1495` です。

## 3. 現実側endpoint

観測単位は人物です。固定資料中の引用から、本人が集団・組織・共同事業等を組み立て、率い、創設し、制度的に実現した直接のactor-action anchorを評価しました。

一次状態は次の四つです。

- `SUPPORTED`
- `NO_DIRECT_ANCHOR_OBSERVED_IN_ADEQUATE_FIXED_SOURCE`
- `PARTIAL`
- `UNKNOWN_NO_ANALYSIS_ELIGIBLE_EVIDENCE` または `UNKNOWN_SEMANTIC_OR_ACTOR`

一次推定のdecided maskは最初の二状態だけです。`PARTIAL` と `UNKNOWN_*` は陰性へ変換しません。`NO_DIRECT_ANCHOR_OBSERVED_IN_ADEQUATE_FIXED_SOURCE` は「固定資料で直接anchorを観測しなかった」という意味であり、人生全体に行為が存在しないという意味ではありません。

一次群のcoverageは該当群 `0.9830508475`、非該当群 `0.9856938484`、絶対差 `0.0026430009` でした。decided数は58対1,378です。

評定は一つのAI系統によるものです。同じAIの反復を独立評定とは数えず、人間による独立追試も主張しません。

## 4. 一次推定量

固定層は次の直積です。

```text
SOURCE_LANGUAGE × BIRTH_ERA × FIXED_TEXT_LENGTH
```

出生年代は `BEFORE_1900`、`1900_1924`、`1925_1949`、`1950_AND_LATER`、本文量は `TEXT_SHORT`、`TEXT_MEDIUM`、`TEXT_LONG` です。一次群に存在した36層のうち、両曝露群とdecided endpointを持つ24層がestimableでした。

一次estimandは、層固定効果OLSの曝露係数です。これは各層のrisk differenceを `n1s*n0s/(n1s+n0s)` で調和重み付けした値と等価です。分散はHC3です。一次推定に残った人物は1,221名でした。

結果:

- `SUPPORTED`: 35/58 vs 739/1,378
- harmonic risk difference: `0.0710069495149408`
- HC3 standard error: `0.060966604513586056`
- one-sided 95% lower bound: `-0.02927419104214718`
- one-sided 95% upper bound: `0.17128809007202886`

## 5. Null、specificity、欠測

### 層内置換null

曝露人数を層内で固定し、人物の曝露ラベルを各層内で9,999回置換しました。乱数はNumPy 2.2.6の `Generator(PCG64)`、seed `20260817` です。

```text
p = (1 + count(T_perm >= T_observed)) / (9999 + 1)
  = 0.1357
```

### Decoy specificity

複雑度とprevalenceを揃えた凍結decoy集合98個を同じendpointへ適用しました。観測family以上の統計量を持つdecoyは12個で、固定分母99の経験的片側p値は `0.1313131313` です。decoy人物ベクトルそのものはprivacy保護のため公開せず、集約summaryだけを公開します。

### 欠測感度

未判定者を陰性にせず、該当・非該当群の未判定を反対方向の極端値へ置いたsharp Manski boundを計算しました。

- lower: `0.0503018840`
- upper: `0.0815571882`

これは欠測割当だけへのboundです。標本変動、残存交絡、測定誤差、decoy specificityを解消する検定ではありません。

## 6. 検出力と事前終端規則

開発段階から固定した参照効果は `delta_ref = 0.1993299573270514` です。観測された24層のsupportを条件に、非該当側基礎率0.1から0.8のgridで評価した最小powerは `0.9061767589853145` でした。worst-case 80% MDEは `0.16695679312101627` です。

陽性には次の全てを要求しました。

1. permutation `p < 0.05`
2. HC3 one-sided 95% lower bound `> 0`
3. decoy empirical `p <= 0.05`

`ADEQUATELY_POWERED_PRIMARY_NULL` には次の全てを要求しました。

1. 陽性条件が不成立
2. `delta_ref` への最小条件付きpower `>= 0.80`
3. HC3 one-sided 95% upper bound `< delta_ref`

今回の結果は後者を満たしました。推定値の符号をnull条件に入れていないため、小さい正方向が残った状態でも、開発規模の効果について適切にnull終端できます。

## 7. 独立再計算と結果後変更の禁止

独立validatorはproducerをimportせず、人物join、coverage、FE/HC3、9,999置換、98 decoy、Manski bound、条件付きMDE、終端優先順位を再計算し `PASS` しました。

結果後に人物交換、新cohort、候補・閾値変更、枝別確認検定、救済解析は行っていません。
