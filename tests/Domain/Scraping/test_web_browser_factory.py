from unittest.mock import MagicMock, patch
from shared.Core.di_container import DiContainer
from shared.Domain.Scraping.web_browser_factory import WebBrowserFactory
from shared.Domain.Scraping.web_browser_operator import WebBrowserOperator
from shared.Domain.Url.x_url import XUrl
from shared.Domain.Scraping.browser_type import BrowserType


@patch("shared.Domain.Scraping.web_browser_factory.BrowserTypeJudgement")
def test_ブラウザオブジェクトを生成できる(browser_judement_mock) -> None:
    web_driver_mock = MagicMock()
    browser_judement_mock.judge.return_value = web_driver_mock

    browser_operator_from_mock = WebBrowserFactory().create(
        XUrl("https://hogefoovar.com"), BrowserType.CHROME
    )

    web_browser_operator = DiContainer().resolve(WebBrowserOperator)
    web_browser_operator.boot(web_driver_mock, XUrl("https://hogefoovar.com"))

    expected = web_browser_operator
    actual = browser_operator_from_mock
    assert expected == actual
