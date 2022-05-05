# import pytest
# from shared.Domain.Url.x_url import XUrl
# from shared.Domain.Url.decode_url_service import DecodeUrlService


# @pytest.fixture
# def setuped_x_url() -> XUrl:
#     return XUrl(
#         "https://www.amazon.co.jp/%E3%82%A2%E3%82%A4%E3%83%AA%E3%82%B9%E3%82%AA%E3%83%BC%E3%83%A4%E3%83%9E-%E3%82%AB%E3%83%A9%E3%83%BC%E3%83%9E%E3%82%B9%E3%82%AF-DAILY-%E3%81%B5%E3%81%A4%E3%81%86%E3%82%B5%E3%82%A4%E3%82%BA-RK-D5MG/dp/B099ZP5LBY/ref=zg-bs_industrial_5/356-8867929-7764050?pd_rd_w=PRDtk&pf_rd_p=061993fb-1a08-486a-9bea-d772d463ba7a&pf_rd_r=3JFJKTEWTA4908KTBXS8&pd_rd_r=b8df20d8-3ec3-451b-8ef7-3cde2a821296&pd_rd_wg=qgkij&pd_rd_i=B09SX36HPS&psc=1"
#     )


# def test_urlをデコードできること(setuped_x_url: XUrl):

#     # たまに503エラーになるときがある
#     decoded_url = DecodeUrlService().decode(setuped_x_url)
#     assert (
#         decoded_url
#         == "https://www.amazon.co.jp/アイリスオーヤマ-カラーマスク-DAILY-ふつうサイズ-RK-D5MG/dp/B099ZP5LBY/ref=zg-bs_industrial_5/356-8867929-7764050?pd_rd_w=PRDtk&pf_rd_p=061993fb-1a08-486a-9bea-d772d463ba7a&pf_rd_r=3JFJKTEWTA4908KTBXS8&pd_rd_r=b8df20d8-3ec3-451b-8ef7-3cde2a821296&pd_rd_wg=qgkij&pd_rd_i=B09SX36HPS&psc=1"
#     )
