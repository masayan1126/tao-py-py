from typing import List
from shared.Domain.Calendar.g_calendar_event import GCalendarEvent
from shared.Domain.Notification.line_notification_service import LineNotificationService
from shared.Domain.Notification.notification import Notification
from shared.Domain.Calendar.g_calendar_service import GCalendarService
import datetime


class TodayTaskNotificationUsecase:
    def __init__(
        self, notification: Notification, g_calendar_service: GCalendarService
    ):
        self.notification = notification
        self.g_calendar_service = g_calendar_service

    def notify_to_line(self) -> int:
        # Googleカレンダーからイベントを取得する
        # 現在時刻を世界協定時刻（UTC）のISOフォーマットで取得する
        utc_now_str = datetime.datetime.utcnow().isoformat()
        time_min = utc_now_str + "Z"
        time_max = datetime.datetime.fromisoformat(utc_now_str) + datetime.timedelta(
            hours=1
        )

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
