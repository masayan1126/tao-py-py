from packages.jobcan.Application.login_jobcan_usecase import LoginJobcanUsecase
from packages.jobcan.Application.pick_up_needs_fix_records_usecase import (
    PickUpNeedsFixRecordsUsecase,
)

from packages.jobcan.Application.register_manhour_usecase import RegisterManhourUseCase
from shared.Domain.IpAddress.ip_address_service import IpAddressService


from shared.Domain.Log.x_logger import XLogger
from packages.today_task_notification.env import ENV as ENV_TODAY_IP
from packages.jobcan.env import ENV as ENV_JOBCAN
from shared.Domain.Scraping.html_analyzer import HtmlAnalyzer
from time import sleep
from shared.Domain.Scraping.soup_factory import SoupFactory
from shared.Domain.Url.x_url import XUrl
from shared.di_container import DiContainer

from shared.factory import Factory

# ログイン
# jobcanを起動し、昨日分の工数レコードを開き、テンプレートから工数を入力
# 修正が必要な工数レコードをピックアップ

try:
    # サイトは確認くん固定
    site_url = "https://www.ugtop.com/spill.shtml"
    factory: Factory = SoupFactory()
    soup = factory.create(XUrl(site_url))
    html_analyzer: HtmlAnalyzer = DiContainer().resolve(HtmlAnalyzer)
    html_analyzer.bind(soup)
    sleep(1)

    ip_address = IpAddressService(html_analyzer).get_today_ip()

    XLogger.notification_to_slack(
        ENV_TODAY_IP["SLACK_WEBHOOK_URL_MY_TASK"],
        f"Notify today task to line is successed !!\n And Today Your IP is {ip_address.value()}",
    )

    web_browser_operator = LoginJobcanUsecase().handle()
    RegisterManhourUseCase().handle(web_browser_operator)
    PickUpNeedsFixRecordsUsecase().handle(web_browser_operator)

except Exception as e:
    XLogger.exception_to_slack(
        ENV_JOBCAN["SLACK_WEBHOOK_URL_JOBCAN"],
        e,
    )
