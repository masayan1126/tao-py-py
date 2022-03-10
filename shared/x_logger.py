from logging import DEBUG, FileHandler, Formatter, Logger, StreamHandler, getLogger
import os
from slack_log_handler import SlackLogHandler


class XLogger:
    @staticmethod
    def debug(msg: str, data=None) -> None:
        # loggerオブジェクトの生成
        logger = getLogger(__name__)

        # どのようにログを出力するかを制御するオブジェクト
        # handler = StreamHandler()  # 標準出力
        handler = FileHandler("logs/log.txt")  # ファイルへの出力

        # 出力するログレベルの設定
        # ケースによって使い分ける(DEBUG,INFO,WARNING,ERROR,CRITICAL)
        # handlerにセットされたログレベルよりレベルが低いログは出力されない
        # 例えば、handlerにWARNINGのログレベルをセットすると、DEBUGやINFOのログは出力されない
        handler.setLevel(DEBUG)
        logger.setLevel(DEBUG)

        # loggerオブジェクトにhandlerをセット
        logger.addHandler(handler)

        # 2.ログの出力フォーマット
        formatter = Formatter(
            "[%(asctime)s] : %(levelname)s - %(message)s - (%(filename)s)"
        )
        handler.setFormatter(formatter)

        logger.debug(f"{msg}:%s", data)

    @staticmethod
    def error(msg: str, data=None) -> None:
        # loggerオブジェクトの生成
        logger = getLogger(__name__)

        # どのようにログを出力するかを制御するオブジェクト
        # handler = StreamHandler()  # 標準出力
        handler = FileHandler("logs/log.txt", encoding="utf-8")  # ファイルへの出力

        # 出力するログレベルの設定
        # ケースによって使い分ける(DEBUG,INFO,WARNING,ERROR,CRITICAL)
        # handlerにセットされたログレベルよりレベルが低いログは出力されない
        # 例えば、handlerにWARNINGのログレベルをセットすると、DEBUGやINFOのログは出力されない
        handler.setLevel(DEBUG)
        logger.setLevel(DEBUG)

        # loggerオブジェクトにhandlerをセット
        logger.addHandler(handler)

        # 2.ログの出力フォーマット
        formatter = Formatter(
            "[%(asctime)s] : %(levelname)s - %(message)s - (%(filename)s) - %(lineno)d"
        )
        handler.setFormatter(formatter)

        logger.error(msg)

    @staticmethod
    def exception(msg: str, data=None) -> None:
        # loggerオブジェクトの生成
        logger = getLogger(__name__)

        # どのようにログを出力するかを制御するオブジェクト
        handler = StreamHandler()  # 標準出力
        # handler = FileHandler("logs/log.txt", encoding="utf-8")  # ファイルへの出力

        # 出力するログレベルの設定
        # ケースによって使い分ける(DEBUG,INFO,WARNING,ERROR,CRITICAL)
        # handlerにセットされたログレベルよりレベルが低いログは出力されない
        # 例えば、handlerにWARNINGのログレベルをセットすると、DEBUGやINFOのログは出力されない
        handler.setLevel(DEBUG)
        logger.setLevel(DEBUG)

        # loggerオブジェクトにhandlerをセット
        logger.addHandler(handler)

        # 2.ログの出力フォーマット
        formatter = Formatter(
            "[%(asctime)s] : %(levelname)s - %(message)s - (%(filename)s) - %(lineno)d"
        )
        handler.setFormatter(formatter)

        logger.exception(msg)

    @staticmethod
    def exceptionToSlack(msg: str) -> None:

        WEBHOOK_URL = os.environ.get("WEBHOOK_URL_JOBCAN")

        handler = SlackLogHandler(WEBHOOK_URL)
        handler.setLevel(DEBUG)
        logger = getLogger(__name__)
        logger.setLevel(DEBUG)
        logger.addHandler(handler)
        logger.exception(msg)
