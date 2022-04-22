from packages.twi_automation.Domain.twi_error_handle_judgement import (
    TwiErrorHandleJudgement,
)
from packages.twi_automation.env import ENV
from shared.Domain.Twi.twitter_operator import TwitterOperator
from shared.Domain.xstr import XStr
from shared.x_logger import XLogger
import tweepy

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

print("debug")
