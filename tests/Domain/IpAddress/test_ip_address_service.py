from unittest.mock import MagicMock, patch
from shared.Domain.IpAddress.ip_address_service import IpAddressService
from shared.Domain.Scraping.html_analyzer_factory import (
    HtmlAnalyzerFactory,
)
from shared.Domain.Url.x_url import XUrl


@patch("shared.Domain.Scraping.html_analyzer_factory.requests")
@patch("shared.Domain.Scraping.html_analyzer_impl.BeautifulSoup.select")
def test_今日のIPアドレスを取得できる(mock_bs4_select_method, mock_requests) -> None:

    mock_requests.get.return_value = MagicMock(status_code=200, content="dummy binary")

    mock_bs4_select_method.return_value = [
        MagicMock(text="あなたの情報（確認くん）"),  # ResultsetMock
        MagicMock(text="192.0.2.12"),
        MagicMock(text="192-0-2-12f1.kyt1.eonet.ne.jp"),
        MagicMock(text="Copyright (C) 1997-"),
    ]

    html_analyzer = HtmlAnalyzerFactory().create(XUrl("https://maasaablog.com"))

    sut = IpAddressService(html_analyzer)

    expected = "192.0.2.12"
    actual = sut.get_today_ip().value()

    assert expected == actual
