import abc


class IReceiver:
    @abc.abstractmethod
    def action(self):
        pass
