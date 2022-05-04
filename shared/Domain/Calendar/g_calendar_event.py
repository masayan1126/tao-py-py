from typing import Dict
from shared.Domain.Time.x_date import XDate

from shared.Domain.Time.x_date_time import XDateTime


class GCalendarEvent:
    def __init__(
        self,
        id: str,
        summary: str,
        link: str,
        start: Dict[str, XDate],
        end: Dict[str, XDate],
        created: XDateTime,
        updated: XDateTime,
    ):
        self._id = id
        self._summary = summary
        self._link = link
        self._start = start
        self._end = end
        self._created = created
        self._updated = updated

    def id(self) -> str:
        return self._id

    def summary(self) -> str:
        return self._summary

    def link(self) -> str:
        return self._link

    def start(self) -> Dict[str, XDate]:
        return self._start

    def end(self) -> Dict[str, XDate]:
        return self._end

    def created(self) -> XDateTime:
        return self._created

    def updated(self) -> XDateTime:
        return self._updated
