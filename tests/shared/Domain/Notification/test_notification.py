import pytest
from shared.Domain.Notification.notification import Notification


@pytest.fixture
def sut():
    return Notification("https://hoge/api/notify", "通知メッセージです")


def test_通知先を設定できる(sut: Notification):
    expected = "https://hoge/api/notify"
    actual = sut.destination_url()
    assert expected == actual


def test_通知メッセージを設定できる(sut: Notification):
    expected = "通知メッセージです"
    actual = sut.message()
    assert expected == actual


def test_通知メッセージを再設定できる(sut: Notification):
    expected = "通知メッセージを変更しました"
    actual = sut.set_message("通知メッセージを変更しました").message()
    assert expected == actual
