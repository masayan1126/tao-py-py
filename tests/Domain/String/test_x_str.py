import pytest
from shared.Domain.String.xstr import XStr
from shared.Exception.empty_string_error import EmptyStringError
from shared.Domain.Log.x_logger import XLogger


@pytest.fixture
def setuped_xstr() -> XStr:
    xstr = XStr("masayan")
    return xstr


def test_文字列を取得できる(setuped_xstr: XStr) -> None:
    acutual = setuped_xstr.get_string()
    expected = "masayan"

    assert acutual == expected


def test_空文字を指定した場合は例外() -> None:
    with pytest.raises(EmptyStringError):
        xstr = XStr("")


def test_文字列型以外を指定した場合は例外() -> None:
    with pytest.raises(TypeError):
        xstr = XStr(1)


def test_対象の文字列に特定の文字が含まれているかチェックできること_含まれていない場合(setuped_xstr: XStr) -> None:

    assert setuped_xstr.is_contain("hoge") == False


def test_対象の文字列に特定の文字が含まれているかチェックできること_含まれている場合(setuped_xstr: XStr) -> None:

    assert setuped_xstr.is_contain("yan") == True


def test_対象の文字列が特定の文字で始まっているかチェックできること(setuped_xstr: XStr) -> None:

    assert setuped_xstr.has_begin("ma") == True


def test_対象の文字列が特定の文字で終わっているかチェックできること(setuped_xstr: XStr) -> None:

    assert setuped_xstr.has_end("an") == True
