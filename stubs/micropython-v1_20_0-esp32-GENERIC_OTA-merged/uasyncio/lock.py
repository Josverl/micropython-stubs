"""
Module: 'uasyncio.lock' on micropython-v1.20.0-esp32-GENERIC_OTA
"""

# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'esp32', 'board': 'GENERIC_OTA', 'cpu': 'ESP32', 'mpy': 'v6.1', 'arch': 'xtensawin'})
# Stubber: v1.13.4
from typing import Any


class Lock:
    def locked(self, *args, **kwargs) -> Any: ...

    def release(self, *args, **kwargs) -> Any: ...

    acquire: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...
