from unittest.mock import MagicMock, patch
from shared.Domain.Scraping.chrome_browser_operator_impl import (
    ChromeBrowserOperatorImpl,
)
from shared.Domain.Scraping.web_browser_operator_factory import (
    WebBrowserOperatorFactory,
)
from shared.Domain.Url.x_url import XUrl


@patch("shared.Domain.Scraping.chrome_browser_operator_impl.Chrome", MagicMock())
@patch.object(ChromeBrowserOperatorImpl, "_webdriver")
def test_ID名でhtml要素を取得できる(web_driver_mock) -> None:
    web_element_mock = MagicMock(text="masayanblog")
    web_driver_instance = web_driver_mock.return_value
    web_driver_instance.find_element.return_value = web_element_mock

    sut = WebBrowserOperatorFactory().create(XUrl("https://maasaablog.com"))

    assert sut.find_by_id("gegeg").web_element().text == "masayanblog"
