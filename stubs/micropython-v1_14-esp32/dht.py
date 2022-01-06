"""
Module: 'dht' on micropython-v1.14-esp32
"""
# MCU: {'ver': 'v1.14', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.14.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.14.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
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
