# 再現手順

リポジトリrootで次を実行します。

```bash
python3 -m pip install -r independent_social_expression_v7/requirements.txt
PYTHONDONTWRITEBYTECODE=1 python3 independent_social_expression_v7/scripts/reproduce_v7.py
PYTHONDONTWRITEBYTECODE=1 python3 independent_social_expression_v7/scripts/validate_public_v7_privacy.py
(cd independent_social_expression_v7 && sha256sum -c CHECKSUMS.sha256)
```

`reproduce_v7.py`は匿名420名matrixから、次を再計算して`RESULTS.json`と照合します。

- M0→M3のrisk differenceとHC3標準誤差
- 年代層、主要測定形態、収集元一つ抜き、311/109観測機会の方向判定
- 年代内・収集元内の各9,999回置換
- 固定22面の9,999回person-package maxT
- 7,634 adversarial decoy行と708一意曝露集合
- Western-only、Jyotish-only、fullの比較

匿名`analysis_order`は乱数割当の再現だけに使います。人物identityへの対応表は作成・保存していません。
