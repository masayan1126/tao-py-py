from shared.Domain.FileSystem.x_folder import XFolder

from shared.Core.iterator import Iterator
from shared.Core.aggregate import Aggregate


class XFolderIterator(Iterator):
    def __init__(self, i_aggregate: Aggregate):
        self.i_aggregate = i_aggregate
        self.index = 0

    def has_next(self) -> bool:
        return self.index < self.i_aggregate.size()

    def next(self) -> XFolder:
        next = self.i_aggregate.item_at(self.index)
        self.index = self.index + 1
        return next
