import googleapiclient.discovery
import google.auth
from shared.Domain.Calendar.g_calendar_event_converter import GCalendarEventConverter
from shared.Domain.Calendar.g_calendar_events import GCalendarEvents


from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr


class GCalendarService:
    def __init__(
        self,
    ):
        auth_url = ["https://www.googleapis.com/auth/calendar"]

        gapi_creds = google.auth.load_credentials_from_file(
            XFileSystemPath(
                XStr(
                    "packages/today_task_notification/my-daily-task-349202-9456073dfb61.json"
                )
            )
            .to_absolute()
            .of_text(),
            auth_url,
        )[0]

        service = googleapiclient.discovery.build(
            "calendar", "v3", credentials=gapi_creds
        )
        self._service = service

    def service(self):
        return self._service

    def fetch_events(self, calendar_id: str, time_min, time_max) -> GCalendarEvents:

        # TODO: エラーハンドリング(一旦Exception)

        try:
            items = (
                self.service()
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

            return GCalendarEventConverter.convert(items)
        except Exception as e:
            raise e
