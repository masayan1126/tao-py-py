from shared.Core.Log.log_handler import LogHandler
from shared.Core.Log.log_type import LogType
from shared.Domain.DataFile.TextFile.text_file_operator_factory import (
    TextFileOperatorFactory,
)
from shared.Domain.DataFile.TextFile.text_file_operator_impl import TextFileOperatorImpl
from shared.Domain.Twi.twi_error_judgement import (
    TwiErrorJudgement,
)
from packages.twi_automation.env import ENV
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr
from shared.Domain.Twi.twitter_operator_factory import TwitterOperatorFactory
from shared.Domain.Twi.twitter_operator_factory_option import (
    TwitterOperatorFactoryOption,
)
import tweepy

try:
    factory_option = TwitterOperatorFactoryOption(
        ENV["MY_SCREEN_NAME"], ENV["BLACK_LIST"]
    )

    operator = TwitterOperatorFactory().create(factory_option)
    success_count, users_tried_to_follow = operator.follow(
        hashtag=XStr(ENV["HASH_TAG"])
    )

except (tweepy.errors.TooManyRequests, tweepy.errors.TweepyException) as e:
    judgement = TwiErrorJudgement(e)
    log_msg = judgement.judge()

    LogHandler(
        LogType.EXCEPTION,
        log_msg,
        ENV["PACKAGE_NAME"],
    ).to_slack(ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"])

finally:
    if "success_count" in locals() and "users_tried_to_follow" in locals():
        LogHandler(
            LogType.NOTIFICATION,
            "フォロー・いいね数:" f"{success_count}/25" "\n" f"{users_tried_to_follow}/25",
            ENV["PACKAGE_NAME"],
        ).to_slack(ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"])
