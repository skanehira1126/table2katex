import pathlib

import pandas as pd


def read_file(filepath: str, file_ext: str = "auto") -> pd.DataFrame:
    """
    Read a file and return it as a pandas DataFrame.

    Args:
        filepath (str): Path to the input file.
        file_ext (str, optional): File extension ('csv', 'tsv', or 'auto'). Defaults to 'auto'.

    Returns:
        pd.DataFrame: Loaded table data.

    Raises:
        ValueError: If the file extension is unsupported.
    """
    path = pathlib.Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {filepath}")

    # Infer extension if 'auto'
    ext = file_ext.lower()
    if ext == "auto":
        ext = path.suffix.lower().lstrip(".")

    if ext == "csv":
        return pd.read_csv(path)
    elif ext == "tsv":
        return pd.read_csv(path, sep="\t")
    elif ext == "jsonl":
        return pd.read_json(path, lines=True)
    else:
        raise ValueError(
            f"Unsupported file extension: {ext}. Supported extensions are 'csv' ,'tsv' or 'jsonl'."
        )
