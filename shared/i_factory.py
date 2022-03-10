import abc


class IFactory:
    @abc.abstractmethod
    def create(self):
        pass
