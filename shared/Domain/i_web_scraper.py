from abc import *

from shared.Enums.ScrapingType import ScrapingType

# インターフェース
class IWebScraper(metaclass=ABCMeta):
    @abstractmethod
    def get_scraper_type(self) -> ScrapingType:
        pass

    @abstractmethod
    def get_scraper(self):
        pass
