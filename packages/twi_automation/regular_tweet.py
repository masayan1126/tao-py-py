from shared.Core.Log.log_handler import LogHandler
from shared.Core.Log.log_type import LogType
from shared.Domain.Twi.twi_error_judgement import (
    TwiErrorJudgement,
)
from packages.twi_automation.env import ENV
from shared.Domain.Time.x_date_time import XDateTime
from shared.Domain.String.xstr import XStr
from shared.Domain.Twi.twitter_operator_factory import TwitterOperatorFactory
from shared.Domain.Twi.twitter_operator_factory_option import (
    TwitterOperatorFactoryOption,
)
from tweepy import errors

now = XDateTime.now()
tweet = ENV["REGULAR_TWEET"]

tweet_content = XStr(f"{tweet}{now.format('%Y/%m/%d %H:%M:%S')}")

try:
    factory_option = TwitterOperatorFactoryOption(
        ENV["MY_SCREEN_NAME"], ENV["BLACK_LIST"]
    )

    operator = TwitterOperatorFactory().create(factory_option)
    operator.do_tweet(tweet_content)

    LogHandler(
        LogType.NOTIFICATION,
        "Tweet was successful" "\n\n" f"{tweet_content.value()}",
        ENV["PACKAGE_NAME"],
    ).to_slack(ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"])

except (errors.TweepyException) as e:

    judgement = TwiErrorJudgement(e)
    log_msg = judgement.judge()

    LogHandler(
        LogType.EXCEPTION,
        log_msg,
        ENV["PACKAGE_NAME"],
    ).to_slack(ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"])
