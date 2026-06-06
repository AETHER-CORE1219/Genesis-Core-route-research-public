# Route Research Master Next Plan JA v1

## 1. この計画の位置づけ

- 本計画は、現在の発現経路研究を
  - まず公開可能な固定研究として確定させる段階
  - その後に deeper split と追加サンプルで次段研究へ入る段階
  の二層に分けて整理した総合計画である。
- 研究順序は崩さない。まず現行 route layer を固定し、外部公開・再現・批判耐性を整え、その後に細分化研究へ入る。
- 固定面を勝手に増やさない。現在の fixed 16 を公開 claim surface とし、それ以外は hold / non-claim / provisional のまま扱う。

## 2. 現在の確定状態

- 第一段階:
  - publication 台帳 `188 rows / 151 unique people / duplicated 37`
  - ここで各分野の発現経路を発見し、初期 inventory を形成した。
- 第二段階:
  - publication 外人物の blind ingress と mass intake を反復
  - 現在値は `master 1030 / exact-like 795 / discovery 761`
- 現在の主張境界:
  - fixed routes `16`
  - unified non-claim `14`
  - science nonfixed `16`
  - narrow provisional packet `1`
  - watch subbranch `8`
- 公開パッケージ:
  - materialized release bundle あり
  - top-level file 群あり
  - supporting file 群 `36`
  - readiness check で `all_top_level_present = True`

## 3. 最終目的

- 目的1:
  - 現在の route research を、GitHub 公開、外部投稿、第三者再読に耐える形で確定させる。
- 目的2:
  - 「何を主張してよいか」と「まだ主張してはいけないか」を明確に分離したまま公開する。
- 目的3:
  - 公開後も同じ方法で exact 人物を追加し、将来的に 4 桁規模まで一貫した研究として伸ばせる基盤を維持する。
- 目的4:
  - 第二段階以降の deeper split、インド側分岐、将来的な shadbala / divisional 導入を、現行 fixed layer を壊さずに行えるようにする。

## 4. 絶対に崩さない研究ルール

- fixed 16 を、追加の印象や少数例で勝手に増減させない。
- hold / non-claim / provisional を、公開文面で route claim のように書かない。
- 西洋だけ、インドだけの単層説明で押し切らない。両体系照合を前提にする。
- blind ingress は分類結果ではなく pressure / observation として扱う。
- 追加人物は重複を絶対に避ける。
- exact 時刻の扱いと source trace を必ず残す。
- 追加研究は常に
  - source
  - intake
  - trace
  - route pressure
  - manual reread
  の順に追跡できる状態で残す。

## 5. 全体計画

### Phase A. 公開固定面の最終凍結

- 目的:
  - 現在の fixed / hold / non-claim 境界を、公開基準として最終固定する。
- 作業:
  - fixed 16 の route description を最終確認
  - stage1 / stage2 の説明差分を確認
  - release bundle と canonical docs の齟齬をゼロにする
  - claim boundary と appendix の代表例を再確認
- 完了条件:
  - 固定経路本文、付録、公開 summary、claim boundary が相互整合
  - README、REPORT、APPENDIX、BOUNDARY の数字が一致

### Phase B. 公開実行準備

- 目的:
  - repo の外へ出すときに必要な front-door 資料を揃える。
- 作業:
  - GitHub 用 release folder をそのまま使える状態に保つ
  - 公開順を `README -> REPORT -> SUMMARY -> CLAIM_BOUNDARY -> REPRODUCTION -> APPENDIX` に固定
  - 外部投稿文面を、短文版 / 長文版 / 形式研究版に分けて保持
  - criticism 対応用に、誤読されやすい論点を FAQ 化
- 完了条件:
  - 第三者が release folder を読めば
    - 研究目的
    - 二段階構造
    - データ規模
    - fixed / hold 境界
    - 再現手順
    を順に追える

### Phase C. 再現性監査

- 目的:
  - 「読める」だけでなく「作り直せる」状態にする。
- 作業:
  - reproduction protocol のコマンド順を再実行
  - build script 群が現在の release bundle を再生成できるか確認
  - 主要台帳の依存関係を一覧化
  - raw / review / release の三層構造を維持
- 完了条件:
  - 第三者が repo 内 script 群から同じ release surface を再構成できる
  - readiness check が再度通る

### Phase D. 外部公開

- 目的:
  - 研究を外部に出し、後続の検証入口を作る。
- 作業:
  - GitHub に release bundle を公開
  - Reddit 等に short / long posting を展開
  - 必要なら formal な研究機関向け説明文へ変換
  - 公開時には fixed 16 のみを主張
  - hold / non-claim / provisional は future work として明示
- 完了条件:
  - 公開先ごとに claim surface がぶれない
  - どこに出しても fixed / hold 境界が同じ

### Phase E. 公開後の防御と訂正

- 目的:
  - 誤読、過剰解釈、雑な反論で研究面が崩れないようにする。
- 作業:
  - よくある誤読を 3 群に分ける
    - 占星術全否定型
    - なんでも経路化していると誤解する型
    - fixed 以外も claim していると誤解する型
  - 返答テンプレートを維持
  - 反論で崩れた箇所があれば fixed ではなく文面を直す
- 完了条件:
  - 研究の主張境界が守られる
  - 反論対応で fixed route inventory を不用意に動かさない

### Phase F. 第二次データ拡張

- 目的:
  - 現在の route layer を壊さず、同じ方法で 4 桁規模まで exact 人物を伸ばす。
- 作業:
  - 既存の収集方法で未処理の exact 人物を追加
  - source trace を保持
  - 分野ごとにまとめて intake
  - blind に流し、既存 route へどう乗るかだけをまず観測
  - 新規人物は
    - duplicate check
    - chart facts
    - route trace
    - discovery ledger
    の順で追加
- 完了条件:
  - 追加人数が増えても fixed 16 の大枠が崩れない
  - 本当に新しい反復が出るまで新 route は claim しない

### Phase G. 保留面の再評価

- 目的:
  - hold / non-claim / provisional のうち、どれが本当に昇格余地を持つかを見直す。
- 作業:
  - unified non-claim 14 を再度 cross-field と subject trace で監査
  - science nonfixed 16 を、science 専用ではなく route pressure 側から見直す
  - narrow provisional packet 1 を strict core で監視
  - watch subbranch 8 は route claim にせず internal split signal として維持
- 完了条件:
  - hold 面の扱いが明文化され続ける
  - 昇格条件が曖昧にならない

### Phase H. 第三段階研究

- 目的:
  - 同じ visible gate の内部差を deeper split として研究する。
- 作業:
  - role axis
  - second route
  - vedic lagna
  - nakshatra lord
  を優先して見る
  - それでも潰れる場合に限って shadbala / divisional を入れる
- 前提:
  - これは現行 route layer 固定後に始める
  - 公開 claim surface とは分離する
- 完了条件:
  - deeper split が fixed route の上位層を壊さずに追加できる

## 6. 直近の実行順

1. 現在の release bundle を公開基準の単一入口として使う。
2. GitHub / 外部投稿 / 研究説明文で、fixed 16 以外を claim しない。
3. 公開後は exact 新規人物の追加 intake を再開する。
4. 追加人物はまず既存 route へ blind ingress で流し、厚みと共通因子を監視する。
5. narrow provisional と watch subbranch は、新しい exact 反復が出た場合のみ再評価する。
6. 人数がさらに増えた後に、deeper split を第三段階研究として開始する。

## 7. 実務上の優先順位

- 最優先:
  - claim surface の維持
  - 再現性
  - source trace
- 次点:
  - exact 人物の追加
  - hold 面の監視
- 後順位:
  - shadbala / divisional
  - deeper split の正式命名

## 8. この計画の出口

- この計画の第一出口は、現在の release bundle がそのまま外部公開されること。
- 第二出口は、公開後も同じ ledger / trace / audit 方式で人物追加を続けられること。
- 第三出口は、4 桁規模まで到達した時点でも、fixed layer と deeper split layer が混線しないこと。
