"""
Module: 'dht' on micropython-v1.18-esp8266
"""
# MCU: {'ver': 'v1.18', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.18', 'name': 'micropython', 'mpy': 9733, 'version': '1.18', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.5.3
from typing import Any

def dht_readinto(*args) -> Any:
    ...


class DHTBase():
    ''
    def __init__(self, *argv, **kwargs) -> None:
        ''
        ...
    def __init__(self, *args) -> None:
        ...

    def measure(self, *args) -> Any:
        ...


class DHT11():
    ''
    def __init__(self, *argv, **kwargs) -> None:
        ''
        ...
    def __init__(self, *args) -> None:
        ...

    def measure(self, *args) -> Any:
        ...

    def humidity(self, *args) -> Any:
        ...

    def temperature(self, *args) -> Any:
        ...


class DHT22():
    ''
    def __init__(self, *argv, **kwargs) -> None:
        ''
        ...
    def __init__(self, *args) -> None:
        ...

    def measure(self, *args) -> Any:
        ...

    def humidity(self, *args) -> Any:
        ...

    def temperature(self, *args) -> Any:
        ...

