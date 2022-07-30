import googleapiclient.discovery
import google.auth
from shared.Domain.Calendar.g_calendar_event_converter import GCalendarEventConverter
from shared.Domain.Calendar.g_calendar_events import GCalendarEvents
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from packages.today_task_notification.config import CONFIG


class GCalendarService:
    def __init__(
        self,
        credential_json_file: XFileSystemPath
    ):

        gapi_creds = google.auth.load_credentials_from_file(
            credential_json_file
            .to_absolute()
            .of_text(),
            [CONFIG["CALENDAR_AUTH_ENDPOINT"]],
        )[0]

        self._g_api_service = googleapiclient.discovery.build(
            "calendar", "v3", credentials=gapi_creds
        )

    def g_api_service(self):
        return self._g_api_service

    def fetch_events(self, calendar_id: str, time_min, time_max) -> GCalendarEvents:

        events = (
            self.g_api_service()
            .events()
            .list(
                calendarId=calendar_id,
                timeMin=time_min,
                timeMax=time_max,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()["items"]
        )

        return GCalendarEventConverter.convert(events)
