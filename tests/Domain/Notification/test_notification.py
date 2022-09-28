import pytest
from shared.Domain.Notification.notification import Notification


@pytest.fixture
def setuped_notification():
    return Notification("https://hoge/api/notify", "通知メッセージです")


def test_通知先を設定できる(setuped_notification: Notification):
    expected = "https://hoge/api/notify"
    actual = setuped_notification.destination_url()
    assert expected == actual


def test_通知メッセージを設定できる(setuped_notification: Notification):
    expected = "通知メッセージです"
    actual = setuped_notification.message()
    assert expected == actual


def test_通知メッセージを再設定できる(setuped_notification: Notification):
    expected = "通知メッセージを変更しました"
    actual = setuped_notification.set_message("通知メッセージを変更しました").message()
    assert expected == actual
