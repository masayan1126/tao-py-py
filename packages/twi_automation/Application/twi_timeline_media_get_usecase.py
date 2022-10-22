from dataclasses import dataclass
from packages.twi_automation.env import ENV
from shared.Domain.File.file_download_service import FileDownloadService
from shared.Domain.File.x_file import XFile
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr
from shared.Domain.TextFile.text_file_operator_factory import TextFileOperatorFactory
from shared.Domain.TextFile.text_file_operator_impl import TextFileOperatorImpl
from shared.Domain.Twi.tweet import Tweet
from shared.Domain.Twi.twitter_operator_factory import TwitterOperatorFactory
from shared.Domain.Twi.twitter_operator_factory_option import (
    TwitterOperatorFactoryOption,
)
from shared.Domain.Url.x_url import XUrl


@dataclass
class TwiTimelineMediaGetUsecase:
    screen_name: XStr
    fetch_count: int
    since_tweet_id: int

    def download(
        self, download_path_to: XFileSystemPath = XFileSystemPath.home_dir()
    ) -> None:

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

            for x_url in urls:
                x_file = XFile(x_url)

                FileDownloadService().download(
                    x_file=x_file,
                    download_path_to=download_path_to,
                    extension=extension,
                )

        self.update_last_tweet_id(last_tweet_id)

    def tweets(self) -> list[Tweet]:

        factory_option = TwitterOperatorFactoryOption(
            ENV["MY_SCREEN_NAME"], ENV["BLACK_LIST"]
        )

        return (
            TwitterOperatorFactory()
            .create(factory_option)
            .fetch_timeline(
                screen_name=self.screen_name,
                count=self.fetch_count,
                since_id=self.since_tweet_id,
            )
        )

    def update_last_tweet_id(self, last_tweet_id: int) -> None:
        filepath = XFileSystemPath(
            XStr("packages/twi_automation/files/fetch_timeline/since_tweet_id.txt")
        ).to_absolute()

        text_file_operator = TextFileOperatorFactory().create(filepath)

        text_file_operator.write(
            content=[str(last_tweet_id)],
            is_overwrite=True,
            encoding="UTF-8",
            needs_indention=False,
        )
