from time import sleep
from shared.Domain.Notification.line_notification_service import LineNotificationService
from shared.Domain.Notification.notification import Notification
from shared.Domain.Scraping.i_html_analyzer import IHtmlAnalyzer
from shared.Domain.Scraping.soup_factory import SoupFactory
from shared.Domain.Text.text_file_service import TextFileService
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr
from shared.Domain.Text.x_text import XText
from shared.Domain.Url.x_url import XUrl
from shared.di_container import DiContainer
from shared.i_factory import IFactory
from shared.Domain.Log.x_logger import XLogger
from selenium.common.exceptions import SessionNotCreatedException

from packages.my_rss.env import ENV


class RssNotificationUsecase:
    def __init__(self, notification: Notification):
        self.notification = notification

    def notify_to_line(self) -> int:

        # 1.BeautifulSoupもしくは、Selenium等でサイト情報(例えば、新着情報箇所のhtml)を取得

        try:
            site_url = ENV["SITE_URL"]
            factory: IFactory = SoupFactory()
            cookie = ENV["AUTH_COOKIE"]
            soup = factory.create(XUrl(site_url), cookie)
            i_html_analyzer: IHtmlAnalyzer = DiContainer().resolve(IHtmlAnalyzer)
            i_html_analyzer.bind(soup)
            sleep(3)
            current = i_html_analyzer.find_by_id("topic_text").text
        except SessionNotCreatedException as e:
            XLogger.exception_to_slack(
                ENV["SLACK_WEBHOOK_URL_RSS"],
                e,
            )
            raise e

        # 2.テキストから、前回のサイト情報を取得

        filepath = XFileSystemPath(XStr("packages/my_rss/rss.txt")).to_absolute()
        prev = TextFileService(x_text=XText(filepath)).read(encoding="UTF-8")

        # 3.1.と2.を比較して、一致していなければ更新があったことになるので、その場合はテキストを更新して、LINE通知する
        if prev != current:
            content = TextFileService(x_text=XText(filepath)).write(
                content=[current],
                is_overwrite=True,
                encoding="UTF-8",
                needs_indention=False,
            )

            return LineNotificationService(self.notification).send()
