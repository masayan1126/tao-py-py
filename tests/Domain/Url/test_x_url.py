import pytest
from shared.Domain.Url.x_url import XUrl


@pytest.fixture
def setuped_xurl() -> XUrl:
    xurl = XUrl("https://maasaablog.com/development/python/4257/#toc3")
    return xurl


def test_対象のurlオブジェクトからURL全体を取得できること(setuped_xurl: XUrl) -> None:
    assert setuped_xurl.href() == "https://maasaablog.com/development/python/4257/#toc3"


def test_対象のurlオブジェクトからスキーマのみ取得できること(setuped_xurl: XUrl) -> None:
    assert setuped_xurl.scheme() == "https"


def test_対象のurlオブジェクトからnetlocのみ取得できること(setuped_xurl: XUrl) -> None:
    assert setuped_xurl.netloc() == "maasaablog.com"


def test_対象のurlオブジェクトからpathのみ取得できること(setuped_xurl: XUrl) -> None:
    assert setuped_xurl.path() == "/development/python/4257/"


def test_対象のurlオブジェクトからクエリパラメータのみ取得できること() -> None:
    xurl = XUrl("https://maasaablog.com/?p=4069")
    assert xurl.query_params() == "p=4069"


def test_対象のurlオブジェクトからfragmentのみ取得できること(setuped_xurl: XUrl) -> None:
    assert setuped_xurl.fragment() == "toc3"


def test_基底パスを取得できること(setuped_xurl: XUrl) -> None:
    assert setuped_xurl.baseurl() == "https://maasaablog.com/"


def test_基底パスと相対パスを結合できること(setuped_xurl: XUrl) -> None:
    assert setuped_xurl.join("python").href() == "https://maasaablog.com/python"
