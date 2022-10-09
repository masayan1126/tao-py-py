import pytest
from shared.Domain.String.xstr import XStr
from shared.Exception.empty_string_error import EmptyStringError


@pytest.fixture
def sut() -> XStr:
    return XStr("masayan")


def test_空文字を指定した場合は例外() -> None:
    with pytest.raises(EmptyStringError):
        XStr("")


def test_文字列型以外を指定した場合は例外() -> None:
    with pytest.raises(TypeError):
        XStr(1)


def test_対象の文字列に特定の文字が含まれているかチェックできる_含まれている場合(sut: XStr) -> None:
    assert sut.is_contain("yan")


def test_対象の文字列に特定の文字が含まれているかチェックできる_含まれていない場合(sut: XStr) -> None:
    assert not sut.is_contain("hoge")


def test_対象の文字列が特定の文字で始まっているかチェックできる_始まっている場合(sut: XStr) -> None:
    assert sut.has_begin("ma")


def test_対象の文字列が特定の文字で始まっているかチェックできる_始まっていない場合(sut: XStr) -> None:
    assert not sut.has_begin("ze")


def test_対象の文字列が特定の文字で終わっているかチェックできる_終わっている場合(sut: XStr) -> None:
    assert sut.has_end("an")


def test_対象の文字列が特定の文字で終わっているかチェックできる_終わっていない場合(sut: XStr) -> None:
    assert not sut.has_end("pc")


def test_対象の文字列数をカウントできる(sut: XStr) -> None:
    assert sut.count() == 7


def test_対象の文字列をリストに変換できる_区切り文字の指定なし(sut: XStr) -> None:
    assert sut.to_list() == ["m", "a", "s", "a", "y", "a", "n"]


def test_対象の文字列をリストに変換できる_区切り文字の指定あり() -> None:
    assert XStr("ma!sa!ya!n").to_list("!") == ["ma", "sa", "ya", "n"]


def test_対象の文字列を結合できる(sut: XStr) -> None:
    expected = XStr("masayan" + "desu")
    actual = sut.join("desu")

    assert expected == actual


def test_対象の文字列を大文字に変換できる(sut: XStr) -> None:
    assert sut.to_upper() == XStr("MASAYAN")


def test_対象の文字列を小文字に変換できる(sut: XStr) -> None:
    xstr = XStr("MASAYAN")
    assert xstr.to_lower() == sut


def test_対象の文字列について文字も位置も一致している文字の数を取得できる_一致あり() -> None:
    xstr = XStr("MASAYAN")
    assert xstr.approximate("NAZALAB") == 3


def test_対象の文字列について文字も位置も一致している文字の数を取得できる_一致なし() -> None:
    xstr = XStr("MASAYAN")
    assert xstr.approximate("XXXXXXX") == 0


def test_対象の文字列について文字も位置も一致している文字の数を取得できる_文字列長が異なる文字列を指定した場合は例外() -> None:
    with pytest.raises(ValueError):
        xstr = XStr("abc")
        xstr.approximate("z")
