from unittest.mock import MagicMock, patch
from packages.jobcan.Application.jobcan_login_usecase import JobcanLoginUsecase


@patch("packages.jobcan.Application.jobcan_login_usecase.LoginJobcanReciver")
def test_勤怠システムにログインできる(reciver_mock):
    reciver_mock.return_value = MagicMock()
    JobcanLoginUsecase(MagicMock()).login()

    reciver_mock.call_count == 1
