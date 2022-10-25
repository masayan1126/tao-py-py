from unittest.mock import MagicMock, patch
from shared.Domain.Scraping.html_analyzer_factory import (
    HtmlAnalyzerFactory,
)
from shared.Domain.Scraping.html_analyzer_impl import HtmlAnalyzerImpl
from shared.Domain.Url.x_url import XUrl


@patch("shared.Domain.Scraping.html_analyzer_factory.requests")
def test_HTML解析用インスタンスを生成できる(mock_requests):
    response_mock = MagicMock(status_code=200, content="dummy binary")
    mock_requests.get.return_value = response_mock
    sut = HtmlAnalyzerFactory()

    expected = HtmlAnalyzerImpl()
    actual = sut.create(XUrl("https://maasaablog.com"))
    assert expected == actual
