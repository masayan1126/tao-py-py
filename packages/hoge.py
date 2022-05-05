import googleapiclient.discovery
import google.auth
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr
import datetime


auth_url = ["https://www.googleapis.com/auth/calendar"]

gapi_creds = google.auth.load_credentials_from_file(
    XFileSystemPath(
        XStr("packages/today_task_notification/my-daily-task-349202-9456073dfb61.json")
    )
    .to_absolute()
    .of_text(),
    auth_url,
)[0]


service = googleapiclient.discovery.build("calendar", "v3", credentials=gapi_creds)

utc_now_str = datetime.datetime.utcnow().isoformat()
time_min = utc_now_str + "Z"
time_max = datetime.datetime.fromisoformat(utc_now_str) + datetime.timedelta(seconds=1)

calendar_id = "masa199311266@gmail.com"
events = (
    service.events()
    .list(
        calendarId=calendar_id,
        timeMin=time_min,
        timeMax=f"{time_max.isoformat()}Z",
        singleEvents=True,
        orderBy="startTime",
    )
    .execute()
)

print(events)


# from shared.Domain.Time.x_date_time import XDateTime


# print(XDateTime.utc_now().datetime().isoformat())
# print(XDateTime.now().datetime().isoformat())
