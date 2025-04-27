import argparse

from table2katex.gen import make_katex_table
from table2katex.io import read_file


def get_parser():
    parser = argparse.ArgumentParser(description="Convert tabular data into KaTeX array format.")
    parser.add_argument("input")

    parser.add_argument(
        "--align",
        default="c",
        help="Column alignment(s). Single value like 'c' or multiple values like 'l:c:r'.",
    )
    parser.add_argument(
        "--file-ext",
        default="auto",
        help="Input file extension (csv, tsv or jsonl). Default is 'auto' (infer from file name).",
    )

    parser.set_defaults(func=main)
    return parser


def cli():
    parser = get_parser()
    args = vars(parser.parse_args())

    if func := args.pop("func", None):
        func(**args)

    else:
        parser.print_help()


def main(input: str, align: str, file_ext: str):
    """ """

    df = read_file(input, file_ext)

    if ":" in align:
        column_alignment = align.split(":")
    else:
        column_alignment = align

    katex_table = make_katex_table(df, column_alignment)

    print(katex_table)
