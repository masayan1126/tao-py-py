from shared.x_logger import XLogger


class XDriver:
    def __init__(self, closure):
        self._closure = closure

    def driver(self):
        try:
            return self._closure()
        except:
            # TODO: ログの出し分け
            XLogger.exceptionToSlack(
                "webdriverのバージョンがChromeブラウザーのバージョンと一致していないため起動に失敗しました。"
            )
            XLogger.exception("webdriverのバージョンがChromeブラウザーのバージョンと一致していないため起動に失敗しました。")
