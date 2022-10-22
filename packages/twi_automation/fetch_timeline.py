from packages.twi_automation.Application.twi_timeline_media_get_usecase import (
    TwiTimelineMediaGetUsecase,
)
from packages.twi_automation.env import ENV
from shared.Core.Log.log_handler import LogHandler
from shared.Core.Log.log_type import LogType
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr
from shared.Domain.TextFile.text_file_operator_factory import TextFileOperatorFactory
from shared.Domain.TextFile.text_file_operator_impl import TextFileOperatorImpl
from shared.Domain.Twi.twitter_operator_factory_option import (
    TwitterOperatorFactoryOption,
)


def screen_name() -> XStr:
    text_file_operator = TextFileOperatorFactory().create(
        XFileSystemPath(
            XStr("packages/twi_automation/files/fetch_timeline/screen_name.txt")
        ).to_absolute()
    )

    return XStr(text_file_operator.read(encoding="UTF-8"))


def since_tweet_id() -> int:
    text_file_operator = TextFileOperatorFactory().create(
        XFileSystemPath(
            XStr("packages/twi_automation/files/fetch_timeline/since_tweet_id.txt")
        ).to_absolute()
    )

    return int(text_file_operator.read(encoding="UTF-8"))


try:

    download_path_to = XFileSystemPath.home_dir().join(
        "desktop", "collections", "images"
    )

    factory_option = TwitterOperatorFactoryOption(
        ENV["MY_SCREEN_NAME"], ENV["BLACK_LIST"]
    )

    TwiTimelineMediaGetUsecase(
        screen_name=screen_name(),
        fetch_count=5,
        since_tweet_id=since_tweet_id(),
    ).download(download_path_to=download_path_to)

except Exception as e:

    LogHandler(
        LogType.EXCEPTION,
        e,
        ENV["PACKAGE_NAME"],
    ).to_slack(ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"])
