from shared.Domain.GCalendar.g_calendar_event import GCalendarEvent
import pytest
from shared.Domain.GCalendar.g_calendar_events import GCalendarEvents
from shared.Domain.Time.x_date import XDate
from shared.Domain.Time.x_date_time import XDateTime


@pytest.fixture
def g_calendar_event_list():

    return [
        GCalendarEvent(
            id=1,
            summary="summary1",
            link="link1",
            start={"date": XDate("2022-10-01")},
            end={"date": XDate("2022-10-01")},
            created_at=XDateTime("2022-10-01"),
            updated_at=XDateTime("2022-10-01"),
        ),
        GCalendarEvent(
            id=2,
            summary="summary2",
            link="link2",
            start={"date": XDate("2022-10-02")},
            end={"date": XDate("2022-10-02")},
            created_at=XDateTime("2022-10-02"),
            updated_at=XDateTime("2022-10-02"),
        ),
        GCalendarEvent(
            id=3,
            summary="summary3",
            link="link3",
            start={"date": XDate("2022-10-03")},
            end={"date": XDate("2022-10-03")},
            created_at=XDateTime("2022-10-03"),
            updated_at=XDateTime("2022-10-03"),
        ),
    ]


def test_グーグルカレンダーオブジェクトのリスト(g_calendar_event_list: list[GCalendarEvent]) -> None:
    sut = GCalendarEvents(g_calendar_event_list)

    expected = g_calendar_event_list
    actual = sut.all()

    assert expected == actual


def test_グーグルカレンダーオブジェクトの写像(g_calendar_event_list: list[GCalendarEvent]) -> None:
    sut = GCalendarEvents(g_calendar_event_list)

    expected = [
        g_calendar_event.summary() for g_calendar_event in g_calendar_event_list
    ]
    actual = sut.map(lambda g_calendar_event: g_calendar_event.summary()).all()

    assert expected == actual
