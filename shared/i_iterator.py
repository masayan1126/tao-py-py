import abc


class IIterator:
    @abc.abstractmethod
    def __str__(self):
        pass

    @abc.abstractmethod
    def hasNext(self) -> bool:
        pass

    def next(self):
        pass
