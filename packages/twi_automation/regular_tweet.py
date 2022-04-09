from packages.twi_automation.Domain.twi_error_handle_judgement import (
    TwiErrorHandleJudgement,
)
from packages.twi_automation.env import ENV
from shared.Domain.Time.x_date_time import XDateTime
from shared.Domain.Twi.twitter_operator import TwitterOperator
from shared.Domain.xstr import XStr
from shared.x_logger import XLogger
from tweepy import errors

now = XDateTime.now()
tweet = ENV["REGULAR_TWEET"]

tweet_content = XStr(f"{tweet}{now.format('%Y/%m/%d %H:%M:%S')}")
twitter_operator = TwitterOperator()

try:
    response = twitter_operator.tweet(tweet_content)

    XLogger.notification_to_slack(
        ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
        "Tweet was successful" "\n\n" f"{tweet_content.get_string()}",
    )
except (errors.TweepyException) as e:

    judgement = TwiErrorHandleJudgement(e)
    log_msg = judgement.judge()

    XLogger.exception_to_slack(
        ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
        log_msg,
    )

print(response)
