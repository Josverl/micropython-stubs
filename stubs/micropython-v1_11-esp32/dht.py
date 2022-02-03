"""
Module: 'dht' on micropython-v1.11-esp32
"""
# MCU: {'ver': 'v1.11', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module with ESP32', 'release': '1.11.0', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.11.0'}
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
