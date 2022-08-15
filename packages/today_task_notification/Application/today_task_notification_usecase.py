from packages.today_task_notification.config import CONFIG
from shared.Domain.Calendar.g_calendar_events import GCalendarEvents
from shared.Domain.Notification.line_notification_service import LineNotificationService
from shared.Domain.Notification.notification import Notification
from shared.Domain.Calendar.g_calendar_service import GCalendarService
from shared.Domain.Time.x_date_time import XDateTime


# グーグルカレンダーから取得した予定をメッセージとして作成し、通知します
class TodayTaskNotificationUsecase:
    def __init__(
        self, notification: Notification, g_calendar_service: GCalendarService
    ):
        self.notification = notification
        self.g_calendar_service = g_calendar_service

    def notify_to_line(self) -> int:
        notification = self.notification.set_message(
            self.build_message(calendar_events=self.calendar_events())
        )

        return LineNotificationService(notification).send()

    def calendar_events(self) -> GCalendarEvents:
        # 世界協定時刻（UTC）のISOフォーマットで取得する
        utc_now = XDateTime.utc_now()
        time_min = XDateTime.utc_now().format("%Y-%m-%dT%H:%M:%S%z")
        time_max = utc_now.add_hours(1).format("%Y-%m-%dT%H:%M:%S%z")

        return self.g_calendar_service.fetch_events(
            calendar_id=CONFIG["CALENDAR_ID"],
            time_min=time_min,
            time_max=time_max,
        )

    def build_message(self, calendar_events: GCalendarEvents) -> str:

        message = ""

        for event in calendar_events.all():
            message += "\n" f"・{event.summary()}" "\n" ""

        return message
