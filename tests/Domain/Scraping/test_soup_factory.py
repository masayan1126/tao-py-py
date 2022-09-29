from unittest.mock import MagicMock, patch
from bs4 import BeautifulSoup
from shared.Domain.Scraping.soup_factory import SoupFactory
from shared.Domain.Url.x_url import XUrl


@patch("shared.Domain.Scraping.soup_factory.requests")
def test_soupオブジェクトを生成できる(mock_requests):
    mock_response = MagicMock(status_code=200, content="dummy binary")
    mock_requests.get.return_value = mock_response

    soup = SoupFactory().create(XUrl("https://maasaablog.com"))

    expected = BeautifulSoup("dummy binary", "html.parser")
    actual = soup
    assert expected == actual
