from shared.Core.Log.log_handler import LogHandler
from shared.Core.Log.log_type import LogType
from shared.Domain.Twi.twi_error_judgement import (
    TwiErrorJudgement,
)
from packages.twi_automation.env import ENV
from shared.Domain.Twi.twitter_operator_factory import TwitterOperatorFactory
from shared.Domain.Twi.twitter_operator_factory_option import (
    TwitterOperatorFactoryOption,
)


try:
    factory_option = TwitterOperatorFactoryOption(
        ENV["MY_SCREEN_NAME"], ENV["BLACK_LIST"]
    )
    operator = TwitterOperatorFactory().create(factory_option)
    total_unfollow_count, unfollowed_user_screen_names = operator.unfollow()

except Exception as e:
    judgement = TwiErrorJudgement(e)
    error_message = judgement.judge()

    LogHandler(
        LogType.EXCEPTION,
        error_message,
        ENV["PACKAGE_NAME"],
    ).to_slack(ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"])
finally:
    if (
        "total_unfollow_count" in locals()
        and "unfollowed_user_screen_names" in locals()
    ):
        LogHandler(
            LogType.NOTIFICATION,
            f"{total_unfollow_count}人のフォローを解除しました。\n {unfollowed_user_screen_names}",
            ENV["PACKAGE_NAME"],
        ).to_slack(ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"])
