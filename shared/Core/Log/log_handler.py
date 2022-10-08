from dataclasses import dataclass
from logging import DEBUG, Formatter, getLogger
from shared.Core.Log.log_type import LogType
from slack_log_handler import SlackLogHandler

# 1.出力先
# handler = StreamHandler()  # 標準出力
# handler = FileHandler("logs/log.txt", encoding="utf-8")  # ファイルへの出力

# 2.ログレベル
# ケースによって使い分ける(DEBUG,INFO,WARNING,ERROR,CRITICAL)
# handlerにセットされたログレベルよりレベルが低いログは出力されない
# 例えば、handlerにWARNINGのログレベルをセットすると、DEBUGやINFOのログは出力されない
# handler.setLevel(DEBUG)
# logger.setLevel(DEBUG)

# 3.ログの出力フォーマット
# formatter = Formatter(
#     "[%(asctime)s] : %(levelname)s - %(message)s - (%(filename)s)"
# )


@dataclass
class LogHandler:
    log_type: LogType
    log_message: str
    caller = None

    def to_slack(self, webhook_url: str):
        if self.log_type == LogType.EXCEPTION:
            formatter = Formatter(":fire: *Exception!!* \n `%(message)s` \n\n")
        elif self.log_type == LogType.NOTIFICATION:
            formatter = Formatter(":tada: *Notification* \n `%(message)s` \n\n")

        handler = SlackLogHandler(webhook_url)
        handler.setLevel(DEBUG)
        handler.setFormatter(formatter)

        logger = getLogger(self.caller)
        logger.setLevel(DEBUG)
        logger.addHandler(handler)

        if self.log_type == LogType.EXCEPTION:
            logger.exception(self.log_message, stack_info=True)
            return "Exception to slack"
        elif self.log_type == LogType.NOTIFICATION:
            logger.info(self.log_message, stack_info=True)
            return "Notification to slack"
