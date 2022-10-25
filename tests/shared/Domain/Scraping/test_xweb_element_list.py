from unittest.mock import MagicMock
import pytest
from shared.Domain.Scraping.xweb_element import XWebElement
from shared.Domain.Scraping.xweb_element_list import XWebElementList


@pytest.fixture
def xweb_elements() -> list[XWebElement]:
    xweb_element_mock1 = MagicMock(name="x_web_element1")
    xweb_element_mock1.value.return_value = "a"
    xweb_element_mock2 = MagicMock(name="x_web_element2")
    xweb_element_mock2.value.return_value = ""
    xweb_element_mock3 = MagicMock(name="x_web_element3")
    xweb_element_mock3.value.return_value = "u"

    return [xweb_element_mock1, xweb_element_mock2, xweb_element_mock3]


def test_all_全要素を取得できる(xweb_elements: list[XWebElement]) -> None:
    sut = XWebElementList([xweb_elements[0], xweb_elements[1], xweb_elements[2]])
    assert xweb_elements == sut.all()


def test_add_要素を追加できる(xweb_elements: list[XWebElement]) -> None:
    new = MagicMock(name="mock4")
    sut = XWebElementList(xweb_elements)

    expected = XWebElementList(
        [xweb_elements[0], xweb_elements[1], xweb_elements[2], new]
    )
    actual = sut.add(new)

    assert expected == actual


def test_map_個々の要素に関数を適用できる(xweb_elements: list[XWebElement]) -> None:
    # xweb_elementをxweb_elementの値に変換して返す
    def callback(xweb_element: XWebElement):
        return xweb_element.value()

    sut = XWebElementList(xweb_elements).map(callback)

    expected = ["a", "", "u"]
    actual = sut.all()

    assert expected == actual


def test_first_1つめの要素を取得できる(xweb_elements: list[XWebElement]) -> None:

    sut = XWebElementList(xweb_elements)
    xweb_element = sut.first()

    expected = xweb_elements[0]
    actual = xweb_element

    assert expected == actual


def test_first_空の場合は例外() -> None:
    with pytest.raises(IndexError):
        XWebElementList().first()


def test_count_要素数を取得できる(xweb_elements: list[XWebElement]) -> None:
    sut = XWebElementList(xweb_elements)
    assert sut.count() == 3


def test_count_要素数を取得できる_callbackあり(xweb_elements: list[XWebElement]) -> None:
    # 空文字の要素数
    def callback(item: XWebElement):
        return item.value() == ""

    sut = XWebElementList(xweb_elements)
    assert sut.count(callback) == 1


def test_is_empty_空かどうかチェックできる_空の場合(xweb_elements: list[XWebElement]) -> None:
    sut = XWebElementList()
    assert sut.is_empty()


def test_is_empty_空かどうかチェックできる_空ではない場合(xweb_elements: list[XWebElement]) -> None:
    sut = XWebElementList(xweb_elements)
    assert not sut.is_empty()
