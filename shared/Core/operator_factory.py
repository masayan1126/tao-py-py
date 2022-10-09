from shared.Core.factory import Factory
from shared.Core.operator_type import OperatorType
from shared.Domain.Twi.twitter_operator_impl import TwitterOperatorImpl


class OperatorFactory(Factory):
    def create(self, type: OperatorType):
        if type is OperatorType.TWI:
            return TwitterOperatorImpl()
        elif type is OperatorType.TEXTFILE:
            pass
        elif type is OperatorType.WP:
            pass
        elif type is OperatorType.GUI:
            pass
        elif type is OperatorType.BROWSER:
            pass
        elif type is OperatorType.HTML:
            pass
