from time import sleep

from shared.Domain.Scraping.i_web_browser_operator import IWebBrowserOperator
from shared.Domain.xstr import XStr

from shared.x_logger import XLogger


class PickUpNeedsFixRecordsService:
    def handle(self, web_browser_operator: IWebBrowserOperator):
        trs = web_browser_operator.search_by_css_selector(css_selector="tbody tr")
        # すでに工数が入力されているが、総労働時間と工数合計が等しくない(つまり修正が必要なレコード)
        target_rows = []

        for tr in trs.all():

            # ['03/24木', '08:00', '08:00', '編集']のようなリスト
            row_text_list = XStr(tr.web_element().text).to_list(" ")

            # 0:'04/30土'
            # 1:'00:00'
            # 2:'入力がありません'
            # 3:'編集'
            total_working_time = row_text_list[1]
            total_man_hours = row_text_list[2]

            if total_working_time != "00:00" and total_working_time != total_man_hours:
                target_rows.append(row_text_list)

        if len(target_rows) == 0:
            XLogger.notificationToSlack("修正が必要なレコードはありませんでした。")
        else:
            XLogger.exceptionToSlack(f"修正が必要なレコードは{target_rows}です")
