from shared.Domain.FileSystem.x_folder import XFolder

from shared.Core.i_iterator import IIterator
from shared.Core.i_aggregate import IAggregate


class XFolderIterator(IIterator):
    def __init__(self, i_aggregate: IAggregate):
        self.i_aggregate = i_aggregate
        self.index = 0

    def has_next(self) -> bool:
        return self.index < self.i_aggregate.size()

    def next(self) -> XFolder:
        next = self.i_aggregate.item_at(self.index)
        self.index = self.index + 1
        return next
