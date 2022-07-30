from packages.today_task_notification.Application.today_task_notification_usecase import (
    TodayTaskNotificationUsecase,
)

from shared.Domain.Calendar.g_calendar_service import GCalendarService
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.Log.x_logger import XLogger
from shared.Domain.Notification.notification import Notification
from packages.today_task_notification.env import ENV
from packages.today_task_notification.config import CONFIG
from shared.Domain.String.xstr import XStr

LINE_NOTIFY_URL = ENV["LINE_NOTIFY_URL"]
LINE_NOTIFY_TOKEN = CONFIG["LINE_NOTIFY_TOKEN"]

notification = Notification(LINE_NOTIFY_URL, "", LINE_NOTIFY_TOKEN)

try:
    TodayTaskNotificationUsecase(
        notification=notification,
        g_calendar_service=GCalendarService(XFileSystemPath(
            XStr(
                "packages/today_task_notification/my-daily-task-349202-9456073dfb61.json"
            )
        )),
    ).notify_to_line()
except Exception as e:
    XLogger.exception_to_slack(
        ENV["SLACK_WEBHOOK_URL_MY_TASK"],
        e,
    )
