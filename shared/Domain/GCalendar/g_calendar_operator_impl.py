from dataclasses import dataclass
from googleapiclient.discovery import Resource
from googleapiclient import discovery
import google.auth
from shared.Core.Log.log_handler import LogHandler
from shared.Core.Log.log_type import LogType
from shared.Domain.GCalendar.g_calendar_event_converter import GCalendarEventConverter
from shared.Domain.GCalendar.g_calendar_events import GCalendarEvents
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from packages.today_task_notification.config import CONFIG
from shared.Domain.GCalendar.g_calendar_operator import GCalendarOperator
from packages.twi_automation.env import ENV


class GCalendarOperatorImpl(GCalendarOperator):
    def __init__(self, credential_json_file: XFileSystemPath):

        credentials = google.auth.load_credentials_from_file(
            credential_json_file.to_absolute().of_text(),
            [CONFIG["CALENDAR_AUTH_ENDPOINT"]],
        )[0]

        self._api_client = discovery.build("calendar", "v3", credentials=credentials)

    def fetch_events(self, calendar_id: str, time_min, time_max) -> GCalendarEvents:
        return GCalendarEventConverter.from_row(
            self.row_events(calendar_id, time_min, time_max)
        )

    def row_events(self, calendar_id: str, time_min, time_max):
        resource: Resource = self.api_client().events()

        return resource.list(
            calendarId=calendar_id,
            timeMin=time_min,
            timeMax=time_max,
            singleEvents=True,
            orderBy="startTime",
        ).execute()["items"]

    def api_client(self):
        return self._api_client
