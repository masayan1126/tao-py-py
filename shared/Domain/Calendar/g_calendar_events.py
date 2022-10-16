from __future__ import annotations
from typing import Callable
from shared.Domain.Calendar.g_calendar_event import GCalendarEvent
from shared.Domain.Array.abstract_array import AbstractArray


class GCalendarEvents(AbstractArray):
    def __init__(
        self,
        g_calendar_events: list[GCalendarEvent],
    ):
        super().__init__(g_calendar_events)

    def all(self) -> list[GCalendarEvent]:
        return super().all()

    def map(self, callable: Callable) -> GCalendarEvents:
        super().map(callable)
        return self
