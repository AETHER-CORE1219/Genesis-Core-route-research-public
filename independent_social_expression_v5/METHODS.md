# 方法

## 仮説と解析単位

一次仮説はdevelopment420だけから固定した一つの完全鎖です。解析単位は人物で、職業・分野は候補選択にも現実側陽性ラベルにも使いません。

旧1030名は削除せず、development420、人物分離primary313、source不足secondary60、その他の品質・重複役割237へ分けました。一次解析は候補発見に使っていない313名です。

## 現実側endpoint

一次endpointは、固定資料に本人が競技をplay/compete/race/fightしたこと、またはprofessional athlete、player、footballer、wrestler、boxer、racing driver等の明示的な競技者roleがあることです。coach、administrator、owner、演技上の選手役、宇宙飛行・操縦は一次陽性にしません。

状態は`SUPPORTED`、`NO_DIRECT_ANCHOR_OBSERVED_IN_ADEQUATE_FIXED_SOURCE`、`NO_ANALYSIS_ELIGIBLE_EVIDENCE`、source欠測等を保持します。未判定を陰性へ変換しません。

## 独立固定

チャート曝露面は現実側stateを読まず、現実面はチャート・候補所属を読まずに別々に固定しました。その後に一回だけ人物IDで結合しました。候補、endpoint、閾値、人物、層、decoyは結果後に変更していません。

## 推定

- 出生年代×source collectionの固定層を持つrisk-difference回帰
- HC3 robust standard errorと片側95%区間
- 層内で曝露を9,999回置換する片側検定、seed `20260821`
- 結果blindに固定した99 decoyとの経験的p値
- UNKNOWNを曝露群・非曝露群の両端へ置くManski bound
- 完全鎖と、carrierだけを除いた同一意味核を分離

一次陽性には、正の推定値、HC3片側下限>0、置換p<=0.05、decoy p<=0.05を同時に要求しました。陽性でないことだけをnullとは呼びません。事前参照効果へのpower>=0.80と上限境界を満たす場合だけ限定nullとします。

## 再現範囲

公開bundleは匿名313名ledgerから、一次・二次推定、置換検定、欠測境界、decoy比較、終端判定を再計算します。privateな出生情報、チャート、資料本文から曝露・anchorを再構成するend-to-end再現ではありません。
