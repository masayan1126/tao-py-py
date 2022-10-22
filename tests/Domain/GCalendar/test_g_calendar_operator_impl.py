from shared.Domain.GCalendar.g_calendar_event import GCalendarEvent
import pytest
from shared.Domain.GCalendar.g_calendar_event_converter import GCalendarEventConverter
from shared.Domain.GCalendar.g_calendar_events import GCalendarEvents
from shared.Domain.Time.x_date import XDate
from shared.Domain.Time.x_date_time import XDateTime
from unittest.mock import MagicMock, patch
import pytest
from shared.Domain.GCalendar.g_calendar_operator_factory import GCalendarOperatorFactory
from shared.Domain.GCalendar.g_calendar_operator_impl import GCalendarOperatorImpl


@pytest.fixture
def g_calendar_event_list():

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


@patch.object(GCalendarOperatorImpl, "_api_client")
@patch("shared.Domain.GCalendar.g_calendar_operator_impl.auth")
def test_fetch_events(auth_mock, g_calendar_api_mock) -> None:

    auth_mock.load_credentials_from_file.return_value = [MagicMock()]

    row_events = {
        "items": [
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
    }

    # mockのキャプチャ：　api_client().events().list().execute().__getitem__()
    mock1 = MagicMock()
    mock1.execute.return_value = row_events
    resouce_mock = MagicMock()
    resouce_mock.list.return_value = mock1
    mock2 = MagicMock()
    mock2.events.return_value = resouce_mock
    g_calendar_api_mock.return_value = mock2

    sut = GCalendarOperatorFactory().create()

    expected = GCalendarEventConverter.from_row(row_events["items"])
    actual = sut.fetch_events(
        calendar_id="calendar_id1",
        time_min="time_min1",
        time_max="time_max1",
    )

    assert expected == actual
