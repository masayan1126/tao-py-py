from shared.Domain.Twi.twi_error_judgement import (
    TwiErrorJudgement,
)
from packages.twi_automation.env import ENV
from shared.Domain.Twi.twitter_operator import TwitterOperator
from shared.Domain.String.xstr import XStr
from shared.Domain.Log.x_logger import XLogger
import tweepy

twitter_operator = TwitterOperator()

try:
    favorited_user_screen_names = twitter_operator.favorite(
        hashtag=XStr(ENV["HASH_TAG"])
    )

    XLogger.notification_to_slack(
        ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
        "Favorite was successful" "\n" f"{favorited_user_screen_names}",
    )
except (tweepy.errors.TooManyRequests, tweepy.errors.TweepyException) as e:

    judgement = TwiErrorJudgement(e)
    log_msg = judgement.judge()

    XLogger.exception_to_slack(
        ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
        log_msg,
    )
