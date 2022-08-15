import pytest
from shared.Domain.Url.x_url import XUrl
from urllib.error import HTTPError


@pytest.fixture
def setuped_xurl() -> XUrl:
    xurl = XUrl("https://maasaablog.com/development/python/4257/#toc3")
    return xurl


def test_対象のurlオブジェクトからスキーマのみ取得できること(setuped_xurl: XUrl) -> None:
    assert setuped_xurl.href() == "https://maasaablog.com/development/python/4257/#toc3"


# 404
def test_対象のurlが存在しない場合は例外() -> None:
    with pytest.raises(HTTPError):
        XUrl("https://maasaablog.com/development/hoge")


# 403
def test_対象のurlが存在しても権限がない等の場合は例外() -> None:
    with pytest.raises(HTTPError):
        XUrl("https://www.meti.go.jp/press/2021/06/20210616004/20210616004-1.pdf")


#
def test_対象のurlが存在してもマルチバイトを含む場合は例外() -> None:
    with pytest.raises(UnicodeEncodeError):
        XUrl(
            "https://www.amazon.co.jp/アイリスオーヤマ-カラーマスク-DAILY-ふつうサイズ-RK-D5MG/dp/B099ZP5LBY/ref=zg-bs_industrial_5/356-8867929-7764050?pd_rd_w=PRDtk&pf_rd_p=061993fb-1a08-486a-9bea-d772d463ba7a&pf_rd_r=3JFJKTEWTA4908KTBXS8&pd_rd_r=b8df20d8-3ec3-451b-8ef7-3cde2a821296&pd_rd_wg=qgkij&pd_rd_i=B09SX36HPS&psc=1"
        )


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
