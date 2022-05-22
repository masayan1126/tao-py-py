from packages.twi_automation.Domain.twi_error_handle_judgement_service import (
    TwiErrorHandleJudgementService,
)

from packages.twi_automation.env import ENV
from shared.Domain.Text.text_file_service import TextFileService
from shared.Domain.Text.x_text import XText
from shared.Domain.Twi.twitter_operator import TwitterOperator
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr
from shared.Domain.Log.x_logger import XLogger
import tweepy

error_log_filepath = XFileSystemPath(
    XStr("packages/twi_automation/error-log.txt")
).to_absolute()
api_code = TextFileService(x_text=XText(error_log_filepath)).read(encoding="UTF-8")

# Rate limit もしくはspam認定ならそもそも1回分処理を中止して、エラーログ用のテキストを空にする
if api_code == "88" or api_code == "283":
    XLogger.exception_to_slack(
        ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
        "Rate limit もしくはspam認定を受けているため、処理開始前にキャンセルしました",
    )

    TextFileService(x_text=XText(error_log_filepath)).write(
        "", is_overwrite=True, encoding="UTF-8", needs_indention=True
    )

    raise Exception


try:
    twitter_operator = TwitterOperator()
    success_count, users_tried_to_follow = twitter_operator.follow(
        hashtag=XStr(ENV["HASH_TAG"])
    )

except (tweepy.errors.TooManyRequests, tweepy.errors.TweepyException) as e:
    judgement = TwiErrorHandleJudgementService(e)
    log_msg = judgement.judge()

    XLogger.exception_to_slack(
        ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
        log_msg,
    )

    TextFileService(x_text=XText(error_log_filepath)).write(
        e.api_codes[0], is_overwrite=True, encoding="UTF-8"
    )
finally:
    if "success_count" in locals() and "users_tried_to_follow" in locals():
        XLogger.notification_to_slack(
            ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
            "フォロー・いいね数:" f"{success_count}/25" "\n" f"{users_tried_to_follow}/25",
        )

print("debug")
