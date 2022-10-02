from unittest.mock import MagicMock, patch
from shared.Core.di_container import DiContainer
from shared.Domain.Scraping.web_browser_operator import WebBrowserOperator
from shared.Domain.Scraping.xweb_element import XWebElement
from shared.Domain.Url.x_url import XUrl


@patch("shared.Domain.Scraping.web_browser_operator_impl.WebDriver")
def test_ID名でhtml要素を取得できること(web_driver_mock) -> None:
    web_element_mock = MagicMock(text="masayanblog")
    web_driver_mock.find_element.return_value = web_element_mock

    # web_browser_operatorの生成にWebBrowserFactoryは使用しない
    web_browser_operator = DiContainer().resolve(WebBrowserOperator)
    web_browser_operator.boot(web_driver_mock, XUrl("https://maasaablog.com"))

    assert web_browser_operator.find_by_id("gegeg") == XWebElement(web_element_mock)
    assert (
        web_browser_operator.find_by_id("gegeg").web_element().text
        == XWebElement(web_element_mock).web_element().text
    )
