import pytest
from shared.Domain.Regex.xregex import XRegex
from shared.Domain.String.xstr import XStr


@pytest.fixture
def sut():
    return XRegex(
        XStr("https://zozo.jp/men-category/jacket-outerwear/tailored-jacket/?p_gtype=2")
    )


def test_正規表現に一致する文字列を取得できる(sut: XRegex):
    assert (
        sut.partial_match(
            XStr(".+?(?=\?)"),  # ?より以前の文字列にマッチ
        )
        == "https://zozo.jp/men-category/jacket-outerwear/tailored-jacket/"
    )


def test_一致する文字列がない場合はNone(sut: XRegex):
    assert sut.partial_match(XStr("([a-z]+)@([a-z]+)\.com")) is None


def test_正規表現に一致する文字列を置換できる(sut: XRegex):
    assert (
        sut.replace(
            XStr(".+?(?=\?)"),
            "",
        )  # ?より以前を空文字に置き換え
        == "?p_gtype=2"
    )
