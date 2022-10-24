import abc

from shared.Core.iterator import Iterator


class Aggregate:
    @abc.abstractmethod
    def __init__(self):
        pass

    def add_item(self):
        pass

    def size(self) -> int:
        pass

    def item_at(self, index: int):
        pass

    def iterator(self) -> Iterator:
        return Iterator(self)
