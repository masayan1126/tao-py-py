from shared.Core.factory import Factory
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.GCalendar.g_calendar_operator import GCalendarOperator
from shared.Domain.GCalendar.g_calendar_operator_impl import GCalendarOperatorImpl


class GCalendarOperatorFactory(Factory):
    def create(self, credential_json_path: XFileSystemPath) -> GCalendarOperator:
        return GCalendarOperatorImpl(credential_json_path)
