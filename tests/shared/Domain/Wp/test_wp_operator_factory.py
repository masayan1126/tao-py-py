from shared.Domain.Url.x_url import XUrl
from shared.Domain.Wp.wp_operator_factory import WpOperatorFactory
from shared.Domain.Wp.wp_operator_impl import WpOperatorImpl


def test_ワードプレス操作用インスタンスを生成できる():
    url = XUrl("https://hogefooavr.com/wp-json/wp/v2/posts")
    sut = WpOperatorFactory()

    expected = WpOperatorImpl(url)
    actual = sut.create(url)
    assert expected == actual
