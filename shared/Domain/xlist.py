class XList:
    @staticmethod
    def map(callable, iterable):

        return list(
            map(
                lambda item: callable(item),
                iterable,
            )
        )
