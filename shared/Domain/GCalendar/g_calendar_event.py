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

    # dataclassを使用しているので、initは不要だが、_なしの変数名で外から受け取り、_付きでprivate変数として定義したいので、記述している
    def __init__(
        self,
        id: str,
        summary: str,
        link: str,
        start: dict[str, XDate],
        end: dict[str, XDate],
        created_at: XDateTime,
        updated_at: XDateTime,
    ):

        self._id = id
        self._summary = summary
        self._link = link
        self._start = start
        self._end = end
        self._created_at = created_at
        self._updated_at = updated_at

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
