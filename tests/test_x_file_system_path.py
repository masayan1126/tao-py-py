import pathlib

import pytest

from shared.Domain.x_file_system_path import XFileSystemPath
from shared.Domain.xstr import XStr


def test_OSに依存しないパス文字列からパスオブジェクトを生成できる() -> None:

    acutual = XFileSystemPath(XStr("tests/x_file_system_path.py")).of_text()
    expected = str(pathlib.Path("tests/x_file_system_path.py"))

    assert acutual == expected


def test_現在の作業ディレクトリを取得できる() -> None:
    acutual = XFileSystemPath.cwd().of_text()
    expected = str(pathlib.Path.cwd())

    assert acutual == expected


def test_絶対パスから相対パスへ変換できる() -> None:
    cwd_str = str(pathlib.Path.cwd())
    abs_path_str = str(pathlib.Path(cwd_str, "tests/x_file_system_path.py"))
    acutual = XFileSystemPath(XStr(abs_path_str)).to_relative().of_text()
    expected = str(pathlib.Path("tests/x_file_system_path.py"))

    assert acutual == expected


def test_絶対パスから相対パスへ変換できる_基底パスを動的に切り替え可能() -> None:
    abs_path = XFileSystemPath.home_dir().join("git")

    acutual = (
        XFileSystemPath(XStr(abs_path.of_text()))
        .to_relative(base_path=XFileSystemPath.home_dir().of_text())
        .of_text()
    )
    expected = "git"

    assert acutual == expected


def test_相対パスから絶対パスへ変換できる() -> None:
    relative_path_str = str(pathlib.Path("tests/x_file_system_path.py"))
    acutual = XFileSystemPath(XStr(relative_path_str)).to_absolute().of_text()
    expected = str(pathlib.Path(pathlib.Path.cwd(), relative_path_str))

    assert acutual == expected


def test_ホームディレクトリを取得できる() -> None:

    acutual = XFileSystemPath.home_dir().of_text()
    expected = str(pathlib.Path.home())

    assert acutual == expected


def test_実際に存在するパスかチェックできる_True() -> None:

    assert XFileSystemPath.home_dir().exsits()


def test_実際に存在するパスかチェックできる_False() -> None:

    assert not XFileSystemPath(XStr("hoge/foo/var")).exsits()


def test_パスがディレクトリかどうかチェックできる_True() -> None:

    assert XFileSystemPath(XStr("tests")).is_dir()


def test_パスがディレクトリかどうかチェックできる_False() -> None:

    assert not XFileSystemPath(XStr("tests/test_x_file_system_path.py")).is_dir()


def test_パスがファイルかどうかチェックできる_True() -> None:

    assert XFileSystemPath(XStr("tests/test_x_file_system_path.py")).is_file()


def test_パスがファイルかどうかチェックできる_False() -> None:

    assert not XFileSystemPath(XStr("tests")).is_file()


def test_パスを追加できる() -> None:

    filepath = XFileSystemPath(XStr("tests")).join("hoge/sample")
    assert filepath.of_text() == str(pathlib.Path("tests/hoge/sample"))


def test_パスを連続で追加できる() -> None:

    filepath = XFileSystemPath(XStr("tests")).join("hoge/sample")
    filepath.join("foo")
    assert filepath.of_text() == str(pathlib.Path("tests/hoge/sample/foo"))
