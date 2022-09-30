import pytest
from shared.Domain.Scraping.i_web_browser_operator import IWebBrowserOperator
from shared.Domain.Url.x_url import XUrl
from shared.Enums.browser_type import BrowserType
from shared.Domain.Scraping.x_browser_factory import XBrowserFactory
from shared.Domain.Scraping.x_driver_factory import XDriverFactory
from shared.factory import Factory
from shared.di_container import DiContainer


@pytest.fixture
def setuped_i_web_browser_operator():
    factory: Factory = XDriverFactory()
    xdriver = factory.create(BrowserType.CHROME, is_headless=True, on_docker=True)

    factory: Factory = XBrowserFactory()
    xbrowser = factory.create(xdriver, XUrl("https://maasaablog.com/"))

    i_web_browser_operator: IWebBrowserOperator = DiContainer().resolve(
        IWebBrowserOperator
    )
    i_web_browser_operator.boot(xbrowser)

    yield i_web_browser_operator

    xdriver.driver().quit()


def test_ID名でhtml要素を取得できること(setuped_i_web_browser_operator: IWebBrowserOperator):
    # ヘッダメニューのタイトル
    actual = setuped_i_web_browser_operator.find_by_id("header-in").web_element().text
    expected = "masayanblog"

    assert expected == actual


def test_xpath名でhtml要素を取得できること(setuped_i_web_browser_operator: IWebBrowserOperator):
    # ヘッダメニューのタイトル
    actual = (
        setuped_i_web_browser_operator.find_by_xpath("//*[@id='header-in']/h1/a/span")
        .web_element()
        .text
    )
    expected = "masayanblog"

    assert expected == actual
