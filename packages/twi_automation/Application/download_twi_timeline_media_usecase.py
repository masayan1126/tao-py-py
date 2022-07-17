from dataclasses import dataclass
from packages.twi_automation.Application.fetch_twi_timeline_usecase import (
    FetchTwiTimelineUsecase,
)
from packages.twi_automation.env import ENV
from shared.Domain.File.file_downloade_service import FileDownloadeService
from shared.Domain.File.x_file import XFile
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.Log.x_logger import XLogger
from shared.Domain.String.xstr import XStr
from shared.Domain.Text.text_file_service import TextFileService
from shared.Domain.Text.x_text import XText
from shared.Domain.Twi.tweet import Tweet
from shared.Domain.Url.x_url import XUrl


@dataclass
class DownloadTwiTimelineMediaUsecase:
    screen_name: XStr
    fetch_count: int
    since_tweet_id: int

    def download(
        self, download_path_to: XFileSystemPath = XFileSystemPath.home_dir()
    ) -> None:
        try:

            last_tweet_id = 0  # ループの一番最後のツイートIDをセットする

            for tweet in self.tweets():
                urls = []
                if tweet.is_contain_media:
                    for media in tweet.media_list():
                        extension = ""

                        if media["type"] == "video":
                            extension = ".mp4"
                        else:
                            extension = ".jpg"

                        urls.append(XUrl(encoded_href=media["url"]))
                else:
                    pass

                for x_url in urls:
                    x_file = XFile(x_url)

                    FileDownloadeService().download(
                        x_file=x_file,
                        download_path_to=download_path_to,
                        extension=extension,
                    )

            self.update_last_tweet_id(last_tweet_id)

        except Exception as e:
            XLogger.exception_to_slack(
                ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
                e,
            )
            raise e

    def tweets(self) -> list[Tweet]:
        return FetchTwiTimelineUsecase().fetch(
            screen_name=self.screen_name,
            fetch_count=self.fetch_count,
            since_tweet_id=self.since_tweet_id,
        )

    def update_last_tweet_id(self, last_tweet_id: int) -> None:
        filepath = XFileSystemPath(
            XStr("packages/twi_automation/files/fetch_timeline/since_tweet_id.txt")
        ).to_absolute()

        TextFileService(x_text=XText(filepath)).write(
            content=[str(last_tweet_id)],
            is_overwrite=True,
            encoding="UTF-8",
            needs_indention=False,
        )
