from packages.today_task_notification.Application.today_task_notify_to_line_usecase import (
    TodayTaskNotifyToLineUsecase,
)

from shared.Domain.Calendar.g_calendar_service import GCalendarService
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.Notification.notification import Notification
from packages.today_task_notification.env import ENV
from shared.Domain.String.xstr import XStr


notification = Notification(ENV["LINE_NOTIFY_URL"])

TodayTaskNotifyToLineUsecase(
    g_calendar_service=GCalendarService(
        XFileSystemPath(
            XStr(
                "packages/today_task_notification/my-daily-task-349202-9456073dfb61.json"
            )
        )
    ),
    notification=notification,
).to_line()
