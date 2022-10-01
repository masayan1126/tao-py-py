from unittest.mock import MagicMock
from shared.Domain.Scraping.xweb_element import XWebElement


def test_webelementを取得できる() -> None:
    web_element = MagicMock(text="hoge", tag_name="p")
    x_web_element = XWebElement(web_element)

    expected1 = "hoge"
    actual1 = x_web_element.web_element().text
    expected2 = "p"
    actual2 = x_web_element.web_element().tag_name
    assert expected1 == actual1 and expected2 == actual2


def test_webelementに値をセットできる() -> None:
    web_element = MagicMock(text="hoge", tag_name="input")
    x_web_element = XWebElement(web_element)

    assert x_web_element.value() == ""

    x_web_element.set_value("大阪太郎")

    expected = "大阪太郎"
    actual = x_web_element.value()

    assert expected == actual


# FIXME: クリックテスト
def test_クリックできる() -> None:
    web_element = MagicMock(text="ボタン", tag_name="button")
    x_web_element = XWebElement(web_element)

    assert x_web_element.click() is None
