from time import sleep
from shared.Domain.Excel.xcsv import XCsv
from shared.Domain.Notification.line_notification_service import LineNotificationService
from shared.Domain.Notification.notification import Notification
from shared.Domain.Scraping.html_analyzer import HtmlAnalyzer
from shared.Domain.Scraping.soup_factory import SoupFactory
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr
from shared.Domain.Url.x_url import XUrl
from shared.di_container import DiContainer
from shared.i_factory import IFactory
from shared.Domain.Log.x_logger import XLogger
from packages.my_rss.env import ENV
from packages.my_rss.config import CONFIG


class RssNotificationUsecase:
    def __init__(self, site_list: list):
        self.site_list = site_list

    def notify_to_line(self) -> None:
        try:
            updated = []

            for site_info in self.site_list:

                if site_info["need_auth_cookie"] == "yes":
                    cookie = ENV["AUTH_COOKIE"]

                html_analyzer = self.build_html_analyzer(
                    site_info=site_info, cookie=cookie
                )
                sleep(3)

                if site_info["prev_info"] != self.current(html_analyzer, site_info):
                    new = site_info
                    new["prev_info"] = self.current(html_analyzer, site_info)
                    updated.append(new)
                    LineNotificationService(self.build_notification(site_info)).send()
                else:
                    updated.append(site_info)

            XCsv().output(
                XFileSystemPath(XStr("packages/my_rss/site_list.csv")).to_absolute(),
                updated,
            )

        except Exception as e:
            XLogger.exception_to_slack(
                ENV["SLACK_WEBHOOK_URL_RSS"],
                e,
            )
            raise e

    def build_notification(self, site_info) -> Notification:
        LINE_NOTIFY_URL = ENV["LINE_NOTIFY_URL"]
        LINE_NOTIFY_TOKEN = CONFIG["LINE_NOTIFY_TOKEN"]
        site_url = site_info["url"]
        message = "サイトが更新されました。" "\n" f"{site_url}"

        return Notification(LINE_NOTIFY_URL, message, LINE_NOTIFY_TOKEN)

    def build_html_analyzer(self, site_info, cookie=None) -> HtmlAnalyzer:
        factory: IFactory = SoupFactory()
        soup = factory.create(XUrl(site_info["url"]), cookie)
        html_analyzer: HtmlAnalyzer = DiContainer().resolve(HtmlAnalyzer)
        html_analyzer.bind(soup)
        return html_analyzer

    def current(self, html_analyzer: HtmlAnalyzer, site_info):
        if site_info["target_html_attr"] == "id":
            current = html_analyzer.find_by_id(site_info["target_html_value"]).text
        else:
            current = html_analyzer.search_by_class(site_info["target_html_value"]).text

        return current
