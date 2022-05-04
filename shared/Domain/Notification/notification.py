class Notification:
    def __init__(self, destination_url: str, message: str = "", token: str = ""):
        self._destination_url = destination_url
        self._message = message
        self._token = token

    def destination_url(self) -> str:
        return self._destination_url

    def message(self) -> str:
        return self._message

    def set_message(self, message: str):
        self._message = message
        return self

    def token(self) -> str:
        return self._token
