import datetime
import pytest
from shared.Domain.Time.x_date import XDate
from shared.Domain.Time.x_date_time import XDateTime


def test_日時オブジェクトを生成できる() -> None:

    # formatテストはこのテスト以降にあるので、ここではisoformat()を使用する
    acutual = XDateTime("2022-12-29").datetime().isoformat()
    expected = "2022-12-29T00:00:00"

    assert acutual == expected


def test_日時オブジェクトを生成できる_ISO8601でない場合は例外() -> None:
    with pytest.raises(ValueError):
        x_date_time = XDateTime("2022/12/29").datetime()


def test_日時オブジェクトをフォーマットできる() -> None:

    acutual = XDateTime("2022-12-29").format("%Y/%m/%d %H:%M:%S")
    expected = "2022/12/29 00:00:00"

    assert acutual == expected


def test_日時オブジェクトから年を取得できる() -> None:

    acutual = XDateTime("2022-12-29").year()
    expected = "2022"

    assert acutual == expected


def test_日時オブジェクトから月を取得できる() -> None:

    acutual = XDateTime("2022-12-29").month()
    expected = "12"

    assert acutual == expected


def test_日時オブジェクトから日を取得できる() -> None:

    acutual = XDateTime("2022-12-29").day()
    expected = "29"

    assert acutual == expected


def test_日時オブジェクトから時間を取得できる() -> None:

    acutual = XDateTime("2022-12-29 23:10:45").hour()
    expected = "23"

    assert acutual == expected


def test_日時オブジェクトから分を取得できる() -> None:

    acutual = XDateTime("2022-12-29 23:10:45").minutes()
    expected = "10"

    assert acutual == expected


def test_日時オブジェクトから秒を取得できる() -> None:

    acutual = XDateTime("2022-12-29 23:10:45").seconds()
    expected = "45"

    assert acutual == expected


def test_今日の日時オブジェクトを生成できる() -> None:

    t_delta = datetime.timedelta(hours=9)
    # 日本標準時
    jst = datetime.timezone(t_delta, "JST")

    acutual = XDateTime.now().format("%Y-%m-%d %H:%M:%S")
    expected = datetime.datetime.now(jst).strftime("%Y-%m-%d %H:%M:%S")

    assert acutual == expected


def test_日時オブジェクトを日付オブジェクトに変換できる() -> None:

    acutual = XDateTime("2022-12-29 23:10:45").to_x_date().format("%Y/%m/%d")
    expected = XDate("2022-12-29").format("%Y/%m/%d")

    assert acutual == expected


def test_指定月の月末日を取得できる() -> None:

    acutual = XDateTime.last_datetime_of_month(2022, 1).format("%Y/%m/%d")
    expected = "2022/01/31"

    assert acutual == expected
