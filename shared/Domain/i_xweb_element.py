from abc import *

# インターフェース
class IXWebElement(metaclass=ABCMeta):
    @abstractmethod
    def get_element(self):
        pass
