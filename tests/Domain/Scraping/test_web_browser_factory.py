from unittest.mock import MagicMock, patch
from shared.Domain.Scraping.web_browser_factory import WebBrowserFactory
from shared.Domain.Scraping.xbrowser import XBrowser
from shared.Domain.Scraping.xdriver import XDriver
from shared.Domain.Url.x_url import XUrl
from shared.Enums.browser_type import BrowserType


@patch("shared.Domain.Scraping.browser_judgement.webdriver.Chrome")
def test_ブラウザオブジェクトを生成できる(chorme_webdriver_mock) -> None:
    chorme_webdriver_mock.return_value = MagicMock()

    chorme_browser_operator = WebBrowserFactory().create(
        BrowserType.CHROME, XUrl("https://hogefoovar.com")
    )

    expected = XBrowser(XDriver(chorme_webdriver_mock), XUrl("https://hogefoovar.com"))
    actual = chorme_browser_operator.x_browser()
    assert expected == actual
