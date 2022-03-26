import abc


class IIterator:
    @abc.abstractmethod
    def __str__(self):
        pass

    @abc.abstractmethod
    def has_next(self) -> bool:
        pass

    def next(self):
        pass
