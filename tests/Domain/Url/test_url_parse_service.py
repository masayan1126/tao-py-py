from unittest.mock import patch
import pytest
from shared.Domain.Url.x_url import XUrl
from shared.Domain.Url.url_parse_service import UrlParseService


@pytest.fixture
def setuped_x_urls():

    decoded = "https://maasaablog.com/development/typescript/5098/"
    encoded = "https%3A%2F%2Fmaasaablog.com%2Fdevelopment%2Ftypescript%2F5098%2F"

    return [XUrl(decoded), XUrl(encoded)]


@patch("shared.Domain.Url.url_parse_service.urllib.parse.unquote")
def test_URLをデコードできること(mock_quote_method, setuped_x_urls: list[XUrl]):

    mock_quote_method.return_value = setuped_x_urls[0].href()

    expected = setuped_x_urls[0]
    actual = UrlParseService(setuped_x_urls[1]).decode()

    assert expected == actual


@patch("shared.Domain.Url.url_parse_service.urllib.parse.quote")
def test_URLをエンコードできること(mock_quote_method, setuped_x_urls: list[XUrl]):

    mock_quote_method.return_value = setuped_x_urls[1].href()

    expected = setuped_x_urls[1]
    actual = UrlParseService(setuped_x_urls[0]).encode()

    assert expected == actual
