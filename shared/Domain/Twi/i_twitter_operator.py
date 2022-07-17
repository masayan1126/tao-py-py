import abc

from shared.Domain.String.xstr import XStr
from shared.Domain.Twi.tweet import Tweet


class ITwitterOperator:
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def tweet(self):
        pass

    @abc.abstractmethod
    def favorite(self, hashtag: XStr):
        pass

    @abc.abstractmethod
    def follow(self, hashtag: XStr):
        pass

    @abc.abstractmethod
    def unfollow(self):
        pass

    @abc.abstractmethod
    def fetch_timeline(
        self, screen_name: XStr, count: int, since_id: int = None
    ) -> list[Tweet]:
        pass

    @abc.abstractmethod
    def analyze(self):
        pass
