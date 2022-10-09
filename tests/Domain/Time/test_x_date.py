import datetime
import pytest
from shared.Domain.Time.x_date import XDate


@pytest.fixture
def sut() -> XDate:
    return XDate("2022-12-29")


def test_日付オブジェクトを生成できる(sut: XDate) -> None:
    expected = XDate("2022-12-29")
    actual = sut

    assert expected == actual


def test_日付オブジェクトを生成できる_ISO8601形式でない場合は例外() -> None:
    with pytest.raises(ValueError):
        XDate("2022/12/29")


def test_日付オブジェクトをフォーマットできる(sut: XDate) -> None:
    expected = "2022/12/29"
    actual = sut.format("%Y/%m/%d")

    assert expected == actual


def test_日付オブジェクトから年を取得できる(sut: XDate) -> None:
    expected = "2022"
    actual = sut.year()

    assert expected == actual


def test_日付オブジェクトから月を取得できる(sut: XDate) -> None:
    expected = "12"
    actual = sut.month()

    assert expected == actual


def test_日付オブジェクトから日を取得できる(sut: XDate) -> None:
    expected = "29"
    actual = sut.day()

    assert expected == actual


def test_今日の日付オブジェクトを生成できる(sut: XDate) -> None:
    expected = datetime.date.today().strftime("%Y/%m/%d")
    actual = sut.today().format("%Y/%m/%d")

    assert expected == actual


def test_指定月の月末日を取得できる(sut: XDate) -> None:
    expected = "2022/04/30"
    actual = sut.last_day_of_month(2022, 4).format("%Y/%m/%d")

    assert expected == actual
