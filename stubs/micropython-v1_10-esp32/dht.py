"""
Module: 'dht' on micropython-v1.10-esp32
"""
# MCU: {'ver': 'v1.10', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module with ESP32', 'release': '1.10.0', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.10.0'}
# Stubber: 1.5.0
from typing import Any


def dht_readinto(*args) -> Any:
    ...


class DHTBase:
    """"""

    def __init__(self, *args) -> None:
        ...

    def measure(self, *args) -> Any:
        ...


class DHT11:
    """"""

    def __init__(self, *args) -> None:
        ...

    def measure(self, *args) -> Any:
        ...

    def humidity(self, *args) -> Any:
        ...

    def temperature(self, *args) -> Any:
        ...


class DHT22:
    """"""

    def __init__(self, *args) -> None:
        ...

    def measure(self, *args) -> Any:
        ...

    def humidity(self, *args) -> Any:
        ...

    def temperature(self, *args) -> Any:
        ...
