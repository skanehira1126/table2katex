import pandas as pd

from table2katex.gen import make_katex_table


def test_make_katex_table_default_align():
    df = pd.DataFrame(
        {
            "A": [1, 2],
            "B": [3, 4],
        }
    )

    output = make_katex_table(df)

    for fragment in [
        r"\begin{array}{l:l}",
        r"\textbf{A} & \textbf{B} \\ \hline",
        r"1 & 3 \\",
        r"2 & 4 \\",
        r"\end{array}",
    ]:
        assert fragment in output


def test_make_katex_table_custom_align():
    df = pd.DataFrame(
        {
            "Name": ["Alice", "Bob"],
            "Score": [90, 85],
        }
    )

    output = make_katex_table(df, column_alignment=["l", "r"])

    assert r"\begin{array}{l:r}" in output
    assert r"\textbf{Name} & \textbf{Score}" in output
    assert r"Alice & 90" in output
    assert r"Bob & 85" in output


def test_make_katex_table_note_mode():
    df = pd.DataFrame(
        {
            "商品": ["りんご", "みかん"],
            "価格": [200, 100],
        }
    )

    # 通常出力
    output_normal = make_katex_table(df)

    # note向けにバックスラッシュ置換
    output_note = output_normal.replace(r"\\", r"\\\\")  # CLIの挙動を再現！

    # 通常版はバックスラッシュ2個連続ではない
    assert r"\\\\" not in output_normal

    # note版はバックスラッシュ2個連続になっている
    assert r"\\\\" in output_note
