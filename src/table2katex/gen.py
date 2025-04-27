from collections.abc import Sequence

import pandas as pd


def make_katex_table(
    df: pd.DataFrame,
    column_alignment: str | Sequence[str] = "l",
    for_note: bool = False,
) -> str:
    """
    Convert pandas DataFrame to KaTeX array string.

    Args:
        df (pd.DataFrame): Table data to convert.
        column_alignment (str | Sequence[str], optional):
            Column alignment(s) for each column.
            Either a single alignment character ('l', 'c', 'r')
            or a sequence matching the number of columns.
        for_note (bool, optional):
            Adjust KaTeX output for note.com (double backslashes).

    Returns:
        str: A KaTeX array string representing the table.
    """
    if for_note:
        new_line = r" \\\\ "
    else:
        new_line = r" \\ "
    # Fill missing values and convert all entries to string
    df = df.fillna("").astype(str)

    # Validate and build column alignment specifier
    # (KaTeX requires alignment specification matching number of columns)
    if isinstance(column_alignment, str):
        align_spec = ":".join([column_alignment for _ in df.columns])
    elif isinstance(column_alignment, Sequence):
        if len(df.columns) != len(column_alignment):
            raise ValueError("The length mismatch ...")
        align_spec = ":".join(column_alignment)
    else:
        raise TypeError("")

    header = rf"\begin{{array}}{{{align_spec}}}" + "\n"
    columns = (
        " & ".join(r"\textbf{" + col + "}" for col in df.columns) + new_line + r"\hline" + "\n"
    )

    # Build each row by joining columns with '&' to fit KaTeX array format
    body = df.apply(lambda row: " & ".join(row) + new_line, axis=1)
    body = "\n".join(body) + "\n"

    footer = r"\end{array}"

    katex_table = header + columns + body + footer
    return katex_table
