# openの返り値はファイルオブジェクト
# openでファイルが開けないときは、FileNotFoundErrorが送出
# mode
# 読み込み(r または rt)
# 書き込み(w または wt)
# 追記(a または at)

import sys
from shared.Domain.xtext import XText
from shared.x_logger import XLogger


class OpenTextService:
    def execute(self, x_text: XText, mode, encoding):
        try:
            f = open(file=x_text.get_path(), mode=mode, encoding=encoding)
            return f.read()

        except FileNotFoundError:
            XLogger.exceptionToSlack("対象のファイルが存在しないか、破損しています")
            sys.exit()
        finally:
            # 必ず閉じる。閉じていないファイルに再びアクセスしたら、ファイルが開きっぱなしなので開けない等になる
            # with文を使用すれば、自動で閉じてくれる
            if "f" in locals():
                f.close()
