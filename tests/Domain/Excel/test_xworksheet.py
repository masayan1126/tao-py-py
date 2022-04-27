import pytest
from shared.Domain.Excel.xexcel import XExcel
from shared.Domain.Excel.xworksheet import XWorksheet
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr


@pytest.fixture
def setuped_worksheet():
    filepath = XFileSystemPath(XStr("tests/Domain/Excel/sample.xlsx")).to_absolute()
    xworkbook = XExcel().read(filepath, sheet_name=None)
    xworksheet = xworkbook.get_sheet_by_name("プログラミング言語一覧")
    return xworksheet


def test_特定のセルを取得できる(setuped_worksheet: XWorksheet):

    assert setuped_worksheet.get_cell(2, 2) == "PHP"


def test_get_record_特定のレコードを取得できる(setuped_worksheet: XWorksheet):

    actual = setuped_worksheet.get_record(4)
    expected = {"id": 3, "name": "Python", "type": "動的型付け"}

    assert actual == expected


def test_get_record_存在しない行を指定した場合は例外(setuped_worksheet: XWorksheet):
    with pytest.raises(IndexError):
        setuped_worksheet.get_record(100)


def test_複数レコードを取得できる(setuped_worksheet: XWorksheet):

    actual = setuped_worksheet.get_records(3, 4, 1, 3)
    expected = [
        {"id": 2, "name": "Java", "type": "静的型付け"},
        {"id": 3, "name": "Python", "type": "動的型付け"},
    ]

    assert actual == expected


def test_条件指定してレコードを取得できる(setuped_worksheet: XWorksheet):

    actual = setuped_worksheet.get_records_with_filter(2, 4, 1, 3, "type == '動的型付け'")
    expected = [
        {"id": 1, "name": "PHP", "type": "動的型付け"},
        {"id": 3, "name": "Python", "type": "動的型付け"},
        {"id": 4, "name": "Ruby", "type": "動的型付け"},
    ]

    assert actual == expected


def test_条件に一致するレコードがない場合は空配列(setuped_worksheet: XWorksheet):

    actual = setuped_worksheet.get_records_with_filter(2, 4, 1, 3, "type == 'hoge'")
    expected = []

    assert actual == expected


def test_全レコードを取得できる(setuped_worksheet: XWorksheet):
    actual = setuped_worksheet.all_records()
    expected = [
        {"id": 1, "name": "PHP", "type": "動的型付け"},
        {"id": 2, "name": "Java", "type": "静的型付け"},
        {"id": 3, "name": "Python", "type": "動的型付け"},
        {"id": 4, "name": "Ruby", "type": "動的型付け"},
    ]

    assert actual == expected
