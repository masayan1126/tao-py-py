from unittest.mock import MagicMock, patch
from shared.Core.Log.log_handler import LogHandler
from shared.Core.Log.log_type import LogType


@patch("shared.Core.Log.log_handler.SlackLogHandler")
def test_slackにログを通知できる_NOTIFICATION(slack_log_handler_mock) -> None:
    handler_mock = MagicMock()
    handler_mock.level = 1
    slack_log_handler_mock.return_value = handler_mock

    sut = LogHandler(LogType.NOTIFICATION, "ログメッセージ1", "package1")

    expected = "Notification to slack"
    actual = sut.to_slack("webhook url1")
    assert expected == actual
