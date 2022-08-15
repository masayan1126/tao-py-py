import datetime
import pytest
from shared.Domain.Time.x_date import XDate
from shared.Domain.Time.x_date_time import XDateTime


def test_日時オブジェクトを生成できる() -> None:

    # formatテストはこのテスト以降にあるので、ここではisoformat()を使用する
    actual = XDateTime("2022-12-29").datetime().isoformat()
    expected = "2022-12-29T00:00:00"

    assert expected == actual


def test_日時オブジェクトを生成できる_ISO8601でない場合は例外() -> None:
    with pytest.raises(ValueError):
        XDateTime("2022/12/29").datetime()


def test_日時オブジェクトをフォーマットできる() -> None:

    actual = XDateTime("2022-12-29").format("%Y/%m/%d %H:%M:%S")
    expected = "2022/12/29 00:00:00"

    assert expected == actual


def test_日時オブジェクトから年を取得できる() -> None:

    actual = XDateTime("2022-12-29").year()
    expected = "2022"

    assert expected == actual


def test_日時オブジェクトから月を取得できる() -> None:

    actual = XDateTime("2022-12-29").month()
    expected = "12"

    assert expected == actual


def test_日時オブジェクトから日を取得できる() -> None:

    actual = XDateTime("2022-12-29").day()
    expected = "29"

    assert expected == actual


def test_日時オブジェクトから時間を取得できる() -> None:

    actual = XDateTime("2022-12-29 23:10:45").hour()
    expected = "23"

    assert expected == actual


def test_日時オブジェクトから分を取得できる() -> None:

    actual = XDateTime("2022-12-29 23:10:45").minutes()
    expected = "10"

    assert expected == actual


def test_日時オブジェクトから秒を取得できる() -> None:

    actual = XDateTime("2022-12-29 23:10:45").seconds()
    expected = "45"

    assert expected == actual


def test_今日の日時オブジェクトを生成できる() -> None:

    t_delta = datetime.timedelta(hours=9)
    # 日本標準時
    jst = datetime.timezone(t_delta, "JST")

    actual = XDateTime.now().format("%Y-%m-%d %H:%M:%S")
    expected = datetime.datetime.now(jst).strftime("%Y-%m-%d %H:%M:%S")

    assert expected == actual


def test_日時オブジェクトを日付オブジェクトに変換できる() -> None:

    actual = XDateTime("2022-12-29 23:10:45").to_x_date().format("%Y/%m/%d")
    expected = XDate("2022-12-29").format("%Y/%m/%d")

    assert expected == actual


def test_指定月の月末日を取得できる() -> None:

    actual = XDateTime.last_datetime_of_month(2022, 1).format("%Y/%m/%d")
    expected = "2022/01/31"

    assert expected == actual


def test_日時を加算できる_日() -> None:

    x_date_time = XDateTime("2022-12-21 23:10:45")
    actual = x_date_time.add_days(2).format("%Y/%m/%d")
    expected = "2022/12/23"

    assert expected == actual
