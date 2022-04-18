from packages.twi_automation.env import ENV
from shared.Application.download_file_service import DownloadFileService
from shared.Domain.x_file_system_path import XFileSystemPath
from shared.Domain.xfile import XFile
from shared.Domain.xurl import XUrl
from shared.x_logger import XLogger

x_url = XUrl(href="https://www.home-movie.biz/mov/hts-samp001.mp4")
x_file = XFile(x_url)

try:
    download_path_to = XFileSystemPath.home_dir().join("desktop", "private")

    DownloadFileService().download(
        x_file=x_file, download_path_to=download_path_to, extension=".mp4"
    )
except ValueError as e:
    XLogger.exception_to_slack(
        ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
        "相対パスに変換しようとしたパスに、起点となるcwdが含まれていないため、変換に失敗しました",
    )


print("debug")
