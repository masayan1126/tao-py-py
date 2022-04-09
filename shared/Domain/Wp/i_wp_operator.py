import abc


class IWpOperator:
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def response_headers(self):
        pass

    @abc.abstractmethod
    def total_page_count(self):
        pass

    @abc.abstractmethod
    def total_posts_count(self):
        pass

    @abc.abstractmethod
    def fetch_posts(self):
        pass
