from dataclasses import dataclass
import requests

from shared.Domain.Notification.notification import Notification


@dataclass
class LineNotificationService:
    notification: Notification

    def send(self, LINE_NOTIFY_TOKEN) -> int:
        if self.notification.message() == "":
            self.notification.set_message("通知するメッセージがありませんでした")

        headers = {"Authorization": f"Bearer {LINE_NOTIFY_TOKEN}"}
        data = {"message": f"{self.notification.message()}"}
        res = requests.post(
            self.notification.destination_url(), headers=headers, data=data
        )
        return res.status_code
