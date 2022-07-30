from dataclasses import dataclass
from shared.Domain.Time.x_date import XDate
from shared.Domain.Time.x_date_time import XDateTime


@dataclass
class GCalendarEvent:
    _id: str
    _summary: str
    _link: str
    _start: dict[str, XDate]
    _end: dict[str, XDate]
    _created_at: XDateTime
    _updated_at: XDateTime

    def id(self) -> str:
        return self._id

    def summary(self) -> str:
        return self._summary

    def link(self) -> str:
        return self._link

    def start(self) -> dict[str, XDate]:
        return self._start

    def end(self) -> dict[str, XDate]:
        return self._end

    def created_at(self) -> XDateTime:
        return self._created_at

    def updated_at(self) -> XDateTime:
        return self._updated_at
