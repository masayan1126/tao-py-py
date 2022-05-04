from packages.my_rss.Application.rss_notification_usecase import RssNotificationUsecase
from shared.Domain.Notification.notification import Notification
from packages.my_rss.env import ENV
from packages.my_rss.config import CONFIG

LINE_NOTIFY_URL = ENV["LINE_NOTIFY_URL"]
site_url = ENV["SITE_URL"]
message = "サイトが更新されました。" "\n" f"{site_url}"
LINE_NOTIFY_TOKEN = CONFIG["LINE_NOTIFY_TOKEN"]

notification = Notification(LINE_NOTIFY_URL, message, LINE_NOTIFY_TOKEN)

RssNotificationUsecase(
    notification=Notification(LINE_NOTIFY_URL, message, LINE_NOTIFY_TOKEN)
).notify_to_line()

print("debug")
