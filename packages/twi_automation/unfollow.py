from packages.twi_automation.Domain.twi_error_handle_judgement_service import (
    TwiErrorHandleJudgementService,
)

from packages.twi_automation.env import ENV
from shared.Domain.Twi.twitter_operator import TwitterOperator
from shared.Domain.Log.x_logger import XLogger
import tweepy


try:
    twitter_operator = TwitterOperator()
    unfollowed_user_screen_names = twitter_operator.unfollow()

except (tweepy.errors.TooManyRequests, tweepy.errors.TweepyException) as e:
    judgement = TwiErrorHandleJudgementService(e)
    log_msg = judgement.judge()

    XLogger.exception_to_slack(
        ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
        log_msg,
    )
finally:
    if "unfollowed_user_screen_names" in locals():
        XLogger.notification_to_slack(
            ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
            "{0}のフォローを解除しました。".format(unfollowed_user_screen_names),
        )

print("debug")
