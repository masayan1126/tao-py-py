from abc import *

# インターフェース
class Scraper(metaclass=ABCMeta):
    @abstractmethod
    def find_by_id(id_name: str):
        pass
