from dataclasses import dataclass


@dataclass
class IpAddress:
    _address: str

    def value(self) -> str:
        return self._address
