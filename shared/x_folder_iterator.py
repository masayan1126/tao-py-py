import abc
from shared.Domain.xfolder import XFolder

from shared.i_iterator import IIterator
from shared.i_aggregate import IAggregate


class XFolderIterator(IIterator):
    def __init__(self, i_aggregate: IAggregate):
        self.i_aggregate = i_aggregate
        self.index = 0

    def hasNext(self) -> bool:
        return self.index < self.i_aggregate.size()

    def next(self) -> XFolder:
        next = self.i_aggregate.itemAt(self.index)
        self.index = self.index + 1
        return next
