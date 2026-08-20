# 独立・社会的発現経路研究 v5

## 結論

今回評価したのは、development420で結果を見る前に固定された、次の一つの厳密なJyotish候補です。

```text
Amatya候補
  -> 土星的な構造・限界・義務・持続の担い手
  -> 木星的な知識・判断・正当化能力への方向付き依存／媒介
  -> Dusthana carrier
  -> 身体的競争・遂行
```

開発面では14名中6名に直接支持があり、311名側で4/10、109名側で2/4と、両部分群で各基礎率より高い方向でした。これは候補発見の根拠ですが、独立確認ではありません。

legacy1030を全員保持して役割を分けると、候補発見と人物分離された一次解析は313名でした。固定資料から競技者anchorを判定できた230名について、厳密な完全鎖の該当者は7名でしたが、競技者anchorは0名でした。非該当者では27/223名でした。

- 層調整risk difference: `-0.0527426351`
- HC3片側95%下限 / 上限: `-0.1251912170` / `0.0197059467`
- 9,999回の層内置換、片側p値: `1.0`
- 99個の同程度decoyに対する経験的p値: `0.63`
- 欠測を両端へ置いたManski bound: `-0.3531353135` から `0.2108910891`

したがって、この完全鎖が競技者へ特異的に濃縮するという人物外の正関連は再現しませんでした。ただし、曝露者が10名と少なく、開発差を50%縮小した約11.45ポイントへの事前powerは`0.11199`でした。そのため終端は **`INCONCLUSIVE_STRICT_ROUTE_WITH_DIRECTION_AND_LIMITS_REPORTED`** です。これは占星術全体、身体表現全体、他の候補を否定するnullではありません。

## 意味として新たに分かったこと

完全鎖からDusthana carrierだけを外し、同じ土星―木星の意味核を見ると、競技者anchorは2/13対25/217、層調整差は約`+0.03379`でした。方向は正ですが、片側95%下限は負で、置換p値は`0.5276`です。

この差から、開発時の信号を「Dusthanaを伴う競技者専用経路」と読むのは不適切だった可能性が高いと分かりました。残る仮説は、土星的持続・制約と木星的判断の接続が、競技だけでなく訓練・規律・熟達など、より上位の実現機能へ関係する可能性です。本研究では結果後にその仮説へ候補を変更・再検定していません。

## 研究上の位置づけ

v5が分離したのは三層です。

1. 開発発見: 14名中6名で反復した候補信号。
2. 人物外評価: 厳密な完全鎖の競技者濃縮は再現せず。
3. 解釈上の発見: carrierを外した意味核には弱い正方向が残るが未確認。

職業は入口や正解ラベルではなく、意味機能が現れる媒体・共変量・transport boundaryです。固定資料でanchorが見つからないことを、人生上その行為がないという陰性にはしていません。

## 公開ファイル

- [RESULTS.json](RESULTS.json): 結果の正本
- [METHODS.md](METHODS.md): 候補固定、現実endpoint、解析
- [FAILURES_AND_LIMITS.md](FAILURES_AND_LIMITS.md): 失敗原因と主張限界
- [CLAIM_BOUNDARY.json](CLAIM_BOUNDARY.json): machine-readableな主張境界
- [REPRODUCTION.md](REPRODUCTION.md): 再現・privacy・checksum手順
- [data/legacy313_anonymous_primary_v5.json](data/legacy313_anonymous_primary_v5.json): 匿名一次人物ledger
- [data/decoy_summary_v5.json](data/decoy_summary_v5.json): 99 decoyの集約結果

再現方法は [REPRODUCTION.md](REPRODUCTION.md) を参照してください。
