# 公開再現手順

## 必要環境

- Python 3.11
- NumPy 2.2.6
- GNU `sha256sum`

repository rootで次を実行します。

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install 'numpy==2.2.6'
PYTHONDONTWRITEBYTECODE=1 python3 independent_social_expression_v4/scripts/reproduce_v4.py
PYTHONDONTWRITEBYTECODE=1 python3 independent_social_expression_v4/scripts/validate_public_v4_privacy.py
(cd independent_social_expression_v4 && sha256sum -c CHECKSUMS.sha256)
```

`PYTHONDONTWRITEBYTECODE=1` は、再現時にbundle内へ `__pycache__` を生成しないために指定しています。checksumは `independent_social_expression_v4/` を基準にした相対pathなので、上記のようにdirectoryを移して検証します。

## 入力

- `RESULTS.json`: 正本統計量と終端判定
- `data/confirmation1457_anonymous_primary_v4.json`: 匿名一次人物ledger、schema `INDEPENDENT_SOCIAL_EXPRESSION_PRIMARY_LEDGER_V4`
- `data/primary_permutation_draws_v4.json.gz`: 9,999固定置換統計量、schema `INDEPENDENT_SOCIAL_EXPRESSION_PERMUTATION_DRAWS_V4`
- `data/decoy_summary_v4.json`: 98 decoyの集約結果

匿名ledgerの各行は、unlinkableなrelease ID、family exposure、固定層、endpoint stateだけを持ちます。本人identity、source本文、出生情報、chart、private pathは含みません。

## 再生成するもの

`scripts/reproduce_v4.py` は公開入力から少なくとも次を再計算し、`RESULTS.json` と一致することを確認します。

- 1,457名の人物集合と該当・非該当人数
- endpoint state、decided数、group coverage
- 35/58対739/1,378の支持数
- 24 estimable strataと1,221 retained people
- 層固定効果・調和重みrisk difference
- HC3 standard errorとone-sided 95% bounds
- 固定9,999置換統計量からの片側p値
- 98 decoyの経験的p値
- Manski missingness bounds
- `delta_ref` への条件付きpowerとMDE
- 事前優先順位による `ADEQUATELY_POWERED_PRIMARY_NULL`

## Privacy検査

`scripts/validate_public_v4_privacy.py` は、公開projectionに次が含まれないことを検査します。

- 実名、QID、Wikipedia URL、identity mapping
- source本文・引用本文
- 出生日時・座標・chart特徴
- private absolute path、private artifact名、shuffle seed
- row-level decoy vectors、shared-page secondary、structural unknown

この検査は匿名性を数学的に保証するものではありません。公開schemaと禁止fieldに対する決定的なrelease検査です。

## 再現境界

公開bundleが再現するのは、凍結済み匿名人物所属とendpointから先の統計解析、null、sensitivity、終端判定です。private source snapshot、出生情報、完全chart意味グラフ、人物とrelease IDの対応は公開していないため、出生情報からfamily exposureを再生成するend-to-end再現ではありません。

期待する成功条件は、二つのPython commandがexit code 0となり、`sha256sum -c` が全対象で `OK` を返すことです。いずれかが失敗した場合は、公開結果を再現済みと扱わないでください。
