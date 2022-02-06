import pytest
from shared.Domain.xurl import XUrl
from shared.Application.decode_url_service import DecodeUrlService


@pytest.fixture
def setuped_xurl():
    xurl = XUrl("https%3A//hoge.com/doc/2021/06/20210616004/%E5%A3%B2%E3%82%8A%E4%B8%8A%E3%81%92%E7%AE%A1%E7%90%86%E6%9B%B8.pdf")
    return xurl


def test_urlをデコードできること(setuped_xurl: XUrl):

    decoded_url = DecodeUrlService().execute(setuped_xurl)
    assert (
        decoded_url
        == "https://hoge.com/doc/2021/06/20210616004/売り上げ管理書.pdf"
    )
