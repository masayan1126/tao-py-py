from dataclasses import dataclass
import datetime
from shared.Domain.Time.x_date import XDate
from dateutil.relativedelta import relativedelta


@dataclass
class XDateTime:
    _datetime: datetime.datetime

    def __init__(self, date_time_str: str) -> None:

        try:
            # Y-m-d形式(例.2012-02-21)
            # 年月日時間分秒のどれかが省略されていたり、桁数が合っていなかったりするとValueError。
            self._datetime = datetime.datetime.fromisoformat(date_time_str)

        except ValueError:
            raise ValueError

    def year(self) -> str:
        return self.format("%Y")

    def month(self) -> str:
        return self.format("%m")

    def day(self) -> str:
        return self.format("%d")

    def hour(self) -> str:
        return self.format("%H")

    def minutes(self) -> str:
        return self.format("%M")

    def seconds(self) -> str:
        return self.format("%S")

    @staticmethod
    def now():
        # timezoneを指定するとdatetimeの生成が早くなる
        t_delta = datetime.timedelta(hours=9)
        # 日本標準時
        jst = datetime.timezone(t_delta, "JST")
        now_str = datetime.datetime.now(jst).isoformat()

        return XDateTime(now_str)

    @staticmethod
    def utc_now():
        # 世界協定時刻（UTC）
        utc_str = datetime.datetime.now(datetime.timezone.utc).isoformat()
        return XDateTime(utc_str)

    # 指定月の月末日を返します
    @staticmethod
    def last_datetime_of_month(year: int, month: int):
        last_datetime = (
            datetime.datetime(year, month, 1)
            + relativedelta(months=1)
            + datetime.timedelta(days=-1)
        )

        last_datetime_str = datetime.date.strftime(last_datetime, "%Y-%m-%d")
        return XDateTime(last_datetime_str)

    def format(self, format: str):
        # isoformat(Y-m-d)以外のフォーマットで取得したい場合に使用
        # format文字列は"%Y年%m月%d日%H時%M分%S秒"など
        # localにより、%Yなどの文字列は何を取得できるかが変わる
        # ここではエラーハンドリングしない。文字列が渡ってきさえすれば変換は可能。呼び出し側の記述が守れていればOKなため
        return self._datetime.strftime(format)

    def to_x_date(self):
        dt = self._datetime
        date = datetime.date(dt.year, dt.month, dt.day)
        date_str = date.isoformat()
        return XDate(date_str)

    def add_days(self, days=1):
        self._datetime = self._datetime + datetime.timedelta(days=days)
        return self

    def add_hours(self, hours=1):
        self._datetime = self._datetime + datetime.timedelta(hours=hours)
        return self

    def add_minutes(self, minutes=1):
        self._datetime = self._datetime + datetime.timedelta(minutes=minutes)
        return self

    def add_seconds(self, seconds=1):
        self._datetime = self._datetime + datetime.timedelta(seconds=seconds)

        return self

    def sub_days(self, days=1):
        self._datetime = self._datetime - datetime.timedelta(days=days)
        return self

    def sub_hours(self, hours=1):
        self._datetime = self._datetime - datetime.timedelta(hours=hours)
        return self

    def sub_minutes(self, minutes=1):
        self._datetime = self._datetime - datetime.timedelta(minutes=minutes)
        return self

    def sub_seconds(self, seconds=1):
        self._datetime = self._datetime - datetime.timedelta(seconds=seconds)
        return self

    def text_of(self, format: str = "%Y-%m-%dT%H:%M:%S"):
        return self.format(format)
