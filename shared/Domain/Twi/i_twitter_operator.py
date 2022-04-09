import abc

from shared.Domain.xstr import XStr


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
    def unfollow(self, my_screen_name: XStr):
        pass

    @abc.abstractmethod
    def analyze(self, my_screen_name: XStr):
        pass
