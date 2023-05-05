"""
Module: 'dht' on micropython-v1.20.0-samd-SEEED_WIO_TERMINAL
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'cpu': 'SAMD51P19A', 'mpy': 'v6.1', 'arch': 'armv7emsp'})
# Stubber: v1.13.4
from typing import Any


def dht_readinto(*args, **kwargs) -> Any:
    ...


class DHT22:
    def humidity(self, *args, **kwargs) -> Any:
        ...

    def temperature(self, *args, **kwargs) -> Any:
        ...

    def measure(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class DHT11:
    def humidity(self, *args, **kwargs) -> Any:
        ...

    def temperature(self, *args, **kwargs) -> Any:
        ...

    def measure(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class DHTBase:
    def measure(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
