# 独立・社会的発現経路研究 v4

## 結論

今回評価したのは、開発段階で固定された **Jyotish の火星―水星能力対から、集団を組織して実現する行為へ接続する二枝の集約 family** です。職業名を当てる研究ではありません。

conditional person-out 確認枠1,495名のうち、独立した人物ページを持つ一次解析対象は1,457名でした。候補family該当59名、非該当1,398名のうち、固定資料で状態を判定できた人数はそれぞれ58名と1,378名です。本人による組織化行為の直接anchorは、該当群35/58、非該当群739/1,378でした。

言語・出生年代・固定本文量で層別した推定結果は次のとおりです。

- 層固定効果・調和重みrisk difference: `0.0710069495`（約7.10 percentage points）
- HC3 one-sided 95% lower / upper bound: `-0.0292741910` / `0.1712880901`
- 9,999回の層内置換検定、片側p値: `0.1357`
- 98個の同程度decoy集合に対する経験的片側p値: `0.131313`
- 開発段階から固定した基準効果 `delta_ref`: `0.1993299573`
- `delta_ref` に対する最小条件付きpower: `0.906176759`

事前に定めた陽性条件は満たさず、同時に95%上限は `delta_ref` を下回り、基準効果へのpowerは0.8を超えました。したがって終端判定は **`ADEQUATELY_POWERED_PRIMARY_NULL`** です。

平易に言えば、**開発段階と同程度の約19.93 percentage-point以上の効果は、この確認面では再現しませんでした。一方、推定値は約+7.10 pointsであり、より小さい正の関連は否定も確認もされていません。**

## 何が分かったか

分かったこと:

- 固定した二枝familyを、結果後に候補・閾値・人物を変更せず一回評価した。
- 固定資料に記録された本人の組織化行為は、該当群で60.3%、非該当群で53.6%だった。
- 欠測状態を陰性へ潰さないManski boundは `0.0503019` から `0.0815572` だった。
- それでも、層別推定の不確実性、置換null、decoy specificityの事前陽性条件を満たさなかった。
- 開発規模の効果を検出する能力は十分だったため、その大きさの再現についてはnullとして終了できる。

分からなかったこと:

- 約+7.10 pointsという小さい正方向が再現可能な真の関連か、偶然か。
- 二つの枝のどちらか一方が独立に有効か。枝別値は記述のみで、枝別検定をしていない。
- 個別515規則、西洋・インド両体系の収束、旧固定16経路が人物外で再現するか。
- 占星術全体の真偽、因果関係、個人の職業予測。

## 候補familyの意味

候補は一つの集約仮説です。

```text
Jyotishの火星―水星能力対
  -> 担い手・関係・核・carrierが異なる二つの固定枝
  -> ORGANIZED_COLLECTIVE_REALIZATION
     （本人が集団・組織・事業・制度的な共同実現を組み立てる行為）
```

「政治家」「起業家」「経営者」などの肩書は入口にも陽性ラベルにもしていません。分野・職業は、発現媒体、共変量、moderator、またはtransport boundaryとしてのみ扱います。

## 独立性と観測範囲

この確認は **完全に未接触の外部cohortではありません**。人物のsource、出生情報、旧予測面は以前の処理で露出していますが、今回の社会行為のsemantic/outcomeは候補所属を見ない状態で評価しました。このため表現は `CONDITIONAL_PERSON_OUT_SEMANTIC_OUTCOME_BLIND_CONFIRMATION1495` としています。

現実側endpointは、固定された資料に記録された本人の行為です。人生全体にその行為が存在しなかったことを意味しません。評定はAI一系統で、人間による独立追試は未実施です。

## 公開ファイル

- [RESULTS.json](RESULTS.json): 結果の正本
- [METHODS.md](METHODS.md): 固定設計、推定量、終端規則
- [FAILURES_AND_LIMITS.md](FAILURES_AND_LIMITS.md): 失敗と主張限界
- [CLAIM_BOUNDARY.json](CLAIM_BOUNDARY.json): machine-readableな主張境界
- [REPRODUCTION.md](REPRODUCTION.md): 再現・privacy検査・checksum手順
- [data/confirmation1457_anonymous_primary_v4.json](data/confirmation1457_anonymous_primary_v4.json): 匿名一次人物ledger
- [data/primary_permutation_draws_v4.json.gz](data/primary_permutation_draws_v4.json.gz): 固定置換統計量
- [data/decoy_summary_v4.json](data/decoy_summary_v4.json): decoy集約結果

再現は [REPRODUCTION.md](REPRODUCTION.md) の三つの短いコマンドで行えます。
