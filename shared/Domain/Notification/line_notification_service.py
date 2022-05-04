import requests

from shared.Domain.Notification.notification import Notification


class LineNotificationService:
    def __init__(self, notification: Notification):
        self.notification = notification

    def send(self) -> int:

        headers = {"Authorization": f"Bearer {self.notification.token()}"}
        data = {"message": f"{self.notification.message()}"}
        res = requests.post(
            self.notification.destination_url(), headers=headers, data=data
        )
        return res.status_code
