from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
import youtube_dl
from shared.Domain.Log.x_logger import XLogger
from shared.Domain.Url.x_url import XUrl

from shared.Youtube.i_yt_downloader import IYtDownloader


class YtDownloader(IYtDownloader):
    downloader: youtube_dl.YoutubeDL

    def __init__(self, options: dict = {}):

        self.downloader = youtube_dl.YoutubeDL(options)

    def download(self, download_path_from: XUrl) -> None:
        try:

            with self.downloader as ydl:
                ydl.download([download_path_from.href()])
        except Exception as e:
            raise e
