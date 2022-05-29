from typing import List
from shared.Domain.Calendar.g_calendar_event import GCalendarEvent


class GCalendarEvents:
    def __init__(
        self,
        g_calendar_events: list[GCalendarEvent],
    ):
        self._g_calendar_events = g_calendar_events

    def all(self) -> list[GCalendarEvent]:
        return self._g_calendar_events

    def add(self, g_calendar_event: GCalendarEvent):
        self._g_calendar_events.append(g_calendar_event)
        return self
