from abc import ABCMeta, abstractmethod
from shared.Domain.GCalendar.g_calendar_events import GCalendarEvents


# グーグルカレンダー操作用インターフェース


class GCalendarOperator(metaclass=ABCMeta):
    @abstractmethod
    def fetch_events(self, calendar_id: str, time_min, time_max) -> GCalendarEvents:
        pass
