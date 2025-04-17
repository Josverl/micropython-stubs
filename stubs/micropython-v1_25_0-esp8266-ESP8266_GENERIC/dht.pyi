"""
Module: 'dht' on micropython-v1.25.0-esp8266-ESP8266_GENERIC
"""
# MCU: {'version': '1.25.0', 'mpy': 'v6.3', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensa', 'ver': '1.25.0', 'cpu': 'ESP8266'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

def dht_readinto(*args, **kwargs) -> Incomplete:
    ...


class DHTBase():
    def measure(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class DHT22():
    def measure(self, *args, **kwargs) -> Incomplete:
        ...

    def temperature(self, *args, **kwargs) -> Incomplete:
        ...

    def humidity(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class DHT11():
    def measure(self, *args, **kwargs) -> Incomplete:
        ...

    def temperature(self, *args, **kwargs) -> Incomplete:
        ...

    def humidity(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

