from shared.Domain.GCalendar.g_calendar_event import GCalendarEvent
import pytest
from shared.Domain.GCalendar.g_calendar_event_converter import GCalendarEventConverter
from shared.Domain.GCalendar.g_calendar_events import GCalendarEvents
from shared.Domain.Time.x_date import XDate
from shared.Domain.Time.x_date_time import XDateTime


@pytest.fixture
def g_calendar_events():

    return GCalendarEvents(
        [
            GCalendarEvent(
                id="id1",
                summary="予定1",
                link="link1",
                start={"date": XDate("2022-10-01")},
                end={"date": XDate("2022-10-02")},
                created_at=XDateTime("2022-10-01"),
                updated_at=XDateTime("2022-10-01"),
            ),
            GCalendarEvent(
                id="id2",
                summary="予定2",
                link="link2",
                start={"date": XDate("2022-10-02")},
                end={"date": XDate("2022-10-03")},
                created_at=XDateTime("2022-10-02"),
                updated_at=XDateTime("2022-10-02"),
            ),
        ]
    )


def test_フェッチしたグーグルカレンダーオブジェクトのリストを整形できる(
    g_calendar_events: GCalendarEvents,
) -> None:
    row_events = [
        {
            "id": "id1",
            "htmlLink": "link1",
            "created": XDateTime("2022-10-01"),
            "updated": XDateTime("2022-10-01"),
            "summary": "予定1",
            "start": {"date": XDate("2022-10-01")},
            "end": {"date": XDate("2022-10-02")},
        },
        {
            "id": "id2",
            "htmlLink": "link2",
            "created": XDateTime("2022-10-02"),
            "updated": XDateTime("2022-10-02"),
            "summary": "予定2",
            "start": {"date": XDate("2022-10-02")},
            "end": {"date": XDate("2022-10-03")},
        },
    ]

    sut = GCalendarEventConverter

    expected = g_calendar_events
    actual = sut.from_row(row_events)

    assert expected == actual
