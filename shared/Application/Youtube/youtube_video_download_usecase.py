from shared.Domain.Url.x_url import XUrl
from shared.Youtube.yt_downloader import YtDownloader


class YoutubeVideoDownloadUsecase:
    def download(self, video_id: str, options: dict):

        yt_downloader = YtDownloader(options)
        yt_downloader.download(XUrl(f"https://www.youtube.com/watch?v={video_id}"))
