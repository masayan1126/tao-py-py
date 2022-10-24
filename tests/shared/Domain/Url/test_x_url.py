import pytest
from shared.Domain.Url.x_url import XUrl


@pytest.fixture
def sut() -> XUrl:
    return XUrl("https://maasaablog.com/development/python/4257/#toc3")


def test_対象のurlオブジェクトからURL全体を取得できる(sut: XUrl) -> None:
    assert sut.href() == "https://maasaablog.com/development/python/4257/#toc3"


def test_対象のurlオブジェクトからスキーマのみ取得できる(sut: XUrl) -> None:
    assert sut.scheme() == "https"


def test_対象のurlオブジェクトからnetlocのみ取得できる(sut: XUrl) -> None:
    assert sut.netloc() == "maasaablog.com"


def test_対象のurlオブジェクトからpathのみ取得できる(sut: XUrl) -> None:
    assert sut.path() == "/development/python/4257/"


def test_対象のurlオブジェクトからクエリパラメータのみ取得できる() -> None:
    xurl = XUrl("https://maasaablog.com/?p=4069")
    assert xurl.query_params() == "p=4069"


def test_対象のurlオブジェクトからfragmentのみ取得できる(sut: XUrl) -> None:
    assert sut.fragment() == "toc3"


def test_基底パスを取得できる(sut: XUrl) -> None:
    assert sut.baseurl() == "https://maasaablog.com/"


def test_基底パスと相対パスを結合できる(sut: XUrl) -> None:
    assert sut.join("python").href() == "https://maasaablog.com/python"
