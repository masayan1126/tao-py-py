import abc

from shared.Domain.String.xstr import XStr
from shared.Domain.Twi.tweet import Tweet


class TwitterOperator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def do_tweet(self) -> Tweet:
        pass

    @abc.abstractmethod
    def favorite(self, hashtag: XStr):
        pass

    @abc.abstractmethod
    def follow(self, hashtag: XStr):
        pass

    @abc.abstractmethod
    def unfollow(self, max_unfollow_count: int):
        pass

    @abc.abstractmethod
    def fetch_timeline(
        self, screen_name: XStr, count: int, since_id: int = None
    ) -> list[Tweet]:
        pass

    @abc.abstractmethod
    def follower_ids(self, screen_name: str) -> list[int]:
        pass

    @abc.abstractmethod
    def follow_ids(self, screen_name: str) -> list[int]:
        pass
