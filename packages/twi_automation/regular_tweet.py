from shared.Core.Log.log_handler import LogHandler
from shared.Core.Log.log_type import LogType
from shared.Core.operator_factory import OperatorFactory
from shared.Core.operator_type import OperatorType
from shared.Domain.Twi.twi_error_judgement import (
    TwiErrorJudgement,
)
from packages.twi_automation.env import ENV
from shared.Domain.Time.x_date_time import XDateTime
from shared.Domain.String.xstr import XStr
from tweepy import errors

now = XDateTime.now()
tweet = ENV["REGULAR_TWEET"]

tweet_content = XStr(f"{tweet}{now.format('%Y/%m/%d %H:%M:%S')}")
twitter_operator = OperatorFactory().create(OperatorType.TWI)

try:
    LogHandler(
        LogType.NOTIFICATION,
        "Tweet was successful" "\n\n" f"{tweet_content.value()}",
    ).to_slack(ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"])

except (errors.TweepyException) as e:

    judgement = TwiErrorJudgement(e)
    log_msg = judgement.judge()

    LogHandler(
        LogType.NOTIFICATION,
        log_msg,
    ).to_slack(ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"])
