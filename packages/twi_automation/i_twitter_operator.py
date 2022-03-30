import abc

class ITwitterOperator:
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def tweet(self):
        pass

    @abc.abstractmethod
    def favorite(self, hashtag: str):
        pass

    @abc.abstractmethod
    # FIXME: XStrを使う
    def follow(self, hashtag: str):
        pass

    @abc.abstractmethod
    def unfollow(self, my_screen_name:str):
        pass

    @abc.abstractmethod
    def analyze(self, my_screen_name:str):
        pass
