from packages.twi_automation.env import ENV
from shared.Domain.Excel.xcsv import XCsv
from shared.Domain.Wp.wp_operator import WpOperator
import urllib.request, urllib.error
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.xstr import XStr
from shared.Exception.wp_error import WpError
from shared.x_logger import XLogger

# 毎月1日10::00に実行して新規記事を取り込む

url = "https://maasaablog.com/"
endpoint = "/wp-json/wp/v2/posts"
wrong_url = "https://note.nkmk.me/"
api_url = url + endpoint


try:
    wp = WpOperator(api_url=wrong_url)
    posts = wp.fetch_posts()

    XCsv().output(
        XFileSystemPath(XStr("packages/twi_automation/posts.csv")).to_absolute(), posts
    )

except urllib.error.URLError as e:
    if e.code == 403:
        XLogger.exception_to_slack(
            ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
            "Failed to fetch the article. Because the url was not found",
        )
except WpError as e:
    XLogger.exception_to_slack(
        ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
        e._msg,
    )


print("debug")
