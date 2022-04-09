import pytest
from shared.Domain.Scraping.i_web_browser_operator import IWebBrowserOperator
from shared.Domain.xurl import XUrl
from shared.Enums.browser_type import BrowserType
from shared.Domain.Scraping.x_browser_factory import XBrowserFactory
from shared.Domain.Scraping.x_driver_factory import XDriverFactory
from shared.i_factory import IFactory
from shared.di_container import DiContainer


@pytest.fixture
def setuped_i_web_browser_operator():
    factory: IFactory = XDriverFactory()
    xdriver = factory.create(BrowserType.CHROME)

    factory: IFactory = XBrowserFactory()
    xbrowser = factory.create(xdriver, XUrl("https://maasaablog.com/"))

    i_web_browser_operator: IWebBrowserOperator = DiContainer().resolve(
        IWebBrowserOperator
    )
    i_web_browser_operator.boot(xbrowser)

    return i_web_browser_operator


def test_ID名でhtml要素を取得できること(setuped_i_web_browser_operator: IWebBrowserOperator):
    # ヘッダメニューのタイトル
    acutual = setuped_i_web_browser_operator.find_by_id("header-in").web_element().text
    expected = "masayanblog"

    assert acutual == expected


def test_xpath名でhtml要素を取得できること(setuped_i_web_browser_operator: IWebBrowserOperator):
    # ヘッダメニューのタイトル
    acutual = (
        setuped_i_web_browser_operator.find_by_xpath("//*[@id='header-in']/h1/a/span")
        .web_element()
        .text
    )
    expected = "masayanblog"

    assert acutual == expected
