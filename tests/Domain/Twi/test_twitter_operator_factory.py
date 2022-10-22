from unittest.mock import MagicMock, patch

# モジュールをモックへ差し替えるように追加(Gitリポジトリに存在しないconfigなど)
import sys

from shared.Domain.Twi.twitter_operator_factory_option import (
    TwitterOperatorFactoryOption,
)

config_mock = MagicMock()
config_mock.CONFIG = {
    "CONSUMER_KEY": "CONSUMER_KEY1",
    "CONSUMER_SECRET": "CONSUMER_SECRET1",
    "ACCESS_TOKEN": "ACCESS_TOKEN1",
    "ACCESS_SECRET": "ACCESS_SECRET1",
}
sys.modules["packages.twi_automation.config"] = config_mock

from shared.Domain.Twi.twitter_operator_factory import TwitterOperatorFactory
from shared.Domain.Twi.twitter_operator_impl import TwitterOperatorImpl


# 実際にAPIへ通信しないようにするためだけのMockへの置き換え(そこから何かメソッドを実行したりするわけではない)
@patch("shared.Domain.Twi.twitter_operator_impl.API", return_value=MagicMock())
def test_ツイッターAPI操作用インスタンスを生成できる(mock):
    sut = TwitterOperatorFactory()

    expected = TwitterOperatorImpl(
        "screen_name1", ["black_list_user1", "black_list_user2"]
    )
    actual = sut.create(
        TwitterOperatorFactoryOption(
            "screen_name1", ["black_list_user1", "black_list_user2"]
        )
    )
    assert expected == actual
