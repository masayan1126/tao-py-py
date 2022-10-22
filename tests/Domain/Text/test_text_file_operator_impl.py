import pytest
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr
from shared.Domain.TextFile.text_file_operator_impl import TextFileOperatorImpl


@pytest.fixture
def setuped_filepaths():
    # 読み込み用
    filepath1 = XFileSystemPath(XStr("tests/Domain/Text/sample.txt")).to_absolute()
    # 書き込み用
    filepath2 = XFileSystemPath(XStr("tests/Domain/Text/sample2.txt")).to_absolute()
    return filepath1, filepath2


def test_テキストファイルの中身をを1つの文字列として読み取ることができる(
    setuped_filepaths: list[XFileSystemPath],
) -> None:
    sut = TextFileOperatorImpl(setuped_filepaths[0])
    expected = "ruby,python\njava,php\njavascript"
    actual = sut.read("UTF-8")

    assert expected == actual


def test_ファイルが見つからない場合は例外_read() -> None:
    with pytest.raises(FileNotFoundError):
        filepath = XFileSystemPath(XStr("tests/Domain/Foo/hoge.txt")).to_absolute()
        sut = TextFileOperatorImpl(filepath)
        sut.read("UTF-8")


def test_テキストファイルの中身をリストとして読み取ることができる(setuped_filepaths: list[XFileSystemPath]) -> None:
    sut = TextFileOperatorImpl(setuped_filepaths[0])
    expected = ["ruby,python", "java,php", "javascript"]
    actual = sut.readlines("UTF-8")

    assert expected == actual


def test_ファイルが見つからない場合は例外_readlines() -> None:
    with pytest.raises(FileNotFoundError):
        filepath = XFileSystemPath(XStr("tests/Domain/Foo/hoge.txt")).to_absolute()
        sut = TextFileOperatorImpl(filepath)
        sut.readlines("UTF-8")


def test_テキストファイルに書き込むことができる_write_改行あり(
    setuped_filepaths: list[XFileSystemPath],
) -> None:
    sut = TextFileOperatorImpl(setuped_filepaths[1])

    expected = "python\njava\nphp"
    actual = sut.write(
        content=["python", "java", "php"],
        is_overwrite=True,
        encoding="UTF-8",
        needs_indention=True,
    )

    assert expected == actual


def test_テキストファイルに書き込むことができる_write_改行なし(
    setuped_filepaths: list[XFileSystemPath],
) -> None:
    sut = TextFileOperatorImpl(setuped_filepaths[1])

    expected = "pythonjavaphp"
    actual = sut.write(
        content=["python", "java", "php"],
        is_overwrite=True,
        encoding="UTF-8",
        needs_indention=False,
    )

    assert expected == actual


def test_ファイルが見つからない場合は例外_write() -> None:
    with pytest.raises(FileNotFoundError):
        filepath = XFileSystemPath(XStr("tests/Domain/Foo/hoge.txt")).to_absolute()
        sut = TextFileOperatorImpl(filepath)
        sut.write(
            content=XStr("python"),
            is_overwrite=True,
            encoding="UTF-8",
            needs_indention=True,
        )
