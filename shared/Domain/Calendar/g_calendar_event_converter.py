
from shared.Domain.Calendar.g_calendar_event import GCalendarEvent
from shared.Domain.Calendar.g_calendar_events import GCalendarEvents


class GCalendarEventConverter:
    def convert(row_events: list) -> GCalendarEvents:
        return GCalendarEvents(list(
            map(
                lambda row_event: GCalendarEvent(
                    id=row_event["id"],
                    summary=row_event["summary"],
                    link=row_event["htmlLink"],
                    start=row_event["start"],
                    end=row_event["end"],
                    created_at=row_event["created"],
                    updated_at=row_event["updated"],
                ),
                row_events,
            )
        ))
