import abc

from shared.i_iterator import IIterator


class IAggregate:
    @abc.abstractmethod
    def __init__(self):
        pass

    def add_item(self):
        pass

    def size(self) -> int:
        pass

    def item_at(self, index: int):
        pass

    def iterator(self) -> IIterator:
        return IIterator(self)
