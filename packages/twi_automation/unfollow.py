from shared.Core.Log.log_handler import LogHandler
from shared.Core.Log.log_type import LogType
from shared.Core.operator_factory import OperatorFactory
from shared.Core.operator_type import OperatorType
from shared.Domain.Twi.twi_error_judgement import (
    TwiErrorJudgement,
)
from packages.twi_automation.env import ENV


try:

    twitter_operator = OperatorFactory().create(OperatorType.TWI)
    total_unfollow_count, unfollowed_user_screen_names = twitter_operator.unfollow()

except Exception as e:
    judgement = TwiErrorJudgement(e)
    error_message = judgement.judge()

    LogHandler(
        LogType.EXCEPTION,
        error_message,
    ).to_slack(ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"])
finally:
    if (
        "total_unfollow_count" in locals()
        and "unfollowed_user_screen_names" in locals()
    ):
        LogHandler(
            LogType.EXCEPTION,
            f"{total_unfollow_count}人のフォローを解除しました。\n {unfollowed_user_screen_names}",
        ).to_slack(ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"])
