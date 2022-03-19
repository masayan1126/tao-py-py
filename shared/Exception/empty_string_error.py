class EmptyStringError(Exception):
    def __init__(self, msg: str) -> None:
        self._msg = msg

    def __str__(self) -> str:
        return self._msg
