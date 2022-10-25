import pytest
from shared.Domain.Url.x_url import XUrl


@pytest.fixture(scope="module")  # module(テストファイル全体で1回実行)
def sut() -> XUrl:
    return XUrl("https://maasaablog.com/development/python/4257/#toc3")


def test_URL全体を取得できる(sut: XUrl) -> None:
    assert "https://maasaablog.com/development/python/4257/#toc3" == sut.url()


def test_スキーマのみ取得できる(sut: XUrl) -> None:
    assert "https" == sut.scheme()


def test_netlocのみ取得できる(sut: XUrl) -> None:
    assert "maasaablog.com" == sut.netloc()


def test_pathのみ取得できる(sut: XUrl) -> None:
    assert "/development/python/4257/" == sut.path()


def test_クエリパラメータのみ取得できる() -> None:
    sut = XUrl("https://maasaablog.com/?p=4069")
    assert "p=4069" == sut.query_params()


def test_fragmentのみ取得できる(sut: XUrl) -> None:
    assert "toc3" == sut.fragment()


def test_基底パスを取得できる(sut: XUrl) -> None:
    assert "https://maasaablog.com/" == sut.baseurl()


def test_基底パスと相対パスを結合できる(sut: XUrl) -> None:
    assert "https://maasaablog.com/python" == sut.join("python").url()


# def test_urlをエンコードできる(sut: XUrl) -> None:
#     decode_url = "https://www.amazon.co.jp/Fire-HD-10-ブラック-64GB/dp/B08F5KJLVL/?_encoding=UTF8&pd_rd_w=EDPLl&content-id=amzn1.sym.a230f60e-db7c-45a3-a34f-6d4e93a68386&pf_rd_p=a230f60e-db7c-45a3-a34f-6d4e93a68386&pf_rd_r=P42E8WH624GCYAR7QQ79&pd_rd_wg=wzxRf&pd_rd_r=c8ae5e0b-95a9-4cd9-8d9c-d37955e36cb7&ref_=pd_gw_unk"

#     assert (
#         "https%3A%2F%2Fwww.amazon.co.jp%2FFire-HD-10-%E3%83%96%E3%83%A9%E3%83%83%E3%82%AF-64GB%2Fdp%2FB08F5KJLVL%2F%3F_encoding%3DUTF8%26pd_rd_w%3DEDPLl%26content-id%3Damzn1.sym.a230f60e-db7c-45a3-a34f-6d4e93a68386%26pf_rd_p%3Da230f60e-db7c-45a3-a34f-6d4e93a68386%26pf_rd_r%3DP42E8WH624GCYAR7QQ79%26pd_rd_wg%3DwzxRf%26pd_rd_r%3Dc8ae5e0b-95a9-4cd9-8d9c-d37955e36cb7%26ref_%3Dpd_gw_unk"
#         == XUrl(decode_url).encode()
#     )


# def test_urlをデコードできる(sut: XUrl) -> None:
#     decode_url = "https://www.amazon.co.jp/Fire-HD-10-ブラック-64GB/dp/B08F5KJLVL/?_encoding=UTF8&pd_rd_w=EDPLl&content-id=amzn1.sym.a230f60e-db7c-45a3-a34f-6d4e93a68386&pf_rd_p=a230f60e-db7c-45a3-a34f-6d4e93a68386&pf_rd_r=P42E8WH624GCYAR7QQ79&pd_rd_wg=wzxRf&pd_rd_r=c8ae5e0b-95a9-4cd9-8d9c-d37955e36cb7&ref_=pd_gw_unk"

#     assert (
#         "https://www.amazon.co.jp/Fire-HD-10-%25E3%2583%2596%25E3%2583%25A9%25E3%2583%2583%25E3%2582%25AF-64GB/dp/B08F5KJLVL/?_encoding=UTF8%2526pd_rd_w=EDPLl%2526content-id=amzn1.sym.a230f60e-db7c-45a3-a34f-6d4e93a68386%2526pf_rd_p=a230f60e-db7c-45a3-a34f-6d4e93a68386%2526pf_rd_r=P42E8WH624GCYAR7QQ79%2526pd_rd_wg=wzxRf%2526pd_rd_r=c8ae5e0b-95a9-4cd9-8d9c-d37955e36cb7%2526ref_=pd_gw_unk"
#         == XUrl(decode_url).encode()
#     )
