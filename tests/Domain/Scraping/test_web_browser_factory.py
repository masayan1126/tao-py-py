from unittest.mock import MagicMock, patch
from shared.Domain.Scraping.web_browser_factory import WebBrowserFactory
from shared.Domain.Scraping.web_browser_operator_impl import WebBrowserOperatorImpl
from shared.Domain.Url.x_url import XUrl
from shared.Domain.Scraping.browser_type import BrowserType


@patch("shared.Domain.Scraping.web_browser_factory.BrowserTypeJudgement")
def test_ブラウザオブジェクトを生成できる(browser_judement_mock) -> None:
    web_driver_mock = MagicMock()
    browser_judement_mock.judge.return_value = web_driver_mock

    browser_operator_from_mock = WebBrowserFactory().create(
        XUrl("https://hogefoovar.com"), BrowserType.CHROME
    )

    expected = WebBrowserOperatorImpl()
    actual = browser_operator_from_mock
    assert expected == actual
