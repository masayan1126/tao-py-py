from packages.jobcan.Application.login_jobcan_usecase import LoginJobcanUsecase
from packages.jobcan.Application.pick_up_needs_fix_records_usecase import (
    PickUpNeedsFixRecordsUsecase,
)

from packages.jobcan.Application.register_manhour_usecase import RegisterManhourUseCase
from packages.notification_today_ip.Application.fetch_today_ip_address_usecase import (
    FetchTodayIpAddressUsecase,
)


from shared.Domain.Log.x_logger import XLogger
from packages.today_task_notification.env import ENV
from packages.today_task_notification.env import ENV
from shared.Domain.Log.x_logger import XLogger
from shared.Domain.Scraping.i_html_analyzer import IHtmlAnalyzer
from time import sleep
from shared.Domain.Scraping.i_html_analyzer import IHtmlAnalyzer
from shared.Domain.Scraping.soup_factory import SoupFactory
from shared.Domain.Url.x_url import XUrl
from shared.di_container import DiContainer
from selenium.common.exceptions import SessionNotCreatedException

from shared.i_factory import IFactory

# ログイン
# jobcanを起動し、昨日分の工数レコードを開き、テンプレートから工数を入力
# 修正が必要な工数レコードをピックアップ

try:
    # サイトは確認くん固定
    site_url = "https://www.ugtop.com/spill.shtml"
    factory: IFactory = SoupFactory()
    soup = factory.create(XUrl(site_url))
    i_html_analyzer: IHtmlAnalyzer = DiContainer().resolve(IHtmlAnalyzer)
    i_html_analyzer.bind(soup)
    sleep(1)

    # IPを取得する
    ip_address = FetchTodayIpAddressUsecase(i_html_analyzer).fetch()

    XLogger.notification_to_slack(
        ENV["SLACK_WEBHOOK_URL_MY_TASK"],
        f"Notify today task to line is successed !!\n And Today Your IP is {ip_address.value()}",
    )

except SessionNotCreatedException as e:
    XLogger.exception_to_slack(
        ENV["SLACK_WEBHOOK_URL_MY_TASK"],
        e,
    )
    raise e

web_browser_operator = LoginJobcanUsecase().handle()
RegisterManhourUseCase().handle(web_browser_operator)
PickUpNeedsFixRecordsUsecase().handle(web_browser_operator)

print("debug")
