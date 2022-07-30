from shared.Domain.Calendar.g_calendar_event import GCalendarEvent
from shared.Domain.List.array_impl import ArrayImpl


class GCalendarEvents(ArrayImpl):
    def __init__(
        self,
        g_calendar_events: list[GCalendarEvent],
    ):
        super().__init__(g_calendar_events)

    def all(self) -> list[GCalendarEvent]:
        return super().all()
        