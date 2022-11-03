from unittest.mock import Mock, patch
from shared.Domain.Notification.line.line_notification_service import (
    LineNotificationService,
)
from shared.Domain.Notification.notification import Notification


@patch("shared.Domain.Notification.line.line_notification_service.requests")
def test_LINEに通知を送信できる(mock_requests):
    mock_response = Mock(status_code=200)
    mock_requests.post.return_value = mock_response

    sut = LineNotificationService(Notification("https://hoge/api/notify", "通知メッセージです"))

    expected = 200
    actual = sut.send("dummy token")
    assert expected == actual
