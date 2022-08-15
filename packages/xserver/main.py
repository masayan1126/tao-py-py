from packages.xserver.Application.login_xserver_usecase import LoginXserverUsecase
from packages.xserver.env import ENV
from shared.Domain.Automatic.automatic_operator import AutomaticOperator
from shared.Domain.Automatic.automatic_operator_impl import AutomaticOperatorImpl
from shared.Domain.Log.x_logger import XLogger
from selenium.common.exceptions import SessionNotCreatedException


def open_folder():
    # xserverのフォルダ開く
    automatic_operator: AutomaticOperator = AutomaticOperatorImpl()
    automatic_operator.click(x=127, y=466, duration=1, wait_time=2)
    automatic_operator.click(x=163, y=623, duration=1, wait_time=2)
    automatic_operator.click(x=124, y=759, duration=1, wait_time=2)
    automatic_operator.click(x=141, y=791, duration=1, wait_time=2)
    automatic_operator.click(x=181, y=884, duration=1, wait_time=2)


try:
    LoginXserverUsecase().login(open_folder)

except SessionNotCreatedException as e:
    XLogger.exception_to_slack(
        ENV["SLACK_WEBHOOK_URL_COMMON"],
        e,
    )
    raise e
