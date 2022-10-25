# 読み込み(r または rt)
# 書き込み(w または wt)
# 追記(a または at)

from abc import ABCMeta, abstractmethod


class TextFileOperator(metaclass=ABCMeta):
    @abstractmethod
    def _open(self) -> None:
        pass

    @abstractmethod
    def read(self) -> str:
        pass

    @abstractmethod
    def readlines(self) -> list[str]:
        pass

    @abstractmethod
    def write(self) -> str:
        pass
