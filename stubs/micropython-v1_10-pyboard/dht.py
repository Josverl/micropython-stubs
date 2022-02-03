"""
Module: 'dht' on micropython-v1.10-pyboard
"""
# MCU: {'ver': 'v1.10', 'build': '', 'platform': 'pyboard', 'port': 'pyboard', 'machine': 'PYBv1.1 with STM32F405RG', 'release': '1.10.0', 'nodename': 'pyboard', 'name': 'micropython', 'family': 'micropython', 'sysname': 'pyboard', 'version': '1.10.0'}
# Stubber: 1.5.4
from typing import Any


def dht_readinto(*args, **kwargs) -> Any:
    ...


class DHTBase:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def measure(self, *args, **kwargs) -> Any:
        ...


class DHT11:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def measure(self, *args, **kwargs) -> Any:
        ...

    def humidity(self, *args, **kwargs) -> Any:
        ...

    def temperature(self, *args, **kwargs) -> Any:
        ...


class DHT22:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def measure(self, *args, **kwargs) -> Any:
        ...

    def humidity(self, *args, **kwargs) -> Any:
        ...

    def temperature(self, *args, **kwargs) -> Any:
        ...
