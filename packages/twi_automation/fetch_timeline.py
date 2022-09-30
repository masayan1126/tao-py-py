from packages.twi_automation.Application.twi_timeline_media_get_usecase import (
    TwiTimelineMediaGetUsecase,
)
from packages.twi_automation.env import ENV
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath

from shared.Domain.String.xstr import XStr
from shared.Domain.Text.text_file_service import TextFileService
from shared.Domain.Text.x_text import XText
from shared.Domain.Log.x_logger import XLogger


def screen_name() -> XStr:
    return XStr(
        TextFileService(
            x_text=XText(
                XFileSystemPath(
                    XStr("packages/twi_automation/files/fetch_timeline/screen_name.txt")
                ).to_absolute()
            )
        ).read(encoding="UTF-8")
    )


def since_tweet_id() -> int:
    return int(
        TextFileService(
            x_text=XText(
                XFileSystemPath(
                    XStr(
                        "packages/twi_automation/files/fetch_timeline/since_tweet_id.txt"
                    )
                ).to_absolute()
            )
        ).read(encoding="UTF-8")
    )


try:

    download_path_to = XFileSystemPath.home_dir().join(
        "desktop", "collections", "images"
    )

    TwiTimelineMediaGetUsecase(
        screen_name=screen_name(),
        since_tweet_id=since_tweet_id(),
    ).download(download_path_to=download_path_to)

except Exception as e:

    XLogger.exception_to_slack(
        ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
        e,
    )
