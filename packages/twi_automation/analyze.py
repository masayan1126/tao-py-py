from shared.Domain.Twi.twitter_operator import TwitterOperator
from shared.Domain.x_file_system_path import XFileSystemPath
from shared.Domain.xstr import XStr
from packages.twi_automation.env import ENV
from shared.x_logger import XLogger

twitter_operator = TwitterOperator()

try:
    report = twitter_operator.analyze()

    f = open(
        file=XFileSystemPath(XStr("packages/twi_automation/analytics.txt")).of_text(),
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
