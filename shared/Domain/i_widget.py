from abc import abstractmethod, ABCMeta


class IWidget(metaclass=ABCMeta):
    @abstractmethod
    def build(self) -> None:
        pass

    @abstractmethod
    def label(self):
        pass

    @abstractmethod
    def btn(self):
        pass

    # @abstractmethod
    # def input_field(self):
    #     pass

    # @abstractmethod
    # def input_handler(self):
    #     pass

    # @abstractmethod
    # def message(self):
    #     pass
