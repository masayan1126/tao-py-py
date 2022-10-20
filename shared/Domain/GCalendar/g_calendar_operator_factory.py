from shared.Core.factory import Factory
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.GCalendar.g_calendar_operator import GCalendarOperator
from shared.Domain.GCalendar.g_calendar_operator_impl import GCalendarOperatorImpl
from shared.Domain.String.xstr import XStr


class GCalendarOperatorFactory(Factory):
    def create(self) -> GCalendarOperator:
        path = XFileSystemPath(
            XStr(
                "packages/today_task_notification/my-daily-task-349202-9456073dfb61.json"
            )
        )

        return GCalendarOperatorImpl(path)
