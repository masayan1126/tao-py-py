import abc


class IJudgement:
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def judge(self):
        pass
