from shared.Core.factory import Factory
from shared.Domain.Twi.twitter_operator import TwitterOperator
from shared.Domain.Twi.twitter_operator_factory_option import (
    TwitterOperatorFactoryOption,
)
from shared.Domain.Twi.twitter_operator_impl import TwitterOperatorImpl


class TwitterOperatorFactory(Factory):
    def create(self, factory_option: TwitterOperatorFactoryOption) -> TwitterOperator:
        return TwitterOperatorImpl(
            factory_option.screen_name(), factory_option.black_list()
        )
