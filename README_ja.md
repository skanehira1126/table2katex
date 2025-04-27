# table2katex

CSV・TSV・JSONL形式の表データを、簡単にKaTeXの`\begin{array}`形式に変換するCLIツールです。

---

## 特徴

- CSV、TSV、JSONL形式のテーブルデータをKaTeX用配列フォーマットに変換
- 左寄せ・中央寄せ・右寄せを柔軟に指定可能
- 軽量・シンプルな設計
- Python 3.10以上対応

---

## インストール

```bash
pip install table2katex
```

または [uv](https://github.com/astral-sh/uv) を利用している場合：

```bash
uv sync --dev
```

---

## 使い方

### 基本的な使い方

```bash
table-gen path/to/data.csv
```

指定したCSV/TSV/JSONLファイルを読み込み、KaTeX形式に変換して標準出力に出力します。

### オプション一覧

| オプション | 説明 | デフォルト値 |
|:-----------|:-----|:-------------|
| `--align` | 列の整列方向を指定（例：`c`、または`l:c:r`） | `c` |
| `--file-ext` | ファイル拡張子（`csv`, `tsv`, `jsonl`, `auto`） | `auto` |

#### 使用例

```bash
table-gen examples/sample.tsv --align l:c:r
```

このコマンドはTSVファイルを読み込み、左・中央・右に列を揃えてKaTeX出力します。

---

## 出力例

入力ファイル (`sample.csv`)：

| 名前  | スコア |
|:------|------:|
| Alice | 90    |
| Bob   | 85    |

コマンド例：

```bash
table-gen sample.csv --align l:r
```

出力されるKaTeXコード：

```latex
\begin{array}{l:r}
\textbf{名前} & \textbf{スコア} \\ \hline
Alice & 90 \\
Bob & 85 \\
\end{array}
```

---

## 開発・テスト

リポジトリをクローンし、開発用依存をインストールします：

```bash
uv sync --dev
```

テスト実行：

```bash
tox
```

対応Pythonバージョン：3.10, 3.11, 3.12

### コードフォーマットチェック

```bash
tox -e black
tox -e ruff
```

