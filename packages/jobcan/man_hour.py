from packages.jobcan.Application.login_jobcan_usecase import LoginJobcanUsecase
from packages.jobcan.Application.pick_up_needs_fix_records_usecase import (
    PickUpNeedsFixRecordsUsecase,
)

from packages.jobcan.Application.register_manhour_usecase import RegisterManhourUseCase

# ログイン
# jobcanを起動し、昨日分の工数レコードを開き、テンプレートから工数を入力
# 修正が必要な工数レコードをピックアップ

web_browser_operator = LoginJobcanUsecase().handle()
RegisterManhourUseCase().handle(web_browser_operator)
PickUpNeedsFixRecordsUsecase().handle(web_browser_operator)

print("debug")
