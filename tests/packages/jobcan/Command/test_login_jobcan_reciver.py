from unittest.mock import MagicMock, patch
from packages.jobcan.Command.login_jobcan_reciver import LoginJobcanReciver


@patch("packages.jobcan.Command.login_jobcan_reciver.WebBrowserOperator")
def test_勤怠システムへのログインコマンド用レシーバー(operator_mock):
    operator_mock.find_by_id.return_value = MagicMock()

    sut = LoginJobcanReciver(operator_mock)
    sut.action()

    assert operator_mock.find_by_id.call_count == 2
    operator_mock.find_by_id.assert_any_call(id_name="user_email")

    assert operator_mock.send_value.call_count == 1
    operator_mock.find_by_xpath.assert_called_once_with(
        xpath="//*[@id='new_user']/input[2]"
    )

    assert operator_mock.find_by_xpath.call_count == 1
    operator_mock.find_by_xpath.assert_called_once_with(
        xpath="//*[@id='new_user']/input[2]"
    )
