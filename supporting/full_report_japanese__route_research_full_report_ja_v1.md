# 発現経路研究 全体報告書 v1

## 0. 文書の位置づけ

- 本文書は、現時点の発現経路研究を外部公開前提で日本語で総括した研究報告書である。
- 本文書の目的は、研究の目的、仮説、方法、データ、反復回数、結果、固定経路、保留群、限界、再現方法、公開時の主張境界を一つにまとめることにある。
- 本文書は「現在どこまで言えるか」を固定するための文書であり、保留群や仮枝を無理に確定扱いしない。
- 現在の公開主張面の基準ファイルは以下である。
  - `route_research_publication_freeze_package_v1.json`
  - `route_research_reproduction_protocol_v1.md`
  - `all_field_unified_route_freeze_registry_v1.json`

## 1. 要旨

- 本研究は、出生データを持つ著名人物群を用い、西洋占星術とインド占星術の両体系から「どのような発現経路が反復するか」を機械抽出と人物単位再読で追跡したものである。
- 第一段階では、著名人物の表での発現が占星術的配置と反復的に一致することを、経路単位の科学的な一致パターンとして発見した。
- 第二段階では、その発見を数百人規模の blind ingress で再監査し、現時点のデータに基づいて正確に発現を記述できる経路だけを固定面に残した。
- 現時点の母集団は `1030名`、そのうち exact-like は `795名`、人物単位で「人物 -> 第1経路 -> 第2経路 -> 西洋配置 -> インド配置」まで追跡できる discovery 台帳は `761名` である。
- 現在、公開主張として固定してよい経路は `16本` である。
- 一方で、固定してはいけないが保持すべきものとして、
  - unified registry 内 non-claim rows `14`
  - science nonfixed rows `16`
  - surviving narrow packet candidate `1`
  - watch packet provisional subbranches `8`
  がある。
- 研究上もっとも重要な結論は、「著名人物には共通して現れやすい可視化圧・身体圧・制度接続圧・象徴化圧があり、それらがまず大きい gate を形成している」可能性が高い、という点である。
- その上で、より細かい違いは、
  - 第2経路
  - 役割軸
  - 西洋の反復特徴
  - インドの lagna / nakshatra lord / kendra 反復
  に落ちている可能性が高い。
- よって本研究は、単一の配置要素から即座に経路を決める立場ではなく、多層照合でのみ経路を残す保守的な立場を取る。
- 研究の構造は明確に二段階である。
  - 第一段階は、既存 publication 台帳 `188 rows / 151 unique people / duplicated_people 37` を母体として、分野ごとの発現経路そのものを見つけ、初期固定群を作る段階である。
  - 第二段階は、その後の publication 外人物投入と mass intake を通じて、既存経路へ数百人単位で blind に流し、太る経路、保留に落ちる束、共通因子、packet 候補を切り分ける段階である。

## 1.1 研究二段階の定義

### 第一段階: 経路発見段階

- 既存 publication 台帳を母体に、どの分野でどの発現経路があるかを見つける段階である。
- この段階の核心は、著名人物の表での発現と占星術的配置の間に、反復して観測できる一致パターンが存在することを確認した点にある。
- この段階の起点として確認された数は以下である。
  - publication rows: `188`
  - unique people: `151`
  - duplicated people: `37`
  - combined chart-fact pool: `280`
  - text-enriched records: `189`
- ここでは、分野ごとの route family / route branch をまず見出し、後の blind ingress に使う inventory を用意した。
- したがって第一段階の結論は、「表での発現は占星術的構造と無秩序に結びついているのではなく、少なくともこの母集団では反復する経路として科学的に追跡できる」という発見である。
- 現在 fixed claim として残っている `16本` は、直接には第二段階の監査を経ているが、起源はこの第一段階の route discovery にある。

### 第二段階: 拡張・検証段階

- 第一段階で得た route inventory を壊さず、publication 外の人物を blind に流して、
  - 既存経路が太るのか
  - 新しい細い束が出るのか
  - shared fame factor が露出するのか
  - science など未固定群が独立 route へ進むのか
  を監査する段階である。
- この段階では、第一段階の発見を誇張せず、現時点の exact 母集団でどこまで正確に発現を記述できるかを検証した。
- この段階の最初の機械準備では、
  - chart-ready だが publication 外の unique people `143`
  - wave1 first queue `100`
  が確認された。
- その後、mass intake を反復し、最終的に
  - master `1030`
  - exact-like `795`
  - discovery `761`
  まで拡張された。
- 現在の「固定 / 保留 / watch / packet candidate」の区分は、この第二段階で形成された。

## 2. 研究目的

- 目的1: 著名人物群に反復する発現経路を見出し、それを分野別の印象論ではなく、出生データと配置反復に基づいて記述すること。
- 目的2: 先に職業分類を置くのではなく、「人物を現在の経路へ blind に流し、その後で何が出たか」を観測する研究設計へ切り替えること。
- 目的3: 西洋占星術だけでもインド占星術だけでもなく、両体系を同時に使ったときに、どの経路が太く、どの束が保留に留まるかを追跡すること。
- 目的4: GitHub 公開、外部投稿、公開議論に耐える透明性と再現性を持つ研究パッケージを作ること。

## 3. 研究仮説

### 3.1 初期仮説

- 仮説A: 著名人物群には、表面的な職業分類より手前に、反復する発現経路が存在する。
- 仮説B: その経路は、西洋側の visible な特徴だけでなく、インド側の lagna・nakshatra・kendra 構造も含めることで安定して読める。
- 仮説C: 同じ職業でも別経路へ流れうるし、逆に別職業でも同じ経路へ流れうる。

### 3.2 研究が進んだ後の修正仮説

- 仮説D: 著名人物にはまず共通する大きな可視化 gate があり、そこへ多数の配置パターンが圧縮される。
- 仮説E: 細い違いは第1経路より第2経路、役割軸、インド側分岐、packet 構造に残る。
- 仮説F: support が高い束ほど真の独立経路とは限らず、むしろ shared fame factor である可能性がある。

## 4. 固定と保留の違い

### 4.1 固定とは何か

- 本研究でいう「固定」は、現在の公開主張面に入れてよい経路である。
- ただしこれは「絶対確定」ではなく、「現時点の exact 母集団、人物再読、両体系照合に耐えたので、現行研究の claim surface として公開してよい」という意味である。
- 言い換えると固定とは、現時点のデータに基づいて、発現をもっとも正確に記述できる公開用手法である。
- したがって固定は、
  - 全人類に適用できる決定論
  - 職業予測器
  - 一要素だけで成立する法則
  ではない。
- 現在の固定経路は `16本` である。

### 4.2 保留とは何か

- 本研究でいう「保留」は、「現時点では公開主張面に入れないが、捨てずに保持する」状態である。
- 保留には複数種類がある。
  - 人数不足で underfilled のもの
  - science 側の clue / holdout candidate
  - shared fame factor とみなすもの
  - 境界束として split signal を保持するもの
  - packet-level の細い候補だが、まだ route へ昇格させないもの
- 保留は失敗ではない。むしろ、現時点で過剰主張を避けるための研究上の安全弁である。

### 4.3 本研究での簡潔な区分

- 固定:
  - 現在 claim してよい route family / route branch
- 保留:
  - 将来の候補
  - 共通因子
  - 境界束
  - underfilled
  - science 側の未確定系

## 5. データ

### 5.1 現在の母集団

- master subjects: `1030`
- exact-like subjects: `795`
- approximate-like subjects: `90`
- date-only-like subjects: `145`
- subject-level discovery traces: `761`

### 5.1.1 第一段階の基礎母集団

- 第一段階で route discovery の母体となった publication 側台帳は、単純な人数ではなく rows ベースで管理されていた。
- そのため、起点は以下のように整理する必要がある。
  - publication rows: `188`
  - publication unique people: `151`
  - duplicated people count: `37`
- したがって、「188名で研究した」という表現は厳密には `188 rows` を指す。
- 人物ベースで言えば `151 unique people` が第一段階の母体である。
- ただし repo 内の進捗・準備台帳ではこの `188 rows` が一貫して初期 publication 台帳として扱われているため、本報告書でも両方を併記する。

### 5.2 現在の分野分布

- master ledger 上の primary field 分布:
  - ARTS `228`
  - SCIENCE_TECH_INVENTION `198`
  - BUSINESS_ENTREPRENEURSHIP `135`
  - SPORTS `129`
  - RELIGION_SPIRITUALITY `82`
  - CRIME_CONTROVERSY_OUTLAWS `59`
  - INSTITUTIONS_POLITICS `59`
  - EXPLORATION_EXTREME_ACHIEVEMENT `51`
  - REVOLUTION_ACTIVISM_IDEOLOGY `45`
  - HUMANITIES `39`
  - PUBLIC_FIGURE_MIXED `5`

### 5.3 discovery ledger 上の分野分布

- subject-level route trace に実際に入っている `761名` の primary field 分布:
  - SCIENCE_TECH_INVENTION `171`
  - ARTS `163`
  - SPORTS `113`
  - BUSINESS_ENTREPRENEURSHIP `111`
  - RELIGION_SPIRITUALITY `60`
  - INSTITUTIONS_POLITICS `42`
  - HUMANITIES `34`
  - REVOLUTION_ACTIVISM_IDEOLOGY `27`
  - EXPLORATION_EXTREME_ACHIEVEMENT `26`
  - CRIME_CONTROVERSY_OUTLAWS `9`
  - PUBLIC_FIGURE_MIXED `5`

### 5.4 データの出所

- 研究で使う出生データは、既存 repo 内 exact chart facts、Astrotheme、Astro-Databank、既存ローカル研究線の再利用群を含む。
- 研究途中で `Wikipedia 混在` が紛れたため、その後は `direct-source` 監査を行い、直系ソースのみの追跡台帳も別に作成した。
- 現在の公開向け出所追跡には以下を使う。
  - `direct_source_publication_manifest_v1.json`
  - `mass_intake_source_backed_exact_round10_v1_source_manifest_v1.json`

### 5.5 人物追跡の単位

- 各人物について以下を保持している。
  - subject_id
  - 人物名
  - primary_field
  - public_description / occupation_raw
  - birth date / time / place / timezone / precision
  - top route / second route
  - western snapshot
  - vedic snapshot
  - biography source URL
  - birth data source URL
  - chart_fact_file
  - scoring_file

## 6. 研究方法

### 6.1 基本方針

- 先に職業で分類してから route を当てにいくのではなく、現在保持している route inventory へ blind に流し、その後で人物の職・功績・役割・記述と照合する。
- blind ingress は「最終分類」ではなく「route pressure observation layer」として扱う。
- 同じ top route に入っただけで固定しない。
- 同じ feature が出たからといって自動昇格しない。
- したがって、現時点での本研究の手法とは、「第一段階で見つかった一致を、第二段階で exact 母集団へ広げつつ、過剰主張を避けて固定面だけを残す多層監査手法」である。

### 6.2 占星術項目

#### 西洋側

- ASC
- MC
- angular planets
- house clusters
- visible houses
- sign placements
- relevant aspects
- `W_...` 形式の抽出特徴

#### インド側

- lagna
- moon nakshatra
- nakshatra lord
- rashi
- kendra / trikona / dusthana
- house-planet repetition
- `V_...` 形式の抽出特徴

### 6.3 scoring の考え方

- 各人物について route inventory 全体に対して score を計算し、
  - top route
  - second route
  を保持する。
- arts / sports 系を含む一部 schema は、西洋特徴とインド特徴の両方に最小命中条件を置いている。
- したがって本研究は最初から `西洋 + インド` の両体系で動いている。

### 6.4 packet とは何か

- packet は次の4つを束ねた観測単位である。
  - top route
  - second route
  - explicit feature bundle
  - subject trace
- ここで重要なのは、packet は route より細かい観測単位であり、すぐに route と同一視しないことにある。

### 6.5 昇格条件

- 高supportだから昇格、ではない。
- 昇格には少なくとも以下を重ねて見る。
  - route traversal の反復
  - subject-level の共通性
  - role-side coherence
  - western repetition
  - vedic repetition
- これらが揃わなければ、support が高くても common factor hold または boundary hold に留める。

## 7. 研究実施履歴

### 7.1 予備段階

- 第一段階で route discovery に使われた publication 母体は `188 rows / 151 unique people` である。
- その後、公開面に触れずに拡張可能性を確定するための preparation を行い、publication 外の chart-ready unique people `143` を確定した。
- current fixed expression paths に対する blind ingress を `143名` に実施。
- 結果:
  - `non_arts_public_symbol = 58`
  - `music_performance_influence = 23`
  - `overlap_or_ambiguous = 1`
  - `no_clear_fixed_path = 61`
- この段階で、当時の固定 path は blind ingress classifier としては弱いことが確認された。

### 7.2 all-field blind ingress

- all-field route inventory 全体を単一入口に統合し、`143名` を投入した。
- candidate_count `143`
- route_count `22`
- open_local_review_queue_count `334`
- ここで blind ingress は自動確定器ではなく、pressure observation layer と定義し直された。

### 7.3 priority audit

- blind ingress の open row をそのまま route expansion に使わず、
  - expansion_priority
  - boundary_noise_first
  - mixed_review_required
  - underfilled_hold
  - capability_only_do_not_field_fix
  に切り分けた。

### 7.4 mass intake rounds と主な母数推移

- ここから先は第二段階、すなわち「第一段階で見つけた route inventory を維持したまま、外部人物を大量投入して検証する段階」である。
- round2 front-half 後:
  - master `155`
  - exact_like `80`
- round2 tail completion 後:
  - master `176`
  - exact_like `83`
  - discovery `48`
- science/business seeded recovery 後:
  - master `200`
  - exact_like `105`
  - discovery `71`
- round4 multi-field supplement 後:
  - master `291`
  - exact_like `150`
  - discovery `116`
- local exact reuse round7 wave1 後:
  - master `759`
  - exact_like `542`
  - discovery `508`
- local exact archive merge 後:
  - master `882`
  - exact_like `647`
  - discovery `613`
- structured public exact round9 後:
  - master `966`
  - exact_like `731`
  - discovery `697`
- source-backed exact round10 後:
  - master `1030`
  - exact_like `795`
  - discovery `761`

### 7.5 packet 監査段階

- observed packet manual reading round1
- observed packet manual reading round2
- explicit feature packet reading round3
- packet role profile audit
- packet multilayer feature audit
- packet evidence stack
- packet resolution layer audit
- watch packet branch split reading

### 7.6 研究の反復回数について

- 大きく言えば、本研究は以下の反復で進んでいる。
  - blind ingress 実験: 2系統
  - mass intake waves: round2, round3 seeded, round4, round7 reuse, round8 archive merge, round9, round10
  - packet manual reading: 3ラウンド
  - packet 補助監査: role / multilayer / evidence / resolution / branch split
- したがって「一度見て終わり」ではなく、母数増加と再監査を何段も重ねた研究である。

## 8. 現在の主要結果

### 8.1 route cluster と packet 状態

- observed route clusters: `16`
- packet review count: `43`
- explicit feature packet count: `17`
- surviving narrow packet candidate: `1`
- watch packet count: `9`
- watch packet provisional subbranches: `8`

### 8.2 packet resolution class

- surviving_narrow_candidate: `1`
- thick_packet_likely_common_factor_or_family: `4`
- multi_output_family_not_single_route_yet: `2`
- coarse_western_gate_with_large_internal_diversity: `1`
- watch_packet_needing_manual_reading: `9`

### 8.3 current top route pressure

- discovery ledger 上の top route counts 上位:
  - `sports_pressure_friction_core`: `117`
  - `religion_institution_doctrine_reform_frozen_v1`: `115`
  - `arts_venus_aesthetic_body`: `98`
  - `arts_symbolic_pressure_expression`: `72`
  - `institutions_core_governance_frozen_v1`: `70`
  - `religion_public_teacher_healer_media_frozen_v1`: `46`
  - `public_figure_media_presenter_frozen_v1`: `42`

### 8.4 解釈

- 上位に太っているものが、そのまま独立経路とは限らない。
- むしろ最上位層の多くは、
  - 身体圧
  - 可視化圧
  - 様式化圧
  - 制度近接圧
  - 象徴化圧
  として読む方が整合的である。

## 9. 現在固定している発現経路 16本

### 9.1 人文

- `humanities_critique_interpreter_frozen_v1`
  - support `7 / 13`
  - 文化・テキスト・思想の批評的解釈が中心
- `humanities_public_translation_frozen_v1`
  - support `3 / 13`
  - 難しい知や隠れた内容を公的な解釈へ翻訳する

### 9.2 制度政治

- `institutions_core_governance_frozen_v1`
  - support `11 / 25`
  - 正式な役職、統治、制度処理が中心
- `institutions_reform_execution_frozen_v1`
  - support `3 / 25`
  - 改革圧・思想圧が正式権力を通って出る
- `institutions_statecraft_diplomacy_frozen_v1`
  - support `6 / 25`
  - 国家運営・外交・執行型国家技術

### 9.3 public figure mixed

- `public_figure_coercive_notoriety_frozen_v1`
  - support `3 / 22`
  - 反復的な強制・暴力性が public recognition へ出る
- `public_figure_media_presenter_frozen_v1`
  - support `7 / 22`
  - 公的提示、司会、ホスト、媒体化が中心
- `public_figure_visibility_body_frozen_v1`
  - support `3 / 22`
  - 身体・外見・可視イメージが public role の中心

### 9.4 革命運動

- `revolution_rights_movement_speech_frozen_v1`
  - support `4 / 6`
  - 権利闘争、運動象徴、対立、発話が重なる

### 9.5 宗教霊性

- `religion_public_teacher_healer_media_frozen_v1`
  - support `12 / 29`
  - 公的教師、癒し手、媒体化された霊的伝達
- `religion_institution_doctrine_reform_frozen_v1`
  - support `7 / 29`
  - 制度・教義・改革権威
- `religion_mystic_writer_channel_symbol_frozen_v1`
  - support `5 / 29`
  - 神秘的著述、チャネリング、象徴教義
- `religion_evangelical_preacher_movement_frozen_v1`
  - support `4 / 29`
  - 説教、運動、放送型 revival

### 9.6 探検・極限

- `exploration_aerospace_technical_boundary_core_frozen_v1`
  - support `15 / 20`
  - 航空・宇宙・技術境界の shared core
- `exploration_survival_nature_frozen_v1`
  - support `5 / 20`
  - 生存、自然没入、環境持久
- `exploration_risk_body_frozen_v1`
  - support `6 / 20`
  - 身体リスク、閾値耐性、極限身体行為

## 10. 固定していない unified non-claim rows 14本

- HUMANITIES
  - `humanities_testimony_writer`
  - `humanities_writer_symbolic`
- INSTITUTIONS_POLITICS
  - `institutions_executive_power_operator`
  - `institutions_legislative_operator`
- PUBLIC_FIGURE_MIXED
  - `public_figure_coercive_power`
  - `public_figure_coercive_symbol`
  - `public_figure_presenter_teacher`
  - `public_figure_symbolic_controversy`
  - `public_figure_visibility_style`
- REVOLUTION_ACTIVISM_IDEOLOGY
  - `revolution_collective_organizer`
- BUSINESS_ENTREPRENEURSHIP
  - `business_creative_media_market_holdout_frozen_v1`
- SCIENCE_TECH_INVENTION
  - `science_theory_observation_cosmos_holdout_frozen_v1`
- ARTS
  - `arts_lyric_symbolic_story`
- SPORTS
  - `sports_public_competitive_identity`

### 10.1 これらを固定しない理由

- support 不足
- field 母集団不足
- capability overlay 的性格
- shared fame factor との混線
- holdout 候補であって再現証明ではない

## 11. science 側 nonfixed rows 16本

### 11.1 status 分布

- `NOT_FIXED_RETAIN_AS_CLUE_OR_SUBBRANCH`: `5`
- `MOTHER_COHORT_UNDERFILLED_RETAIN_AUXILIARY_COLLECTION_ONLY`: `2`
- `MOTHER_COHORT_SUPPORTED_HOLDOUT_CANDIDATE_NOT_CONFIRMED`: `1`
- `UNDERFILLED_RETAINED_NOT_FROZEN_AS_ROUTE`: `3`
- `HOLDOUT_READY_SUBBRANCH`: `1`
- `CONTEXT_ONLY`: `1`
- `UNDERFILLED_RETAINED_NOT_FINAL`: `3`

### 11.2 代表的な science 非固定群

- `science_theory_observation_cosmos_round15_freeze`
  - 母コホート clean `22`
  - かなり有望だが、独立 holdout と leakage control が未完のため未固定
- `science_experimental_lab_biomed_round15_freeze`
  - 実験室・生物医学・化学反応
  - mother clean `10`
  - underfilled のため未固定
- `science_invention_engineering_after_round12_freeze`
  - 発明・工学・装置化
  - mother clean `12`
  - underfilled のため未固定
- `science_computing_information_round9_freeze_reviewed`
  - 計算・情報構造
  - 情報処理能力と出力枝の重なりが強く、単一 route としては未固定

### 11.3 解釈

- science 側は「存在しない」のではなく、「候補はあるが、公開主張面に入れるにはまだ早い」が正しい。
- 研究としては保持すべきだが、論文や GitHub 公開で fixed と書いてはいけない。

## 12. packet-level の現在地

### 12.1 surviving narrow packet candidate

- 現在、packet-level で生き残っている候補は `1本` のみである。
- packet:
  - top route: `religion_institution_doctrine_reform_frozen_v1`
  - second route: `religion_public_teacher_healer_media_frozen_v1`
  - features:
    - `W_angular_Mercury`
    - `W_angular_density_2plus`
    - `W_house_cluster_H6`
    - `W_pressure_house_density_3plus`
- working commonality:
  - `public explanation that becomes a system, method, or teachable doctrine`

### 12.2 strict core

- strict core `4`
- strong partial fit `3`
- weak partial fit `1`
- 現在の判断:
  - `provisional_packet_candidate_survives_with_boundary`

### 12.3 core subjects

- Bob Dylan
- Clint Eastwood
- Peter Lynch
- Sigmund Freud

### 12.4 なぜ route に昇格しないのか

- 同じ feature bundle が別 second route にも現れるため、`Mercury/H6/pressure` だけで packet を定義すると危険だからである。
- したがって second route context が必要であり、まだ route claim へ上げない。

## 13. watch packet 仮枝 8本

### 13.1 現在の状態

- watch packet count: `9`
- provisional subbranch count: `8`

### 13.2 split signal

- role split strong: `2`
- vedic split strong: `4`
- vedic split moderate: `2`

### 13.3 何を意味するか

- これは「新経路が8本見つかった」という意味ではない。
- 正しくは、「同じ visible gate の下で、role か vedic 側へ枝分かれの signal が出ている」という意味である。
- ここは研究二段階目で詰める領域であり、現段階では主張しない。

## 14. なぜ違いが出にくいのか

### 14.1 確認済み結果

- support の高い束の多くは、独立 route ではなく、common factor または family に見える。
- 明示特徴 packet `17本` を見ても、
  - 真に narrow candidate として残るのは `1本`
  - 他は太い共通因子、内部多様性、watch 状態
  に散った。

### 14.2 現時点のもっとも強い解釈

- 有名人には共通する大きな visible gate がある。
- その gate には、
  - 可視化
  - 身体性
  - 様式化
  - 制度接続
  - 象徴化
  が含まれる可能性が高い。
- そのため、何億通りもの配置がまず大きな gate に圧縮されて見える。

### 14.3 その下で差が出る層

- 第2経路
- 役割軸
- vedic lagna
- moon nakshatra lord
- kendra 反復

### 14.4 今はまだ入れていないが将来候補の層

- shadbala
- divisional charts
- より細かいインド側強度指標

### 14.5 注意

- ただし現段階では、これらを入れないと何も見えないわけではない。
- まずは現在の route layer を固定し、その後に第二段階として deeper split を行うのが研究順序として適切である。

## 15. 研究上の革新性

- 職業ラベル先行ではなく、blind ingress 後に読む構造へ切り替えた点。
- 高supportだから昇格、ではなく、
  - 高supportでも保留
  - 低supportでも explicit feature と人物共通性が揃えば候補化
  という非対称ルールを採用した点。
- 西洋とインドの両体系を最初から同時に scoring し、その後 packet-level でも full chart から再監査した点。
- route と packet を分け、
  - route family / branch
  - packet candidate
  - shared fame factor
  - watch subbranch
  を階層化した点。
- 研究を「何でも枝を増やす作業」から、「主張してよい面と保留面を分離する作業」へ変えた点。

## 16. 限界

- 著名人物研究であるため、一般人口研究ではない。
- source exhaustion により、新規 exact 取得線が分野により枯れやすい。
- science 側は候補が厚くても、独立 holdout と leakage control が不足している部分が残る。
- top route はあくまで pressure observation であり、人物の全存在を一経路に還元するものではない。
- packet 候補 `1本` は有望だが、まだ route claim にしてはいけない。

## 17. 現在の公開主張境界

- 公開してよい:
  - fixed route claims `16`
  - 母集団と再現手順
  - blind ingress を pressure observation とする立場
  - packet/hold/watch の区分
- 公開してはいけない:
  - science 非固定群を確定 route として書くこと
  - surviving narrow packet を fixed route として書くこと
  - watch subbranches を新経路として書くこと
  - blind ingress の top route を最終ラベルとして書くこと

## 18. 再現方法

- 現在の再現順は `route_research_reproduction_protocol_v1.md` に固定済みである。
- コマンド順は 15 本あり、最後に publication freeze package を再生成する。
- 最低限必要な主要出力:
  - `all_field_unified_route_freeze_registry_v1.json`
  - `science_route_family_freeze_registry_v2.csv`
  - `route_mass_intake_master_ledger_v1.json`
  - `mass_route_discovery_ledger_v1.json`
  - `observed_route_signature_clusters_v1.json`
  - `observed_packet_review_ledger_v1.json`
  - `explicit_feature_packet_queue_v1.json`
  - `packet_resolution_layer_audit_v1.json`
  - `watch_packet_provisional_subbranch_registry_v1.json`
  - `route_research_publication_freeze_package_v1.json`

## 19. 研究として現時点で言えること

### 19.1 確認済み

- 全分野で完全に何もない状態ではない。
- 現在、公開主張面として固定可能な経路は `16本` ある。
- 人数を増やしても新経路が無限に乱立するわけではなかった。
- むしろ著名人物の可視化共通因子が太る傾向が明確になった。
- それでも narrow candidate `1本` は潰れずに残っている。

### 19.2 推測

- 著名人物には有名化の共通 gate がある可能性が高い。
- 細い差はより下位の層、特に second route と vedic split に落ちている可能性が高い。
- science 側は route 不在ではなく、独立証明の不足により未固定である可能性が高い。

## 20. 固定経路の二段階整理

- 固定 `16本` については、第一段階の発見根拠と第二段階の大量投入後の生存状況を別付録に分離した。
- 付録:
  - `route_research_fixed_route_stage_history_appendix_ja_v1.json`
  - `route_research_fixed_route_stage_history_appendix_ja_v1.md`
- 短い公開向け要約:
  - `route_research_fixed_route_public_summary_ja_v1.json`
  - `route_research_fixed_route_public_summary_ja_v1.md`
- この付録では各経路について、
  - 第一段階:
    - publication `188 rows / 151 unique people` を母体に、support / field universe でどう見つかったか
  - 第二段階:
    - mass intake 後に top / second route として何回反復したか
    - どの分野へ広がったか
    - 大量投入後にどう振る舞ったか
  を並べている。
- これにより、「どこで見つかり、後でどう生き残ったか」が、経路単位で直接追える。

## 21. 次の計画

- 研究二段階目の deeper split にはまだ入らない。
- まず現在の固定研究を公開可能形に整える。
- 次にやることは以下である。
  - 固定 `16本` それぞれについて、公開文面用の短い説明版を整備する
  - 日本語レポートと英語 package の対応を明確にする
  - GitHub 公開時の claim / non-claim 境界を明文化する
  - 公開後の議論で誤読されやすい `shared fame factor` と `fixed route` の違いを先回りして説明する

## 22. 関連ファイル

- 現在の固定境界:
  - `route_research_publication_freeze_package_v1.json`
  - `route_research_publication_freeze_package_v1.md`
- 再現手順:
  - `route_research_reproduction_protocol_v1.md`
- 公開入口:
  - `route_research_public_release_readme_v1.md`
- 統合索引:
  - `mass_route_research_compact_index_v1.json`
- 固定経路一覧:
  - `all_field_unified_route_freeze_registry_v1.json`
- 固定経路の二段階整理:
  - `route_research_fixed_route_stage_history_appendix_ja_v1.json`
  - `route_research_fixed_route_stage_history_appendix_ja_v1.md`
- 固定経路の短い公開要約:
  - `route_research_fixed_route_public_summary_ja_v1.json`
  - `route_research_fixed_route_public_summary_ja_v1.md`
- science 非固定群:
  - `science_route_family_freeze_registry_v2.csv`
- 母集団台帳:
  - `route_mass_intake_master_ledger_v1.json`
- 人物追跡:
  - `mass_route_discovery_ledger_v1.json`
- packet 関連:
  - `observed_packet_review_ledger_v1.json`
  - `explicit_feature_packet_queue_v1.json`
  - `provisional_packet_candidate_ledger_v1.json`
  - `packet_resolution_layer_audit_v1.json`
  - `watch_packet_provisional_subbranch_registry_v1.json`
