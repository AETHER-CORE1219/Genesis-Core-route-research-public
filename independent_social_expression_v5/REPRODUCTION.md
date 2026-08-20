# 公開再現手順

必要環境はPython 3.11、NumPy 2.2.6、GNU `sha256sum`です。repository rootで実行します。

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install 'numpy==2.2.6'
PYTHONDONTWRITEBYTECODE=1 python3 independent_social_expression_v5/scripts/reproduce_v5.py
PYTHONDONTWRITEBYTECODE=1 python3 independent_social_expression_v5/scripts/validate_public_v5_privacy.py
(cd independent_social_expression_v5 && sha256sum -c CHECKSUMS.sha256)
```

`reproduce_v5.py`は匿名313名ledgerから次を再計算します。

- 完全鎖とcarrier-free意味核の曝露・支持・coverage
- 層調整risk difference、HC3区間
- 固定9,999置換p値と統計列SHA
- Manski欠測境界
- 99 decoyの経験的p値
- 事前終端規則

公開projectionには実名、QID、URL、資料本文、引用、出生日時・座標、チャート、private path、匿名ID対応表を含めません。このため、出生図から候補曝露を再生成する完全end-to-end公開ではなく、凍結した匿名曝露・現実state以後の統計再現です。
