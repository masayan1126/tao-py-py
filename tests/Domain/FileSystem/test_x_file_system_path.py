import pathlib
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr


def test_OSに依存しないパス文字列からパスオブジェクトを生成できる() -> None:
    expected = str(pathlib.Path("tests/x_file_system_path.py"))
    actual = XFileSystemPath(XStr("tests/x_file_system_path.py")).of_text()

    assert expected == actual


def test_現在の作業ディレクトリを取得できる() -> None:
    expected = str(pathlib.Path.cwd())
    actual = XFileSystemPath.cwd().of_text()

    assert expected == actual


def test_絶対パスから相対パスへ変換できる() -> None:
    cwd_str = str(pathlib.Path.cwd())
    abs_path_str = str(pathlib.Path(cwd_str, "tests/x_file_system_path.py"))

    expected = str(pathlib.Path("tests/x_file_system_path.py"))
    actual = XFileSystemPath(XStr(abs_path_str)).to_relative().of_text()

    assert expected == actual


def test_絶対パスから相対パスへ変換できる_基底パスを動的に切り替え可能() -> None:
    abs_path = XFileSystemPath.home_dir().join("git")

    expected = "git"
    actual = (
        XFileSystemPath(XStr(abs_path.of_text()))
        .to_relative(base_path=XFileSystemPath.home_dir().of_text())
        .of_text()
    )

    assert expected == actual


def test_相対パスから絶対パスへ変換できる() -> None:
    relative_path_str = str(pathlib.Path("tests/x_file_system_path.py"))

    expected = str(pathlib.Path(pathlib.Path.cwd(), relative_path_str))
    actual = XFileSystemPath(XStr(relative_path_str)).to_absolute().of_text()

    assert expected == actual


def test_ホームディレクトリを取得できる() -> None:
    expected = str(pathlib.Path.home())
    actual = XFileSystemPath.home_dir().of_text()

    assert expected == actual


def test_実際に存在するパスかチェックできる_True() -> None:
    assert XFileSystemPath.home_dir().exsits()


def test_実際に存在するパスかチェックできる_False() -> None:
    assert not XFileSystemPath(XStr("hoge/foo/var")).exsits()


def test_パスがディレクトリかどうかチェックできる_True() -> None:
    assert XFileSystemPath(XStr("tests")).is_dir()


def test_パスがディレクトリかどうかチェックできる_False() -> None:
    assert not XFileSystemPath(XStr("README.md")).is_dir()


def test_パスがファイルかどうかチェックできる_True() -> None:
    assert XFileSystemPath(XStr("README.md")).is_file()


def test_パスがファイルかどうかチェックできる_False() -> None:
    assert not XFileSystemPath(XStr("tests")).is_file()


def test_パスを追加できる() -> None:
    sut = XFileSystemPath(XStr("tests")).join("hoge/sample")
    assert sut.of_text() == str(pathlib.Path("tests/hoge/sample"))


def test_パスを連続で追加できる() -> None:
    sut = XFileSystemPath(XStr("tests")).join("hoge/sample")
    sut.join("foo")
    assert sut.of_text() == str(pathlib.Path("tests/hoge/sample/foo"))
