import pytest
from shared.Domain.xurl import XUrl
from shared.Application.encode_url_service import EncodeUrlService


@pytest.fixture
def setuped_xurl():
    xurl = XUrl("https://hoge.com/doc/2021/06/20210616004/売り上げ管理書.pdf")
    return xurl


def test_urlをエンコードできること(setuped_xurl: XUrl):

    encoded_url = EncodeUrlService().execute(setuped_xurl)
    assert (
        encoded_url
        == "https%3A//hoge.com/doc/2021/06/20210616004/%E5%A3%B2%E3%82%8A%E4%B8%8A%E3%81%92%E7%AE%A1%E7%90%86%E6%9B%B8.pdf"
    )


# オプション引数safeはクオートしたくないASCII文字を指定できる(デフォルトは、"/")
def test_エンコードしない文字を指定しつつurlをエンコードできること(setuped_xurl: XUrl):

    encoded_url = EncodeUrlService().execute(setuped_xurl, not_escape_ascii="/:")
    assert (
        encoded_url
        == "https://hoge.com/doc/2021/06/20210616004/%E5%A3%B2%E3%82%8A%E4%B8%8A%E3%81%92%E7%AE%A1%E7%90%86%E6%9B%B8.pdf"
    )
