# 独立・社会的発現経路研究 v3

## 結論

五つの社会的発現機能は、420名のdevelopment内では311名・109名の両部分群で正方向を示しました。しかし、訂正後portable面と測定誤差を用いた事前検出力監査では、「著作・象徴制作」だけがAKS575で識別可能でした。

結果を見ずに凍結したJyotish 25単位のANY機構群を、未使用575名へ一回適用しました。該当218名・非該当357名のうち、固定資料から著作行為を判定できた該当127名・非該当212名を年代標準化して比較した結果、risk differenceは `-0.02562`、95% bootstrap区間は `[-0.12690, 0.07693]`、五候補Holm補正pは `1.0` でした。

したがって、この集約機構群は人物外再現しませんでした。これは限定されたnullです。

## 何が肯定され、何が肯定されなかったか

肯定されたもの:

- 訂正後matcherのdevelopment420完全parity
- 五機能すべての311名・109名内での正方向
- 訂正後チャート機構面のfresh人物への決定的輸送
- 現実面とチャート面を独立凍結した一回評価

肯定されなかったもの:

- 著作25単位ANY集約の人物外濃縮
- 個別515規則の人物外再現
- 西洋・インド両体系の人物外収束
- 因果関係または職業予測

他の四機能は検出力不足であり、nullではありません。

## 五機能は五本の経路ではない

五機能は詳細経路の上位出力です。訂正後一次確認面には74固有単位があり、機能所属は重複を許して合計83です。今回検証したのは、そのうち著作へ接続するJyotish 25単位をANYで束ねた一つの集約仮説です。

## 起業・政治・ビジネスの位置

人物は非排他的な機能集合として表現します。

- 起業・企業構築: `ORGANIZED_COLLECTIVE_REALIZATION`
- 製品・技術を実装する起業: `TECHNOLOGY_OR_PRODUCT_IMPLEMENTATION`
- 出版・理論・コンテンツ事業: `AUTHORED_SYMBOLIC_PRODUCTION`
- 公益目的の社会起業: `ADVOCACY_OR_PUBLIC_CAUSE_ACTION`
- 政治的運動・代表・交渉: `ADVOCACY_OR_PUBLIC_CAUSE_ACTION`
- 法・行政・統治・制度運用: `RULE_OR_INSTITUTION_OPERATION`
- 政党・行政組織の構築指揮: `ORGANIZED_COLLECTIVE_REALIZATION`

職業名や肩書だけでは付与しません。資本配分、投資、所有、取引、市場形成は現在の11機能rubricに独立機能がなく、今後の発見課題です。

## 再現

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r independent_social_expression_v3/requirements.txt
python independent_social_expression_v3/scripts/reproduce_v3.py
```

詳細は [METHODS.md](METHODS.md)、[CLAIM_BOUNDARY.json](CLAIM_BOUNDARY.json)、[FAILURES_AND_LIMITS.md](FAILURES_AND_LIMITS.md) を参照してください。
