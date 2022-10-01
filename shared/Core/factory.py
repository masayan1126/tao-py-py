import abc


class Factory:
    @abc.abstractmethod
    def create(self):
        pass
