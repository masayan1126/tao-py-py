# 読み込み(r または rt)
# 書き込み(w または wt)
# 追記(a または at)

from abc import ABCMeta, abstractmethod


class TextFileOperator(metaclass=ABCMeta):
    @abstractmethod
    def _open(self) -> None:
        pass

    @abstractmethod
    def read(self) -> None:
        pass

    @abstractmethod
    def readlines(self) -> None:
        pass

    @abstractmethod
    def write(self) -> None:
        pass
