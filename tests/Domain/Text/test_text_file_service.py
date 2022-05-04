import pytest
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr
from shared.Domain.Text.text_file_service import TextFileService
from shared.Domain.Text.x_text import XText


@pytest.fixture
def setuped_x_text() -> XText:
    # 読み込み用
    filepath1 = XFileSystemPath(XStr("tests/Domain/Text/sample.txt")).to_absolute()
    # 書き込み用
    filepath2 = XFileSystemPath(XStr("tests/Domain/Text/sample2.txt")).to_absolute()
    x_text1 = XText(filepath1)
    x_text2 = XText(filepath2)
    return x_text1, x_text2


def test_テキストファイルを文字列として読み取ることができる(setuped_x_text: XText) -> None:
    acutual = TextFileService(setuped_x_text[0]).read("UTF-8")
    expected = "ruby,python\njava,php\njavascript"

    assert acutual == expected


def test_ファイルが見つからない場合は例外_read() -> None:
    with pytest.raises(FileNotFoundError):
        filepath = XFileSystemPath(XStr("tests/Domain/Foo/hoge.txt")).to_absolute()
        x_text = XText(filepath)
        TextFileService(x_text).read("UTF-8")


def test_テキストファイルをリストとして読み取ることができる(setuped_x_text: XText) -> None:
    acutual = TextFileService(setuped_x_text[0]).readlines("UTF-8")
    expected = ["ruby,python", "java,php", "javascript"]

    assert acutual == expected


def test_ファイルが見つからない場合は例外_readlines() -> None:
    with pytest.raises(FileNotFoundError):
        filepath = XFileSystemPath(XStr("tests/Domain/Foo/hoge.txt")).to_absolute()
        x_text = XText(filepath)
        TextFileService(x_text).readlines("UTF-8")


def test_テキストファイルに書き込むことができる_write_改行あり(setuped_x_text: XText) -> None:
    acutual = TextFileService(setuped_x_text[1]).write(
        content=["python", "java", "php"],
        is_overwrite=True,
        encoding="UTF-8",
        needs_indention=True,
    )
    expected = "python\njava\nphp"

    assert acutual == expected


def test_テキストファイルに書き込むことができる_write_改行なし(setuped_x_text: XText) -> None:
    acutual = TextFileService(setuped_x_text[1]).write(
        content=["python", "java", "php"],
        is_overwrite=True,
        encoding="UTF-8",
        needs_indention=False,
    )
    expected = "pythonjavaphp"

    assert acutual == expected


def test_ファイルが見つからない場合は例外_write() -> None:
    with pytest.raises(FileNotFoundError):
        filepath = XFileSystemPath(XStr("tests/Domain/Foo/hoge.txt")).to_absolute()
        x_text = XText(filepath)
        TextFileService(x_text).write(
            content=XStr("python"),
            is_overwrite=True,
            encoding="UTF-8",
            needs_indention=True,
        )
