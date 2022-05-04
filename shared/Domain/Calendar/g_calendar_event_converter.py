from typing import List
from shared.Domain.Calendar.g_calendar_event import GCalendarEvent
from shared.Domain.Calendar.g_calendar_events import GCalendarEvents


class GCalendarEventConverter:
    def convert(row_events: List) -> GCalendarEvents:

        result = []

        for row_event in row_events:
            result.append(
                GCalendarEvent(
                    id=row_event["id"],
                    summary=row_event["summary"],
                    link=row_event["htmlLink"],
                    start=row_event["start"],
                    end=row_event["end"],
                    created=row_event["created"],
                    updated=row_event["updated"],
                )
            )

        return GCalendarEvents(result)
