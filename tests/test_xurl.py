import pytest
from shared.Domain.xurl import XUrl


@pytest.fixture
def setuped_xurl():
    xurl = XUrl("https://maasaablog.com/development/python/3795/#toc2")
    return xurl


def test_対象のurlからスキーマのみ取得できること(setuped_xurl: XUrl):
    assert setuped_xurl.get_scheme() == "https"


def test_対象のurlからnetlocのみ取得できること(setuped_xurl: XUrl):
    assert setuped_xurl.get_netloc() == "maasaablog.com"


def test_対象のurlからpathのみ取得できること(setuped_xurl: XUrl):
    assert setuped_xurl.get_path() == "/development/python/3795/"


def test_対象のurlからパラメータのみ取得できること(setuped_xurl: XUrl):
    assert setuped_xurl.get_params() == ""


def test_対象のurlからfragmentのみ取得できること(setuped_xurl: XUrl):
    assert setuped_xurl.get_fragment() == "toc2"


def test_基底パスを取得できること(setuped_xurl: XUrl):
    assert setuped_xurl.get_baseurl() == "https://maasaablog.com/"


def test_基底パスと相対パスを結合できること(setuped_xurl: XUrl):
    assert setuped_xurl.join_to("hoge") == "https://maasaablog.com/hoge"
