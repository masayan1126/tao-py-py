import sys
from packages.twi_automation.Domain.twi_error_handle_judgement import (
    TwiErrorHandleJudgement,
)
from packages.twi_automation.env import ENV
from shared.Domain.Text.text_file_operator import TextFileOperator
from shared.Domain.Text.x_text import XText
from shared.Domain.Twi.twitter_operator import TwitterOperator
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.xstr import XStr
from shared.x_logger import XLogger
import tweepy

filepath = XFileSystemPath(XStr("packages/twi_automation/error-log.txt")).to_absolute()
api_code = TextFileOperator(x_text=XText(filepath)).read(encoding="UTF-8")

# Rate limit もしくはspam認定ならそもそも1回分処理を中止する
if api_code == 88 or api_code == 283:
    XLogger.exception_to_slack(
        ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
        "Rate limit もしくはspam認定を受けているため、処理開始前にキャンセルしました",
    )

    TextFileOperator(x_text=XText(filepath)).write(
        "", is_overwrite=True, encoding="UTF-8"
    )

    sys.exit()


twitter_operator = TwitterOperator()

try:
    success_count = twitter_operator.follow(hashtag=XStr(ENV["HASH_TAG"]))[0]
    users_tried_to_follow = twitter_operator.follow(hashtag=XStr(ENV["HASH_TAG"]))[1]

    XLogger.notification_to_slack(
        ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
        "フォロー・いいね数:" f"{success_count}/25" "\n" f"{users_tried_to_follow}/25",
    )

except (tweepy.errors.TooManyRequests, tweepy.errors.TweepyException) as e:
    judgement = TwiErrorHandleJudgement(e)
    log_msg = judgement.judge()

    XLogger.exception_to_slack(
        ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
        log_msg,
    )

    TextFileOperator(x_text=XText(filepath)).write(
        e.api_codes[0], is_overwrite=True, encoding="UTF-8"
    )

print("debug")
