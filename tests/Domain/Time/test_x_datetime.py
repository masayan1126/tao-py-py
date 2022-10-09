import datetime
import pytest
from shared.Domain.Time.x_date import XDate
from shared.Domain.Time.x_date_time import XDateTime


@pytest.fixture
def sut() -> XDateTime:
    return XDateTime("2022-12-29 23:10:45")


def test_日時オブジェクトを生成できる(sut: XDateTime) -> None:
    expected = "2022-12-29T23:10:45"
    actual = sut.text_of()

    assert expected == actual


def test_日時オブジェクトを生成できる_ISO8601形式でない場合は例外() -> None:
    with pytest.raises(ValueError):
        XDateTime("2022/12/29")


def test_日時オブジェクトをフォーマットできる(sut: XDateTime) -> None:
    expected = "2022/12/29T23:10:45"
    actual = sut.format("%Y/%m/%dT%H:%M:%S")

    assert expected == actual


def test_日時オブジェクトから年を取得できる(sut: XDateTime) -> None:
    expected = "2022"
    actual = sut.year()

    assert expected == actual


def test_日時オブジェクトから月を取得できる(sut: XDateTime) -> None:
    expected = "12"
    actual = sut.month()

    assert expected == actual


def test_日時オブジェクトから日を取得できる(sut: XDateTime) -> None:
    expected = "29"
    actual = sut.day()

    assert expected == actual


def test_日時オブジェクトから時間を取得できる(sut: XDateTime) -> None:
    expected = "23"
    actual = sut.hour()

    assert expected == actual


def test_日時オブジェクトから分を取得できる(sut: XDateTime) -> None:
    expected = "10"
    actual = sut.minutes()

    assert expected == actual


def test_日時オブジェクトから秒を取得できる(sut: XDateTime) -> None:
    expected = "45"
    actual = sut.seconds()

    assert expected == actual


def test_今日の日時オブジェクトを生成できる() -> None:
    t_delta = datetime.timedelta(hours=9)
    # 日本標準時
    jst = datetime.timezone(t_delta, "JST")

    sut = XDateTime.now()

    expected = datetime.datetime.now(jst).strftime("%Y-%m-%d %H:%M:%S")
    actual = sut.format("%Y-%m-%d %H:%M:%S")

    assert expected == actual


def test_日時オブジェクトを日付オブジェクトに変換できる(sut: XDateTime) -> None:
    expected = XDate("2022-12-29")
    actual = sut.to_x_date()

    assert expected == actual


def test_指定月の月末日を取得できる(sut: XDateTime) -> None:
    expected = "2022/01/31"
    actual = sut.last_datetime_of_month(2022, 1).format("%Y/%m/%d")

    assert expected == actual


def test_日時を加算できる_日(sut: XDateTime) -> None:
    expected = "2022/12/31"
    actual = sut.add_days(2).format("%Y/%m/%d")

    assert expected == actual
