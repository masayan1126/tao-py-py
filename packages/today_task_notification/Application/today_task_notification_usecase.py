from typing import List
from shared.Domain.Calendar.g_calendar_event import GCalendarEvent
from shared.Domain.Notification.line_notification_service import LineNotificationService
from shared.Domain.Notification.notification import Notification
from shared.Domain.Calendar.g_calendar_service import GCalendarService

from shared.Domain.Time.x_date_time import XDateTime


class TodayTaskNotificationUsecase:
    def __init__(
        self, notification: Notification, g_calendar_service: GCalendarService
    ):
        self.notification = notification
        self.g_calendar_service = g_calendar_service

    def notify_to_line(self) -> int:
        # 世界協定時刻（UTC）のISOフォーマットで取得する
        utc_now = XDateTime.utc_now()
        time_min = XDateTime.utc_now().format("%Y-%m-%dT%H:%M:%S%z")
        time_max = utc_now.add_hours(1).format("%Y-%m-%dT%H:%M:%S%z")

        event_list = self.g_calendar_service.fetch_events(
            calendar_id="masa199311266@gmail.com", time_min=time_min, time_max=time_max
        ).all()

        notification = self.notification.set_message(
            self.build_message(event_list=event_list)
        )

        return LineNotificationService(notification).send()

    def build_message(self, event_list: List[GCalendarEvent]) -> str:

        message = ""

        for event in event_list:
            message += "\n" f"{event.summary()}" "\n" ""

        return message
