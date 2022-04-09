from shared.Application.check_is_valid_url_service import CheckIsValidUrlService
from shared.Domain.xurl import XUrl


def test_任意のurlが有効かどうかチェックできること():

    x_url = XUrl("https://maasaablog.com/")
    is_valid_url = CheckIsValidUrlService().handle(xurl=x_url)
    assert is_valid_url


def test_無効なurlの場合はFalseを返すこと():

    x_url = XUrl("https://hfefejjekfogehoge.com/")
    is_valid_url = CheckIsValidUrlService().handle(xurl=x_url)
    assert not is_valid_url
