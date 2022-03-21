import abc
from typing import Callable, List
from shared.Domain.xfolder import XFolder
from shared.i_aggregate import IAggregate
from shared.x_folder_iterator import XFolderIterator


class XFolderAggregate(IAggregate):
    def __init__(self):
        self.x_folder_list = []

    def addItem(self, xfolder: XFolder):
        self.x_folder_list.append(xfolder)
        return self.x_folder_list

    def size(self) -> int:
        return len(self.x_folder_list)

    def itemAt(self, index: int) -> XFolder:
        return self.x_folder_list[index]

    def iterator(self) -> XFolderIterator:
        return XFolderIterator(self)

    def map(self, callable: Callable) -> XFolderIterator:
        return list(
            map(
                lambda item: callable(item),
                self.x_folder_list,
            )
        )
