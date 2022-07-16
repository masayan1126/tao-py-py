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
def setuped() -> tuple[XWebElementList, IWebBrowserOperator]:
    xdriver = XDriverFactory().create(
        BrowserType.CHROME, is_headless=True, on_docker=True
    )
    xbrowser = XBrowserFactory().create(xdriver, XUrl("https://maasaablog.com/"))

    i_web_browser_operator: IWebBrowserOperator = DiContainer().resolve(
        IWebBrowserOperator
    )
    i_web_browser_operator.boot(xbrowser)

    yield XWebElementList(
        [
            i_web_browser_operator.find_by_id("header-in"),
            i_web_browser_operator.find_by_id("go-to-top"),
        ]
    ), i_web_browser_operator

    xdriver.driver().quit()


def test_all_全要素を取得できる(setuped: tuple[XWebElementList, IWebBrowserOperator]) -> None:
    xweb_element_list: XWebElementList = setuped[0]
    actual = xweb_element_list.all()
    expected = [
        setuped[1].find_by_id("header-in"),
        setuped[1].find_by_id("go-to-top"),
    ]

    assert expected == actual


def test_first_1つめの要素を取得できる(
    setuped: tuple[XWebElementList, IWebBrowserOperator]
) -> None:
    xweb_element_list: XWebElementList = setuped[0]
    actual = xweb_element_list.first()
    expected = setuped[1].find_by_id("header-in")

    assert expected == actual


def test_first_空のリストから要素を取り出そうとした場合は例外() -> None:
    with pytest.raises(IndexError):
        XWebElementList([]).first()


def test_add_要素を追加できる(setuped: tuple[XWebElementList, IWebBrowserOperator]) -> None:

    xweb_element_list: XWebElementList = setuped[0]
    xweb_element_list = xweb_element_list.add(setuped[1].find_by_id("index-tab-wrap"))
    expected = 3
    actual = xweb_element_list.count()

    assert expected == actual


def test_all_全ての要素を取得できる(setuped: tuple[XWebElementList, IWebBrowserOperator]) -> None:
    xweb_element_list: XWebElementList = setuped[0]
    expected = 2
    actual = xweb_element_list.count()

    assert expected == actual


def test_map_個々の要素に関数を適用できる(
    setuped: tuple[XWebElementList, IWebBrowserOperator]
) -> None:

    xweb_element_list: XWebElementList = setuped[0]

    def callable(xweb_element: XWebElement):
        value = 1
        xweb_element.set_value(value)
        value += 1

    xweb_element_list = xweb_element_list.map(callable)

    expected = 1
    actual = xweb_element_list.first().value()

    assert expected == actual


def test_is_empty_空かどうかチェックできる(
    setuped: tuple[XWebElementList, IWebBrowserOperator]
) -> None:

    xweb_element_list: XWebElementList = XWebElementList([])
    # 空
    expected = True
    actual = xweb_element_list.is_empty()
    assert expected == actual

    # 要素有り

    xweb_element_list = xweb_element_list.add(setuped[1].find_by_id("index-tab-wrap"))

    expected = False
    actual = xweb_element_list.is_empty()
    assert expected == actual
