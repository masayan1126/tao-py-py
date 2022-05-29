from typing import Dict
import pytest
from shared.Domain.Scraping.xweb_element import XWebElement
from shared.Domain.Scraping.xweb_element_list import XWebElementList
from shared.Domain.Scraping.i_web_browser_operator import IWebBrowserOperator
from shared.Domain.Url.x_url import XUrl
from shared.Enums.browser_type import BrowserType
from shared.Domain.Scraping.x_browser_factory import XBrowserFactory
from shared.Domain.Scraping.x_driver_factory import XDriverFactory
from shared.di_container import DiContainer


@pytest.fixture
def setuped():
    xdriver = XDriverFactory().create(
        BrowserType.CHROME, is_headless=True, on_docker=True
    )
    xbrowser = XBrowserFactory().create(xdriver, XUrl("https://maasaablog.com/"))

    i_web_browser_operator: IWebBrowserOperator = DiContainer().resolve(
        IWebBrowserOperator
    )
    i_web_browser_operator.boot(xbrowser)

    yield {
        "list": XWebElementList(
            [
                i_web_browser_operator.find_by_id("header-in"),
                i_web_browser_operator.find_by_id("go-to-top"),
            ]
        ),
        "operator": i_web_browser_operator,
    }

    xdriver.driver().quit()


def test_first_1つめの要素を取得できる(setuped: dict) -> None:
    xweb_element_list: XWebElementList = setuped["list"]
    acutual = xweb_element_list.first()
    expected = setuped["operator"].find_by_id("header-in")

    assert acutual == expected


def test_first_空のリストから要素を取り出そうとした場合は例外() -> None:
    with pytest.raises(IndexError):
        XWebElementList([]).first()


def test_add_要素を追加できる(setuped: dict) -> None:

    xweb_element_list: XWebElementList = setuped["list"]
    xweb_element_list = xweb_element_list.add(
        setuped["operator"].find_by_id("index-tab-wrap")
    )
    expected = 3
    acutual = xweb_element_list.count()

    assert acutual == expected


def test_all_全ての要素を取得できる(setuped: dict) -> None:
    xweb_element_list: XWebElementList = setuped["list"]
    expected = 2
    acutual = xweb_element_list.count()

    assert acutual == expected


def test_map_個々の要素に関数を適用できる(setuped: dict) -> None:

    xweb_element_list: XWebElementList = setuped["list"]

    def callable(xweb_element: XWebElement):
        value = 1
        xweb_element.set_value(value)
        value += 1

    xweb_element_list = xweb_element_list.map(callable)

    expected = 1
    acutual = xweb_element_list.first().value()

    assert acutual == expected


def test_is_empty_空かどうかチェックできる(setuped: dict) -> None:

    xweb_element_list: XWebElementList = XWebElementList([])
    # 空
    expected = True
    acutual = xweb_element_list.is_empty()
    assert acutual == expected

    # 要素有り

    xweb_element_list = xweb_element_list.add(
        setuped["operator"].find_by_id("index-tab-wrap")
    )

    expected = False
    acutual = xweb_element_list.is_empty()
    assert acutual == expected
