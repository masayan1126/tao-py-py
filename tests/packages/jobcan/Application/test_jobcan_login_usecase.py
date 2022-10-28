from unittest.mock import MagicMock, patch


# モジュールをモックへ差し替えるように追加(Gitリポジトリに存在しないconfigなど)
import sys

env_mock = MagicMock()
# config_mock.CONFIG = {
#     "CONSUMER_KEY": "CONSUMER_KEY1",
#     "CONSUMER_SECRET": "CONSUMER_SECRET1",
#     "ACCESS_TOKEN": "ACCESS_TOKEN1",
#     "ACCESS_SECRET": "ACCESS_SECRET1",
# }
sys.modules["packages.jobcan.Application.jobcan_login_usecase.ENV"] = env_mock


# memo: テスト対象のクラスでconfigを使用しているので、mockした後にimportする必要あり
from packages.jobcan.Application.jobcan_login_usecase import JobcanLoginUsecase


@patch("packages.jobcan.Application.jobcan_login_usecase.LoginJobcanReciver")
def test_勤怠システムにログインできる(reciver_mock):
    reciver_mock.return_value = MagicMock()
    JobcanLoginUsecase(MagicMock()).login()

    reciver_mock.call_count == 1
