# 再現手順

## 必要環境

- Python 3.10以降
- 外部Pythonパッケージ、GPU、ネットワーク接続は不要

## 実行

リポジトリ直下で次を実行します。

```bash
python3 independent_social_expression_v1/scripts/reproduce_measurement_failure_v1.py
```

検証器は公開された匿名データだけから次を再計算します。

- 12人物 × 5機能 × 2手順 = 120評定の完全性
- 生応答186件の連番、SHA-256、評定・引用との完全対応
- 全体precision、recall、F1
- 手順別・機能別precision、recall、F1
- 二手順の二値一致率
- 陽性引用の対象行為接地率
- abstention率
- 事前固定gateと終端判定
- AKQ72、AKS575、出生図・経路へのアクセスが0である公開境界

出力例:

```json
{"binary_agreement": 0.8333333333333334, "candidate_count": 5, "external_route_validation_count": 0, "overall_f1": 0.7846153846153846, "overall_precision": 0.7727272727272727, "overall_recall": 0.796875, "positive_target_citation_grounding": 0.5303030303030303, "result": "PASS", "route_test_performed": false, "terminal_outcome": "MEASUREMENT_FAILURE"}
```

`PASS` は測定器の成功ではなく、公開データから固定済みの測定失敗を完全に再現できたことを意味します。

## 完全性確認

```bash
(cd independent_social_expression_v1 && sha256sum -c CHECKSUMS.sha256)
```

`CHECKSUMS.sha256` 自身と生成時刻に依存するmanifestは自己参照を避け、検証対象から除外します。
