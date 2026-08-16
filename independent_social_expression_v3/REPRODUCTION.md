# 再現手順

必要環境はPython 3.11とNumPy 2.2.6です。

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r independent_social_expression_v3/requirements.txt
python independent_social_expression_v3/scripts/reproduce_v3.py
sha256sum -c independent_social_expression_v3/CHECKSUMS.sha256
```

再現器は匿名575名ledgerから、人物集合、25単位manifest、年代別群数、解析可能数、年代標準化差、200,000回の層内null、cluster感度、Holm補正値を再生成します。

この公開再現は統計面と匿名候補所属面を対象とします。出生情報から完全チャート意味グラフを再計算するprivate source snapshotは公開していません。その制限は `CLAIM_BOUNDARY.json` に固定しています。
