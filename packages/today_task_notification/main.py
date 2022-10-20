from packages.today_task_notification.Application.today_task_notify_to_line_usecase import (
    TodayTaskNotifyToLineUsecase,
)
from shared.Domain.Notification.notification import Notification
from packages.today_task_notification.env import ENV


TodayTaskNotifyToLineUsecase(
    notification=Notification(ENV["LINE_NOTIFY_URL"]),
).to_line()
