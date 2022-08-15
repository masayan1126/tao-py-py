import pytest
from shared.Domain.String.xstr import XStr
from shared.Exception.empty_string_error import EmptyStringError


@pytest.fixture
def setuped_xstr() -> XStr:
    return XStr("masayan")


def test_文字列を管理するオブジェクトを生成できる(setuped_xstr: XStr) -> None:
    actual = setuped_xstr
    expected = XStr("masayan")

    assert expected == actual


def test_空文字を指定した場合は例外() -> None:
    with pytest.raises(EmptyStringError):
        XStr("")


def test_文字列型以外を指定した場合は例外() -> None:
    with pytest.raises(TypeError):
        XStr(1)


def test_対象の文字列に特定の文字が含まれているかチェックできる_含まれていない場合(setuped_xstr: XStr) -> None:

    assert setuped_xstr.is_contain("hoge") is False


def test_対象の文字列に特定の文字が含まれているかチェックできる_含まれている場合(setuped_xstr: XStr) -> None:

    assert setuped_xstr.is_contain("yan") is True


def test_対象の文字列が特定の文字で始まっているかチェックできる_始まっている場合(setuped_xstr: XStr) -> None:

    assert setuped_xstr.has_begin("ma") is True


def test_対象の文字列が特定の文字で始まっているかチェックできる_始まっていない場合(setuped_xstr: XStr) -> None:

    assert setuped_xstr.has_begin("ze") is False


def test_対象の文字列が特定の文字で終わっているかチェックできる_終わっている場合(setuped_xstr: XStr) -> None:

    assert setuped_xstr.has_end("an") is True


def test_対象の文字列が特定の文字で終わっているかチェックできる_終わっていない場合(setuped_xstr: XStr) -> None:

    assert setuped_xstr.has_end("pc") is False


def test_対象の文字列数をカウントできる(setuped_xstr: XStr) -> None:

    assert setuped_xstr.count() == 7


def test_対象の文字列をリストに変換できること_区切り文字の指定なし(setuped_xstr: XStr) -> None:

    assert setuped_xstr.to_list() == ["m", "a", "s", "a", "y", "a", "n"]


def test_対象の文字列をリストに変換できること_区切り文字の指定あり() -> None:

    assert XStr("ma!sa!ya!n").to_list("!") == ["ma", "sa", "ya", "n"]


def test_対象の文字列オブジェクトに文字列を結合できる_1(setuped_xstr: XStr) -> None:

    actual = setuped_xstr.join("\n")
    expected = XStr("masayan" + "\n")

    assert actual == expected


def test_対象の文字列オブジェクトに文字列を結合できる_2(setuped_xstr: XStr) -> None:

    actual = setuped_xstr.join("desu")
    expected = XStr("masayan" + "desu")

    assert actual == expected


def test_対象の文字列を大文字に変換できる(setuped_xstr: XStr) -> None:

    assert setuped_xstr.to_upper() == XStr("MASAYAN")


def test_対象の文字列を小文字に変換できる() -> None:

    xstr = XStr("MASAYAN")
    assert xstr.to_lower() == XStr("masayan")


def test_対象の文字列について文字も位置も一致している文字の数を取得できる_1() -> None:

    xstr = XStr("MASAYAN")
    assert xstr.compare("NAZALAB") == 3


def test_対象の文字列について文字も位置も一致している文字の数を取得できる_2() -> None:

    xstr = XStr("MASAYAN")
    assert xstr.compare("XXXXXXX") == 0


def test_対象の文字列について文字も位置も一致している文字の数を取得できる_3() -> None:

    xstr = XStr("MASAYAN")
    assert xstr.compare("XXXXXXX") == 0


def test_対象の文字列について文字も位置も一致している文字の数を取得できる_文字列長が異なる文字列を指定した場合は例外() -> None:
    with pytest.raises(ValueError):
        xstr = XStr("abc")
        xstr.compare("z")
