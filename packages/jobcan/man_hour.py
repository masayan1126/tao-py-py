from packages.jobcan.Application.login_service import LoginService
from packages.jobcan.Application.pick_up_needs_fix_records import (
    PickUpNeedsFixRecordsService,
)
from packages.jobcan.Application.register_manhour_service import RegisterManhourService

# ログイン
# jobcanを起動し、昨日分の工数レコードを開き、テンプレートから工数を入力
# 修正が必要な工数レコードをピックアップ

web_browser_operator = LoginService().handle()
RegisterManhourService().handle(web_browser_operator)
PickUpNeedsFixRecordsService().handle(web_browser_operator)

# print("debug")
