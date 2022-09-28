from unittest.mock import Mock, patch
import pytest
from shared.Domain.Notification.line.line_notification_service import (
    LineNotificationService,
)
from shared.Domain.Notification.notification import Notification
from packages.today_task_notification.config import CONFIG


@patch("shared.Domain.Notification.line.line_notification_service.requests")
def test_LINEに通知を送信できる(mock_requests):
    mock_response = Mock(status_code=200)
    mock_requests.post.return_value = mock_response

    line_notification_service = LineNotificationService(
        Notification("https://hoge/api/notify", "通知メッセージです")
    )

    expected = 200
    actual = line_notification_service.send(CONFIG["LINE_NOTIFY_TOKEN"])
    assert expected == actual
