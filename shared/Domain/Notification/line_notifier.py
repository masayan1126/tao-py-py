import requests


class LineNotifier:
    def __init__(self, line_notify_token: str, line_notify_url: str):
        self.line_notify_token = line_notify_token
        self.line_notify_url = line_notify_url

    def send(self, notification_message):

        headers = {"Authorization": f"Bearer {self.line_notify_token}"}
        data = {"message": f"{notification_message}"}
        requests.post(self.line_notify_url, headers=headers, data=data)
