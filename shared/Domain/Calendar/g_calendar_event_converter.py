
from shared.Domain.Calendar.g_calendar_event import GCalendarEvent
from shared.Domain.Calendar.g_calendar_events import GCalendarEvents


class GCalendarEventConverter:
    def convert(row_events: list) -> GCalendarEvents:
        return GCalendarEvents(list(
            map(
                lambda row_event: GCalendarEvent(
                    _id=row_event["id"],
                    _summary=row_event["summary"],
                    _link=row_event["htmlLink"],
                    _start=row_event["start"],
                    _end=row_event["end"],
                    _created_at=row_event["created"],
                    _updated_at=row_event["updated"],
                ),
                row_events,
            )
        ))
