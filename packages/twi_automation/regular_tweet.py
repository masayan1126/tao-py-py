from shared.Domain.Twi.twi_error_judgement import (
    TwiErrorJudgement,
)
from packages.twi_automation.env import ENV
from shared.Domain.Time.x_date_time import XDateTime
from shared.Domain.Twi.twitter_operator import TwitterOperator
from shared.Domain.String.xstr import XStr
from shared.Domain.Log.x_logger import XLogger
from tweepy import errors

now = XDateTime.now()
tweet = ENV["REGULAR_TWEET"]

tweet_content = XStr(f"{tweet}{now.format('%Y/%m/%d %H:%M:%S')}")
twitter_operator = TwitterOperator()

try:
    response = twitter_operator.tweet(tweet_content)

    XLogger.notification_to_slack(
        ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
        "Tweet was successful" "\n\n" f"{tweet_content.value()}",
    )
except (errors.TweepyException) as e:

    judgement = TwiErrorJudgement(e)
    log_msg = judgement.judge()

    XLogger.exception_to_slack(
        ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
        log_msg,
    )

print("debug")
