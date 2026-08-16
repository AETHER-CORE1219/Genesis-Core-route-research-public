# 方法

## 固定された比較

- 人物集合: 一回限りのAKS575
- チャート側: 訂正後Jyotish primary candidate 25単位のANY一致
- 現実側: 固定Wikipedia revisionに記録された本人の著作・象徴制作行為
- 状態: `SUPPORTED` / `ABSENT` を解析し、`UNADJUDICATED` は陰性へ変換しない
- 単位: 人物
- 層: `BEFORE_1900`, `1900_1949`, `1950_1974`, `1975_OR_LATER`
- estimand: 固定AKS575年代構成で標準化した該当群と非該当群のrisk difference
- null: 年代層内のconditional hypergeometric permutation 200,000回
- 感度: variance multiplier 1.1
- 多重性: 元の固定五候補を保持したHolm補正
- 最小支持: 該当解析可能20名、非該当解析可能50名、各年代層の両群1名以上

## 分離

現実側測定はチャート・候補所属を見ずに先に凍結しました。チャート側所属は現実状態を見ずに別途凍結しました。人物集合の完全一致を確認した後、一度だけ結合しました。

## 旧515規則との関係

v2で公開した515規則はdevelopment上の発見registryです。後続のportable parity監査で旧741面のfresh直接利用が禁止されたため、v3は420/420 parityを通過した訂正後matcherの25単位を使用しています。
