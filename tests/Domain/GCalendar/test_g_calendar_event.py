from shared.Domain.GCalendar.g_calendar_event import GCalendarEvent
import pytest
from shared.Domain.Time.x_date import XDate
from shared.Domain.Time.x_date_time import XDateTime


@pytest.fixture
def sut():
    return GCalendarEvent(
        id=1,
        summary="summary1",
        link="link1",
        start={"date": XDate("2022-10-01")},
        end={"date": XDate("2022-10-01")},
        created_at=XDateTime("2022-10-01"),
        updated_at=XDateTime("2022-10-01"),
    )


def test_グーグルカレンダーオブジェクト(sut: GCalendarEvent) -> None:
    assert 1 == sut.id()
    assert "summary1" == sut.summary()
    assert "link1" == sut.link()
    assert {"date": XDate("2022-10-01")} == sut.start()
    assert {"date": XDate("2022-10-01")} == sut.end()
    assert XDateTime("2022-10-01") == sut.created_at()
    assert XDateTime("2022-10-01") == sut.updated_at()
