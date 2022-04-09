from shared.Domain.Twi.twitter_operator import TwitterOperator
from shared.Domain.xstr import XStr
from packages.twi_automation.env import ENV
from shared.x_logger import XLogger

twitter_operator = TwitterOperator()

try:
    report = twitter_operator.analyze(my_screen_name=XStr(ENV["MY_SCREEN_NAME"]))

    f = open(
        file="C:\\Users\\nishigaki\\jupyter-lab\\packages\\twi_automation\\analytics.txt",
        mode="a",
        encoding="UTF-8",
    )

    f.write(report)

except FileNotFoundError:
    XLogger.exception_to_slack(
        ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
        "対象のファイルが存在しないか、破損しています",
    )
    raise FileNotFoundError
finally:
    if "f" in locals():
        f.close()

print("degug")
