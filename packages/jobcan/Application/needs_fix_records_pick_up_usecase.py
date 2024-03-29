from packages.jobcan.env import ENV
from shared.Core.Log.log_handler import LogHandler
from shared.Core.Log.log_type import LogType
from shared.Domain.Scraping.web_browser_operator import WebBrowserOperator
from shared.Domain.String.xstr import XStr


class NeedsFixRecordsPickUpUsecase:
    def handle(self, web_browser_operator: WebBrowserOperator):
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
            LogHandler(
                LogType.NOTIFICATION,
                "修正が必要なレコードはありませんでした。",
                ENV["PACKAGE_NAME"],
            ).to_slack(ENV["SLACK_WEBHOOK_URL_JOBCAN"])
        else:
            LogHandler(
                LogType.NOTIFICATION,
                f"修正が必要なレコードは{target_rows}です",
                ENV["PACKAGE_NAME"],
            ).to_slack(ENV["SLACK_WEBHOOK_URL_JOBCAN"])
