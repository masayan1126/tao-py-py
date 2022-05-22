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


print("debug")
