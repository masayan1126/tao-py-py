import abc
from functools import total_ordering
from types import NotImplementedType


@total_ordering
class BaseClass(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __str__(self, other) -> str:
        pass

    @abc.abstractmethod
    def __eq__(self, other) -> NotImplementedType | bool:
        pass

    @abc.abstractmethod
    def __lt__(self, other) -> NotImplementedType | bool:
        pass
