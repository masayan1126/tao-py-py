from shared.Core.factory import Factory
from shared.Domain.Url.x_url import XUrl
from shared.Domain.Wp.wp_operator import WpOperator
from shared.Domain.Wp.wp_operator_impl import WpOperatorImpl


class WpOperatorFactory(Factory):
    def create(self, url: XUrl) -> WpOperator:
        return WpOperatorImpl(url)
