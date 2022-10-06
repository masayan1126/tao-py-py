from shared.Core.operator_factory import OperatorFactory
from shared.Core.operator_type import OperatorType
from shared.Domain.Twi.twi_error_judgement import (
    TwiErrorJudgement,
)

from packages.twi_automation.env import ENV
from shared.Domain.Log.x_logger import XLogger


try:

    twitter_operator = OperatorFactory().create(OperatorType.TWI)
    total_unfollow_count, unfollowed_user_screen_names = twitter_operator.unfollow()

except Exception as e:
    judgement = TwiErrorJudgement(e)
    error_message = judgement.judge()

    XLogger.exception_to_slack(
        ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
        error_message,
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
