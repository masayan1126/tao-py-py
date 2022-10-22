from shared.Core.Log.log_handler import LogHandler
from shared.Core.Log.log_type import LogType
from shared.Core.operator_factory import OperatorFactory
from shared.Core.operator_type import OperatorType
from shared.Domain.Twi.twi_error_judgement import (
    TwiErrorJudgement,
)
from packages.twi_automation.env import ENV
from shared.Domain.String.xstr import XStr
import tweepy

twitter_operator = OperatorFactory().create(OperatorType.TWI)

try:
    favorited_user_screen_names = twitter_operator.favorite(
        hashtag=XStr(ENV["HASH_TAG"])
    )

    LogHandler(
        LogType.NOTIFICATION,
        "Favorite was successful" "\n" f"{favorited_user_screen_names}",
        ENV["PACKAGE_NAME"],
    ).to_slack(ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"])

except (tweepy.errors.TooManyRequests, tweepy.errors.TweepyException) as e:

    judgement = TwiErrorJudgement(e)
    log_msg = judgement.judge()

    LogHandler(
        LogType.EXCEPTION,
        log_msg,
        ENV["PACKAGE_NAME"],
    ).to_slack(ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"])
