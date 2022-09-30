from dataclasses import dataclass
import ipaddress


@dataclass
class IpAddress:
    def __init__(self, address: str):
        try:
            ipaddress.ip_address(address)
            self._ip_address = address
        except ValueError as e:
            raise e

    def value(self) -> str:
        return self._ip_address
