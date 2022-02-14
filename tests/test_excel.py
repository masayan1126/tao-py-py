from glob import glob
import pandas as pd
import pytest
from pandas.testing import assert_series_equal
from pandas.testing import assert_frame_equal
from shared.Domain.xexcel import XExcel
from shared.Domain.xworksheet import XWorksheet


@pytest.fixture
def setuped_worksheet():
    filepath = glob("C:\\Users\\nishigaki\\jupyter-lab\\*.xlsx")[0]
    xworkbook = XExcel().read(filepath, sheet_name=None)
    xworksheet = xworkbook.get_sheet_by_name("プログラミング言語一覧")
    return xworksheet

@pytest.mark.skipif(True, reason="[エクセルファイルの準備が必要なため]")
def test_特定のセルを取得できる(setuped_worksheet: XWorksheet):
    assert setuped_worksheet.get_cell(2, 1) == "Python"

@pytest.mark.skipif(True, reason="[エクセルファイルの準備が必要なため]")
def test_特定のレコードを取得できる(setuped_worksheet: XWorksheet):

    data = {
        "id": [3],
        "name": ["Python"],
        "type": ["動的型付け"],
    }

    actual = setuped_worksheet.get_record(2)
    expected = pd.DataFrame(data, columns=["id", "name", "type"]).iloc[0]
    # check_names：bool、デフォルトはTrue (シリーズ名とインデックス名属性をチェックするかどうか。
    assert_series_equal(actual, expected, check_names=False)

@pytest.mark.skipif(True, reason="[エクセルファイルの準備が必要なため]")
def test_複数レコードを取得できる(setuped_worksheet: XWorksheet):

    data = {
        "id": [2, 3],
        "name": ["Java", "Python"],
        "type": ["静的型付け", "動的型付け"],
    }

    # インデックスを振り直す
    actual = setuped_worksheet.get_records(1, 2, 0, 2).reset_index(drop=True)
    expected = (
        pd.DataFrame(data, columns=["id", "name", "type"])
        .iloc[0:1, 0:2]
        .reset_index(drop=True)
    )
    assert_frame_equal(actual, expected)
