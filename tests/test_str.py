import pytest
from shared.Domain.xstr import XStr


@pytest.fixture
def setuped_xstr():
    xstr = XStr("masayan")
    return xstr


def test_対象の文字列に特定の文字が含まれているかチェックできること_含まれていない場合(setuped_xstr):

    assert setuped_xstr.is_contain("hoge") == False


def test_対象の文字列に特定の文字が含まれているかチェックできること_含まれている場合(setuped_xstr):

    assert setuped_xstr.is_contain("yan") == True


def test_対象の文字列が特定の文字で始まっているかチェックできること(setuped_xstr):

    assert setuped_xstr.has_begin("ma") == True


def test_対象の文字列が特定の文字で終わっているかチェックできること(setuped_xstr):

    assert setuped_xstr.has_end("an") == True
