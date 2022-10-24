from unittest.mock import MagicMock, patch
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.GCalendar.g_calendar_operator_factory import GCalendarOperatorFactory
from shared.Domain.GCalendar.g_calendar_operator_impl import GCalendarOperatorImpl
from shared.Domain.String.xstr import XStr


@patch("shared.Domain.GCalendar.g_calendar_operator_impl.auth")
def test_テキストファイル操作用インスタンスを生成できる(auth_mock):
    auth_mock.load_credentials_from_file.return_value = [MagicMock()]
    credential_json_file_path = XFileSystemPath(XStr("sample.json"))

    sut = GCalendarOperatorFactory()

    expected = GCalendarOperatorImpl(credential_json_file_path)
    actual = sut.create(credential_json_file_path)
    assert expected == actual
