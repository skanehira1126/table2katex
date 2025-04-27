# table2katex

A simple CLI tool to convert tabular data (CSV, TSV, JSONL) into KaTeX array format.

---

## Features

- Convert tables (CSV, TSV, JSONL) into KaTeX `\begin{array}` format
- Flexible column alignment (left, center, right)
- Lightweight and easy to use
- Compatible with Python 3.10+

---

## Installation

```bash
pip install table2katex
```

or, if using [uv](https://github.com/astral-sh/uv):

```bash
uv sync --dev
```

---

## Usage

### Basic command

```bash
table-gen path/to/data.csv
```

This will print the KaTeX array format to standard output.

### Options

| Option | Description | Default |
|:-------|:------------|:--------|
| `--align` | Column alignment(s). Example: `c` or `l:c:r` | `c` |
| `--file-ext` | Input file extension (`csv`, `tsv`, `jsonl`, or `auto`) | `auto` |

#### Example

```bash
table-gen examples/sample.tsv --align l:c:r
```

This will treat the file as a TSV and format columns as Left, Center, Right aligned.

---

## Example Output

Input (`sample.csv`):

| Name  | Score |
|:------|------:|
| Alice | 90    |
| Bob   | 85    |

Command:

```bash
table-gen sample.csv --align l:r
```

Output:

```latex
\begin{array}{l:r}
\textbf{Name} & \textbf{Score} \\ \hline
Alice & 90 \\
Bob & 85 \\
\end{array}
```

---

## Development

Clone the repository and install dependencies:

```bash
uv sync --dev
```

Run tests:

```bash
tox
```

Supported Python versions: 3.10, 3.11, 3.12

### Formatting and Linting

```bash
tox -e black
tox -e ruff
```
