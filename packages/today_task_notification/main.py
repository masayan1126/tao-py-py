from packages.today_task_notification.Application.today_task_notification_usecase import (
    TodayTaskNotificationUsecase,
)
from shared.Domain.Calendar.g_calendar_service import GCalendarService
from shared.Domain.Notification.notification import Notification
from packages.today_task_notification.env import ENV
from packages.today_task_notification.config import CONFIG

LINE_NOTIFY_URL = ENV["LINE_NOTIFY_URL"]
LINE_NOTIFY_TOKEN = CONFIG["LINE_NOTIFY_TOKEN"]

notification = Notification(
    destination_url=LINE_NOTIFY_URL, message="", token=LINE_NOTIFY_TOKEN
)


TodayTaskNotificationUsecase(
    notification=notification,
    g_calendar_service=GCalendarService(),
).notify_to_line()

print("debug")
