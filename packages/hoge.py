from shared.Domain.Excel.xexcel import XExcel
from shared.Domain.x_file_system_path import XFileSystemPath
from shared.Domain.xstr import XStr
from shared.x_logger import XLogger
from packages.twi_automation.env import ENV

try:
    filepath = XFileSystemPath(XStr("tests/Domain/Hoge/sample.xlsx")).to_absolute()
    xworkbook = XExcel().output(filepath, {})

except OSError as e:
    XLogger.exception_to_slack(
        ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
        e,
    )

print("debug")
