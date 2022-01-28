"""
Module: 'dht' on micropython-v1.17-esp8266
"""
# MCU: {'ver': 'v1.17', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.17', 'name': 'micropython', 'mpy': 9733, 'version': '1.17', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
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
