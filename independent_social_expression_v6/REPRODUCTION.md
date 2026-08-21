# 再現手順

リポジトリrootから実行します。

```bash
PYTHONDONTWRITEBYTECODE=1 python3 independent_social_expression_v6/scripts/reproduce_v6.py
(cd independent_social_expression_v6 && sha256sum -c CHECKSUMS.sha256)
```

再現器は公開済みv2、v3、v4、v5とv6の公開projectionだけを読みます。人物名から出生図を再計算せず、private path、出生時刻、chart、未公開人物membershipへアクセスしません。

再現されるのは次です。

- development420の五機能結果
- 公開515規則と120 mechanism ID
- 訂正済み五機能136 meaning familyと両部分群支持134
- 六つの人物trace
- v3 ANY25、v4二枝family、v5 strict branchの結果と主張境界

このコマンドは新しい統計検定や候補選定を行いません。
