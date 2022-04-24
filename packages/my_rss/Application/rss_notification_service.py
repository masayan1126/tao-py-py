from shared.Domain.Notification.line_notifier import LineNotifier


class RssNotificationService:
    def __init__(self, line_notify_token: str, line_notify_url: str):
        self.line_notify_token = line_notify_token
        self.line_notify_url = line_notify_url

    def send(self, message: str):
        LineNotifier(
            line_notify_token=self.line_notify_token,
            line_notify_url=self.line_notify_url,
        ).send(message)
