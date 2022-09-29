from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Post:
    _id: int
    _status: str
    _link: str
    _title: str

    def id(self) -> int:
        return self._id

    def status(self) -> str:
        return self._status

    def link(self) -> str:
        return self._link

    def title(self) -> str:
        return self._title
