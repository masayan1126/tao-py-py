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
    unfollowed_user_screen_names = twitter_operator.unfollow(
        my_screen_name=XStr(ENV["MY_SCREEN_NAME"])
    )
    XLogger.notification_to_slack(
        ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
        "{0}のフォローを解除しました。".format(unfollowed_user_screen_names),
    )
except (tweepy.errors.TooManyRequests, tweepy.errors.TweepyException) as e:
    judgement = TwiErrorHandleJudgement(e)
    log_msg = judgement.judge()

    XLogger.exception_to_slack(
        ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
        log_msg,
    )

print("debug")
