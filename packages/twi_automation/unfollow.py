from shared.Domain.Twi.twi_error_judgement import (
    TwiErrorJudgement,
)

from packages.twi_automation.env import ENV
from shared.Domain.Twi.twitter_operator import TwitterOperator
from shared.Domain.Log.x_logger import XLogger
import tweepy


try:
    twitter_operator = TwitterOperator()
    total_unfollow_count, unfollowed_user_screen_names = twitter_operator.unfollow()

except (tweepy.errors.TooManyRequests, tweepy.errors.TweepyException) as e:
    judgement = TwiErrorJudgement(e)
    log_msg = judgement.judge()

    XLogger.exception_to_slack(
        ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
        log_msg,
    )
finally:
    if (
        "total_unfollow_count" in locals()
        and "unfollowed_user_screen_names" in locals()
    ):
        XLogger.notification_to_slack(
            ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
            f"{total_unfollow_count}人のフォローを解除しました。\n {unfollowed_user_screen_names}",
        )

print("debug")
