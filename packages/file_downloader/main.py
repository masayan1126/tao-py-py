from packages.twi_automation.env import ENV
from shared.Domain.File.file_downloade_service import FileDownloadeService
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.File.x_file import XFile
from shared.Domain.Url.x_url import XUrl
from shared.Domain.Log.x_logger import XLogger

x_url = XUrl(href="https://www.home-movie.biz/mov/hts-samp001.mp4")
x_file = XFile(x_url)

try:
    download_path_to = XFileSystemPath.home_dir().join("desktop", "private")

    FileDownloadeService().download(
        x_file=x_file, download_path_to=download_path_to, extension=".mp4"
    )
except ValueError as e:
    XLogger.exception_to_slack(
        ENV["SLACK_WEBHOOK_URL_JOBCAN"],
        e,
    )


print("debug")
