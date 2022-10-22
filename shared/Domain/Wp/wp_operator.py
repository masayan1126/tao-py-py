from abc import ABCMeta, abstractmethod

from shared.Domain.Wp.post import Post


class WpOperator(metaclass=ABCMeta):
    @abstractmethod
    def response_headers(self):
        pass

    @abstractmethod
    def total_page_count(self) -> int:
        pass

    @abstractmethod
    def total_posts_count(self) -> int:
        pass

    @abstractmethod
    def fetch_posts(self) -> list[Post]:
        pass
