"""
Module: 'uasyncio.lock' on micropython-v1.22.2-esp8266-ESP8266_GENERIC
"""

# MCU: {'version': '1.22.2', 'mpy': 'v6.2', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensa', 'ver': '1.22.2', 'cpu': 'ESP8266'}
# Stubber: v1.20.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

class Lock:
    def locked(self, *args, **kwargs) -> Incomplete: ...
    def release(self, *args, **kwargs) -> Incomplete: ...

    acquire: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...
