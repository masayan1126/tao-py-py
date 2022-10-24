from packages.twi_automation.env import ENV
from shared.Core.Log.log_handler import LogHandler
from shared.Core.Log.log_type import LogType
from shared.Domain.DataFile.Csv.csv_file_operator_impl import CsvFileOperatorImpl
from shared.Domain.Url.x_url import XUrl
from shared.Domain.Wp.wp_operator_factory import WpOperatorFactory
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr

url = "https://maasaablog.com/"
endpoint = "/wp-json/wp/v2/posts"
api_url = url + endpoint


try:
    wp_operator = WpOperatorFactory().create(XUrl(api_url))
    posts = wp_operator.fetch_posts(page=1)

    CsvFileOperatorImpl().output(
        XFileSystemPath(XStr("packages/twi_automation/posts.csv")).to_absolute(), posts
    )
except Exception as e:
    LogHandler(
        LogType.EXCEPTION,
        e,
        ENV["PACKAGE_NAME"],
    ).to_slack(ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"])
