import json
import tempfile

import pandas as pd
import pytest

from table2katex.io import read_file


@pytest.mark.parametrize("ext,sep", [("csv", ","), ("tsv", "\t")])
def test_read_file_csv_tsv(ext, sep):
    df_expected = pd.DataFrame({"name": ["Alice", "Bob"], "score": [90, 85]})

    with tempfile.NamedTemporaryFile(mode="w+", suffix=f".{ext}", delete=False) as tmp:
        df_expected.to_csv(tmp.name, index=False, sep=sep)
        tmp.flush()

        df_result = read_file(tmp.name)

    pd.testing.assert_frame_equal(df_result, df_expected)


def test_read_file_jsonl():
    df_expected = pd.DataFrame([{"name": "Alice", "score": 90}, {"name": "Bob", "score": 85}])

    with tempfile.NamedTemporaryFile(mode="w+", suffix=".jsonl", delete=False) as tmp:
        for record in df_expected.to_dict(orient="records"):
            tmp.write(json.dumps(record) + "\n")
        tmp.flush()

        df_result = read_file(tmp.name)

    pd.testing.assert_frame_equal(df_result, df_expected)


def test_read_file_notfound():
    with pytest.raises(FileNotFoundError):
        read_file("nonexistent.csv")


def test_read_file_unsupported_ext():
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".unknown", delete=False) as tmp:
        tmp.write("dummy data\n")
        tmp.flush()

        with pytest.raises(ValueError):
            read_file(tmp.name)
