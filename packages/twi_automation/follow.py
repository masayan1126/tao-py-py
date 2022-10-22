from shared.Core.Log.log_handler import LogHandler
from shared.Core.Log.log_type import LogType
from shared.Domain.TextFile.text_file_operator_factory import TextFileOperatorFactory
from shared.Domain.TextFile.text_file_operator_impl import TextFileOperatorImpl
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

error_log_filepath = XFileSystemPath(
    XStr("packages/twi_automation/error-log.txt")
).to_absolute()

text_file_operator = TextFileOperatorFactory().create(error_log_filepath)
api_code = text_file_operator.read(encoding="UTF-8")

# Rate limit もしくはspam認定ならそもそも1回分処理を中止して、エラーログ用のテキストを空にする
if api_code == "88" or api_code == "283":
    LogHandler(
        LogType.EXCEPTION,
        "Rate limit もしくはspam認定を受けているため、処理開始前にキャンセルしました",
        ENV["PACKAGE_NAME"],
    ).to_slack(ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"])

    text_file_operator.write(
        "", is_overwrite=True, encoding="UTF-8", needs_indention=True
    )

    raise Exception


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

    text_file_operator.write(e.api_codes[0], is_overwrite=True, encoding="UTF-8")
finally:
    if "success_count" in locals() and "users_tried_to_follow" in locals():
        LogHandler(
            LogType.NOTIFICATION,
            "フォロー・いいね数:" f"{success_count}/25" "\n" f"{users_tried_to_follow}/25",
            ENV["PACKAGE_NAME"],
        ).to_slack(ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"])
