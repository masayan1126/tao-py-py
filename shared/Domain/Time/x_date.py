from dataclasses import dataclass
import datetime
from dateutil.relativedelta import relativedelta


@dataclass
class XDate:
    _date: datetime.date

    def __init__(self, date_str) -> None:

        try:
            # Y-m-d形式(例.2012-02-21)
            # 年月日が省略されていたり、桁数が合っていなかったりするとValueError。
            self._date = datetime.date.fromisoformat(date_str)
        except ValueError:
            raise ValueError

    def year(self) -> str:
        return self.format("%Y")

    def month(self) -> str:
        return self.format("%m")

    def day(self) -> str:
        return self.format("%d")

    @staticmethod
    def today():
        date_str = datetime.date.today().isoformat()
        return XDate(date_str)

    # 指定月の月末日を返します
    @staticmethod
    def last_day_of_month(year: int, month: int):
        last_day = (
            datetime.date(year, month, 1)
            + relativedelta(months=1)
            + datetime.timedelta(days=-1)
        )

        last_day_str = datetime.date.strftime(last_day, "%Y-%m-%d")
        return XDate(last_day_str)

    def format(self, format: str) -> str:
        # isoformat(Y-m-d)以外のフォーマットで取得したい場合に使用
        # format文字列は"%Y年%m月%d日"など
        # localにより、%Yなどの文字列は何を取得できるかが変わる
        # ここではエラーハンドリングしない。文字列が渡ってきさえすれば変換は可能。呼び出し側の記述が守れていればOKなため
        return self._date.strftime(format)
