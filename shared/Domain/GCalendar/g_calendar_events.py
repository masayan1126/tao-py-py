from __future__ import annotations
from dataclasses import dataclass
from typing import Callable
from shared.Domain.GCalendar.g_calendar_event import GCalendarEvent
from shared.Core.abstract_array import AbstractArray


@dataclass
class GCalendarEvents(AbstractArray):
    _g_calendar_events: list[GCalendarEvent]

    def __init__(self, g_calendar_events: list[GCalendarEvent]):
        super().__init__(g_calendar_events)
        self._g_calendar_events = g_calendar_events

    def all(self) -> list[GCalendarEvent]:
        return super().all()

    def map(self, callable: Callable) -> GCalendarEvents:
        mapped = list(
            map(
                callable,
                self.all(),
            )
        )
        return GCalendarEvents(mapped)
