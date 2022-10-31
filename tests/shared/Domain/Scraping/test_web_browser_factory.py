from unittest.mock import MagicMock, patch
from shared.Domain.Scraping.chrome_browser_operator_impl import (
    ChromeBrowserOperatorImpl,
)
from shared.Domain.Scraping.web_browser_operator_factory import (
    WebBrowserOperatorFactory,
)
from shared.Domain.Url.x_url import XUrl
from shared.Domain.Scraping.browser_type import BrowserType


@patch("shared.Domain.Scraping.chrome_browser_operator_impl.Chrome", MagicMock())
def test_ブラウザ操作用のインスタンスを生成できる() -> None:
    browser_operator_mock = WebBrowserOperatorFactory().create(
        XUrl("https://hogefoovar.com"), BrowserType.CHROME
    )

    expected = ChromeBrowserOperatorImpl(
        XUrl("https://hogefoovar.com"), BrowserType.CHROME
    )
    actual = browser_operator_mock
    assert expected == actual
