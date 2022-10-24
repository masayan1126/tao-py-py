import abc


class Receiver:
    @abc.abstractmethod
    def action(self):
        pass
