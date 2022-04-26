import pytest
from shared.Domain.Url.x_url import XUrl
from shared.Application.url_encoder import UrlEncoder


@pytest.fixture
def setuped_x_url() -> XUrl:
    return XUrl("https://maasaablog.com/python/")


def test_urlをエンコードできること(setuped_x_url: XUrl):

    encoded_url = UrlEncoder().encode(setuped_x_url)
    assert encoded_url == "https%3A//maasaablog.com/python/"


# オプション引数safeはクオートしたくないASCII文字を指定できる(デフォルトは、"/")
def test_エンコードしない文字を指定できること(setuped_x_url: XUrl):

    # デフォルトの/に加えて、:をエンコードしない
    encoded_url = UrlEncoder().encode(setuped_x_url, not_escape_ascii="/:")
    assert encoded_url == "https://maasaablog.com/python/"
