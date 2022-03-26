from typing import Callable
from selenium.common.exceptions import StaleElementReferenceException


class Retry:
    @staticmethod
    def do(callable: Callable, failed_process: Callable, max_retry_count: int):
        CURRENT_COUNT = 1

        while CURRENT_COUNT < max_retry_count:
            try:
                callable()

            except:
                failed_process()
                # if CURRENT_COUNT == max_retry_count:
                #     raise StaleElementReferenceException
            else:
                # 失敗しなかった時はループを抜ける
                break

            finally:
                CURRENT_COUNT += 1
