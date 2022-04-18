from glob import glob
import pandas as pd
import pytest
from pandas.testing import assert_series_equal
from pandas.testing import assert_frame_equal
from shared.Domain.Excel.xexcel import XExcel
from shared.Domain.Excel.xworksheet import XWorksheet
from shared.Domain.x_file_system_path import XFileSystemPath
from shared.Domain.xstr import XStr


@pytest.fixture
def setuped_worksheet():
    filepath = XFileSystemPath(XStr("tests/sample.xlsx")).to_absolute()
    xworkbook = XExcel().read(filepath, sheet_name=None, header_row_number=None)
    xworksheet = xworkbook.get_sheet_by_name("プログラミング言語一覧")
    return xworksheet


def test_特定のセルを取得できる(setuped_worksheet: XWorksheet):
    assert setuped_worksheet.get_cell(1, 0) == "Python"


# def test_エクセルが開いているとパーミッションエラー(setuped_worksheet: XWorksheet):
#      with pytest.raises(UnidentifiedImageError):


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
