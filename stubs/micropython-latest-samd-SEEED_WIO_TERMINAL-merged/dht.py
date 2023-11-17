"""
Module: 'dht' on micropython-v1.21.0-samd-SEEED_WIO_TERMINAL
"""
# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'SAMD51P19A', 'arch': 'armv7emsp'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete


def dht_readinto(*args, **kwargs) -> Incomplete:
    ...


class DHT22:
    def humidity(self, *args, **kwargs) -> Incomplete:
        ...

    def temperature(self, *args, **kwargs) -> Incomplete:
        ...

    def measure(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class DHT11:
    def humidity(self, *args, **kwargs) -> Incomplete:
        ...

    def temperature(self, *args, **kwargs) -> Incomplete:
        ...

    def measure(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class DHTBase:
    def measure(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
