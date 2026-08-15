# 再現手順

Python 3.10以降だけを使用します。リポジトリ直下で実行してください。

```bash
python3 independent_social_expression_v2/scripts/reproduce_v2.py
(cd independent_social_expression_v2 && sha256sum -c CHECKSUMS.sha256)
```

検証器は匿名420名matrixと固定515規則から五候補の全体・311/109部分群の予測数、支持数、支持率、基礎率、方向を再計算します。また公開countからactor precision、coverage、linked recallと終端を再計算します。

出力 `result=PASS` はファイルと算術と主張境界の再現を意味します。人物外経路検証のPASSではありません。
