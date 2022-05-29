import abc


class IYtDownloader:
    @abc.abstractmethod
    def download(self):
        pass
