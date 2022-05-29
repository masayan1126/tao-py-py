from packages.xserver.Application.login_xserver_usecase import LoginXserverUsecase
from shared.Domain.Log.x_logger import XLogger
from packages.today_task_notification.env import ENV
from packages.today_task_notification.env import ENV
from shared.Domain.Log.x_logger import XLogger
from selenium.common.exceptions import SessionNotCreatedException

try:
    web_browser_operator = LoginXserverUsecase().login()

except SessionNotCreatedException as e:
    XLogger.exception_to_slack(
        ENV["SLACK_WEBHOOK_URL_COMMON"],
        e,
    )
    raise e


print("debug")
