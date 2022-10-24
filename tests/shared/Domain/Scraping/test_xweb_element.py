from unittest.mock import MagicMock
from shared.Domain.Scraping.xweb_element import XWebElement


def test_webelementを取得できる() -> None:
    web_element = MagicMock(text="hoge", tag_name="p")
    sut = XWebElement(web_element)

    actual = sut.web_element()
    assert "hoge" == actual.text and "p" == actual.tag_name


def test_webelementに値をセットできる() -> None:
    web_element = MagicMock(text="hoge", tag_name="input")
    sut = XWebElement(web_element)

    # セット前
    assert sut.value() == ""
    sut.set_value("大阪太郎")

    expected = "大阪太郎"
    actual = sut.value()

    assert expected == actual


# FIXME: クリックテスト
def test_クリックできる() -> None:
    web_element = MagicMock(text="ボタン", tag_name="button")
    sut = XWebElement(web_element)

    assert sut.click() is None
