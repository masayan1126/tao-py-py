from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Notification:
    _destination_url: str
    _message: str
    _token: str

    def destination_url(self) -> str:
        return self._destination_url

    def message(self) -> str:
        return self._message

    def set_message(self, message: str) -> Notification:
        self._message = message
        return self

    def token(self) -> str:
        return self._token
