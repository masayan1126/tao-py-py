import datetime
import pytest
from shared.Domain.Time.x_date import XDate


def test_日付オブジェクトを生成できる() -> None:

    # formatテストはこのテスト以降にあるので、ここではisoformat()を使用する
    actual = XDate("2022-12-29").date().isoformat()
    expected = "2022-12-29"

    assert expected == actual


def test_日付オブジェクトを生成できる_ISO8601でない場合は例外() -> None:
    with pytest.raises(ValueError):
        x_date = XDate("2022/12/29").date()


def test_日付オブジェクトをフォーマットできる() -> None:

    actual = XDate("2022-12-29").format("%Y/%m/%d")
    expected = "2022/12/29"

    assert expected == actual


def test_日付オブジェクトから年を取得できる() -> None:

    actual = XDate("2022-12-29").year()
    expected = "2022"

    assert expected == actual


def test_日付オブジェクトから月を取得できる() -> None:

    actual = XDate("2022-12-29").month()
    expected = "12"

    assert expected == actual


def test_日付オブジェクトから日を取得できる() -> None:

    actual = XDate("2022-12-29").day()
    expected = "29"

    assert expected == actual


def test_今日の日付オブジェクトを生成できる() -> None:

    actual = XDate.today().format("%Y/%m/%d")
    expected = datetime.date.today().strftime("%Y/%m/%d")

    assert expected == actual


def test_指定月の月末日を取得できる() -> None:

    actual = XDate.last_day_of_month(2022, 4).format("%Y/%m/%d")
    expected = "2022/04/30"

    assert expected == actual
