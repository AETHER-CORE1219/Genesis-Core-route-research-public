### Standalone Reproduction Instructions

This update provides a self-contained reproduction script that re-executes historical rule selection, cluster-conditioned permutation baselines (999 runs), training-only candidate selection across 5 folds, and selection-inclusive permutation tests (199 runs) using pre-extracted incidence inputs. It relies strictly on the Python standard library.

From the repository root, run:
```bash
python research_update_20261101/scripts/reproduce.py
```

**Scope of Reproduction:**
- **Input Data**: Loads `data/historical_selection_input.json.gz` and `data/repaired_chain_input.json.gz` (anonymized incidence matrices; excludes raw birth dates, times, locations, personal names, and identity mappings).
- **Verification**: Automatically compares runtime outputs against pre-computed values in `EXPECTED_REPLAY_RESULTS.json`.
- **Boundary**: Replays the mechanical rule selection procedures, permutation baselines, and cross-validation mechanics; it does not perform end-to-end chart calculation from raw historical records.

### スタンドアロン再現実行手順

本アップデートには、事前に抽出・匿名化された接続行列を入力として、過去の規則選択、資料群条件付き置換対照（999回）、5分割における訓練フォールド限定候補選択、および選択を含む置換検定（199回）を再実行するスクリプトが含まれています。Python標準ライブラリのみで動作し、外部パッケージは不要です。

リポジトリルートから以下を実行してください：
```bash
python research_update_20261101/scripts/reproduce.py
```

**再現の範囲と仕様：**
- **入力データ**：`data/historical_selection_input.json.gz` および `data/repaired_chain_input.json.gz` を読み込みます（匿名化された接続行列であり、生年月日・時刻・出生地・氏名・内部ID対応表は含まれません）。
- **検証機能**：実行結果を `EXPECTED_REPLAY_RESULTS.json` に記録された数値と自動照合します。
- **再現範囲の境界**：ルール選択アルゴリズムの機械的挙動、置換基準、および交差検証の計算プロセスを再現するものであり、生の出生記録から天体位置やチャートグラフを再計算する工程とは区別されます。
