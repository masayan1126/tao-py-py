from time import sleep
from packages.my_rss.Application.rss_notification_service import RssNotificationService

from packages.my_rss.config import CONFIG
from packages.my_rss.env import ENV
from packages.twi_automation.env import ENV as ENV_TWI
from shared.Domain.Scraping.i_web_browser_operator import IWebBrowserOperator
from shared.Domain.Scraping.x_browser_factory import XBrowserFactory
from shared.Domain.Scraping.x_driver_factory import XDriverFactory
from shared.Domain.Text.text_file_operator import TextFileOperator
from shared.Domain.x_file_system_path import XFileSystemPath
from shared.Domain.xstr import XStr
from shared.Domain.Text.x_text import XText
from shared.Domain.xurl import XUrl
from shared.Enums.browser_type import BrowserType
from shared.di_container import DiContainer
from shared.x_logger import XLogger
from selenium.common.exceptions import SessionNotCreatedException


# 1.BeautifulSoupもしくは、Selenium等でサイト情報(例えば、新着情報箇所のhtml)を取得

try:
    xdriver = XDriverFactory().create(
        BrowserType.CHROME, is_headless=True, on_docker=False
    )
    site_url = ENV["SITE_URL"]
    xbrowser = XBrowserFactory().create(xdriver, XUrl(site_url))
    web_browser_operator: IWebBrowserOperator = DiContainer().resolve(
        IWebBrowserOperator
    )
    web_browser_operator.boot(xbrowser)

    web_browser_operator.find_by_id("AC").web_element().click()
    sleep(5)

    current = web_browser_operator.find_by_id("topic_text").web_element().text
except SessionNotCreatedException as e:
    XLogger.exception_to_slack(
        ENV_TWI["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
        e,
    )
finally:
    if "xdriver" in locals():
        xdriver.driver().quit()

print(current)


# 2.テキストから、前回のサイト情報を取得

filepath = XFileSystemPath(XStr("packages/my_rss/rss.txt")).to_absolute()
prev = TextFileOperator(x_text=XText(filepath)).read(encoding="UTF-8")

# 3.1.と2.を比較して、一致していなければ更新があったことになるので、その場合はテキストを更新して、LINE通知する
if prev != current:
    content = TextFileOperator(x_text=XText(filepath)).write(
        content=current, is_overwrite=True, encoding="UTF-8"
    )

    # 取得したトークンをconfig.pyから読み込み
    LINE_NOTIFY_TOKEN = CONFIG["LINE_NOTIFY_TOKEN"]
    LINE_NOTIFY_URL = ENV["LINE_NOTIFY_URL"]
    RssNotificationService(LINE_NOTIFY_TOKEN, LINE_NOTIFY_URL).send(
        "サイトが更新されました。" "\n" f"{site_url}"
    )


print("debug")
