from unittest.mock import MagicMock, patch
from shared.Domain.Scraping.html_analyzer_factory import (
    HtmlAnalyzerFactory,
)
from shared.Domain.Scraping.html_analyzer_impl import HtmlAnalyzerImpl
from shared.Domain.Url.x_url import XUrl


@patch("shared.Domain.Scraping.html_analyzer_factory.requests")
def test_HTML解析用オブジェクトを生成できる(mock_requests):
    mock_requests.get.return_value = MagicMock(status_code=200, content="dummy binary")
    sut = HtmlAnalyzerFactory()

    expected = sut.create(XUrl("https://maasaablog.com"))
    actual = HtmlAnalyzerImpl()
    assert expected == actual
