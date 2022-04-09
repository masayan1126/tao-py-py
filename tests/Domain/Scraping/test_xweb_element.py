from typing import Dict
import pytest
from shared.Domain.Scraping.xweb_element import XWebElement
from shared.Domain.Scraping.xweb_element_list import XWebElementList
from shared.Domain.Scraping.i_web_browser_operator import IWebBrowserOperator
from shared.Domain.xurl import XUrl
from shared.Enums.browser_type import BrowserType
from shared.Domain.Scraping.x_browser_factory import XBrowserFactory
from shared.Domain.Scraping.x_driver_factory import XDriverFactory
from shared.di_container import DiContainer


@pytest.fixture
def setuped():
    xdriver = XDriverFactory().create(BrowserType.CHROME)
    xbrowser = XBrowserFactory().create(xdriver, XUrl("https://maasaablog.com/"))

    i_web_browser_operator: IWebBrowserOperator = DiContainer().resolve(
        IWebBrowserOperator
    )
    i_web_browser_operator.boot(xbrowser)

    return {
        "list": XWebElementList(
            [
                i_web_browser_operator.find_by_id("header-in"),
                i_web_browser_operator.find_by_id("go-to-top"),
            ]
        ),
        "operator": i_web_browser_operator,
    }


def test_webelementを取得できる(setuped: Dict) -> None:

    xweb_element: XWebElement = setuped["operator"].find_by_id("header-in")
    xweb_element_list: XWebElementList = setuped["list"]

    expected = xweb_element.web_element()
    acutual = xweb_element_list.first().web_element()
    assert acutual == expected
