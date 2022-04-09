import datetime

from shared.Domain.Time.x_date import XDate
from dateutil.relativedelta import relativedelta


class XDateTime:
    def __init__(self, date_time_str: str) -> None:

        try:
            # Y-m-d形式(例.2012-02-21)
            # 年月日時間分秒のどれかが省略されていたり、桁数が合っていなかったりするとValueError。
            self._datetime = datetime.datetime.fromisoformat(date_time_str)

        except ValueError:
            raise ValueError

    def datetime(self):
        return self._datetime

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
        return self.datetime().strftime(format)

    def to_x_date(self):
        dt = self.datetime()
        date = datetime.date(dt.year, dt.month, dt.day)
        date_str = date.isoformat()
        return XDate(date_str)
