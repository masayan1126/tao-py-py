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
def test_URLをデコードできる(mock_quote_method, setuped_x_urls: list[XUrl]):

    mock_quote_method.return_value = setuped_x_urls[0].href()  # decoded_url
    sut = UrlParseService(setuped_x_urls[1])  # encoded_url

    expected = setuped_x_urls[0]
    actual = sut.decode()

    assert expected == actual


@patch("shared.Domain.Url.url_parse_service.urllib.parse.quote")
def test_URLをエンコードできる(mock_quote_method, setuped_x_urls: list[XUrl]):

    mock_quote_method.return_value = setuped_x_urls[1].href()  # encoded_url
    sut = UrlParseService(setuped_x_urls[0])  # decoded_url

    expected = setuped_x_urls[1]
    actual = sut.encode()

    assert expected == actual
