import pytest
from shared.Domain.Excel.xexcel import XExcel
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr


@pytest.fixture
def setuped_filepath() -> XFileSystemPath:
    filepath = XFileSystemPath(
        XStr("tests/Domain/Excel/output_sample.xlsx")
    ).to_absolute()
    yield filepath
    filepath.delete()


def test_エクセルを読み取ることができる():
    filepath = XFileSystemPath(XStr("tests/Domain/Excel/sample.xlsx")).to_absolute()
    xworkbook = XExcel().read(filepath, sheet_name=None)
    expected = "プログラミング言語一覧"
    actual = xworkbook.get_all_sheet_names()[0]
    assert expected == actual


def test_エクセルを出力できる(setuped_filepath: XFileSystemPath):

    data = {
        "id": [1, 2, 3, 4],
        "name": ["PHP", "Java", "Python", "Ruby"],
        "type": ["動的型付け", "静的型付け", "動的型付け", "動的型付け"],
    }

    XExcel().output(setuped_filepath, data)
    # テスト対象のクラスは出力するだけのクラスなので、出力するデータの中身まではチェックしない
    assert setuped_filepath.exsits()


def test_read_存在しないファイルを指定した場合は例外():
    with pytest.raises(FileNotFoundError):
        filepath = XFileSystemPath(XStr("tests/Domain/Hoge/sample.xlsx")).to_absolute()
        XExcel().read(filepath, sheet_name=None)


# def test_output_存在しないファイルを指定した場合は例外():
#     with pytest.raises(OSError):
#         filepath = XFileSystemPath(XStr("tests/Domain/Hoge/sample.xlsx")).to_absolute()

#         xworkbook = XExcel().output(filepath, {})
