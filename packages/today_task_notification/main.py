from packages.notification_today_ip.Application.fetch_today_ip_address_usecase import (
    FetchTodayIpAddressUsecase,
)

from packages.today_task_notification.Application.today_task_notification_usecase import (
    TodayTaskNotificationUsecase,
)

from shared.Domain.Calendar.g_calendar_service import GCalendarService
from shared.Domain.Log.x_logger import XLogger
from shared.Domain.Notification.notification import Notification
from packages.today_task_notification.env import ENV
from packages.today_task_notification.config import CONFIG
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

LINE_NOTIFY_URL = ENV["LINE_NOTIFY_URL"]
LINE_NOTIFY_TOKEN = CONFIG["LINE_NOTIFY_TOKEN"]

notification = Notification(
    destination_url=LINE_NOTIFY_URL, message="", token=LINE_NOTIFY_TOKEN
)

TodayTaskNotificationUsecase(
    notification=notification,
    g_calendar_service=GCalendarService(),
).notify_to_line()

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


print("debug")
