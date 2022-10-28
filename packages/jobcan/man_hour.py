from packages.jobcan.Application.jobcan_login_usecase import JobcanLoginUsecase
from packages.jobcan.Application.needs_fix_records_pick_up_usecase import (
    NeedsFixRecordsPickUpUsecase,
)

from packages.jobcan.Application.manhour_register_usecase import ManhourRegisterUseCase
from packages.jobcan.env import ENV
from shared.Core.Log.log_type import LogType
from shared.Domain.IpAddress.ip_address_service import IpAddressService
from shared.Core.Log.log_handler import LogHandler
from packages.today_task_notification.env import ENV as ENV_TODAY_IP
from time import sleep
from shared.Domain.Scraping.browser_type import BrowserType
from shared.Domain.Scraping.html_analyzer_factory import (
    HtmlAnalyzerFactory,
)
from shared.Domain.Scraping.web_browser_operator_factory import (
    WebBrowserOperatorFactory,
)
from shared.Domain.Url.x_url import XUrl

# ログイン
# jobcanを起動し、昨日分の工数レコードを開き、テンプレートから工数を入力
# 修正が必要な工数レコードをピックアップ

# サイトは確認くん固定
site_url = "https://www.ugtop.com/spill.shtml"
html_analyzer = HtmlAnalyzerFactory().create(XUrl(site_url))
sleep(1)

ip_address = IpAddressService(html_analyzer).get_today_ip()

LogHandler(
    LogType.NOTIFICATION,
    f"Notify today task to line is successed !!\n And Today Your IP is {ip_address.value()}",
    ENV["PACKAGE_NAME"],
).to_slack(ENV_TODAY_IP["SLACK_WEBHOOK_URL_MY_TASK"])

chorme_browser_operator = WebBrowserOperatorFactory().create(
    x_url=XUrl("https://id.jobcan.jp/"),
    browser_type=BrowserType.CHROME,
)

JobcanLoginUsecase(chorme_browser_operator).login()
ManhourRegisterUseCase().handle(chorme_browser_operator)
NeedsFixRecordsPickUpUsecase().handle(chorme_browser_operator)
