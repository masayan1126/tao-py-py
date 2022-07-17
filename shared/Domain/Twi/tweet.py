from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Tweet:
    _id: int
    _text: str
    _is_contain_media: bool
    _media_list: list

    def id(self) -> int:
        return self._id

    def text(self) -> str:
        return self._text

    def is_contain_media(self) -> bool:
        return self._is_contain_media

    def media_list(self) -> list:
        return self._media_list
