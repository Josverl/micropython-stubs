"""
Module: 'uasyncio.lock' on micropython-v1.20.0-samd-ADAFRUIT_FEATHER_M4_EXPRESS
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'samd', 'board': 'ADAFRUIT_FEATHER_M4_EXPRESS', 'cpu': 'SAMD51J19A', 'mpy': 'v6.1', 'arch': 'armv7emsp'})
# Stubber: v1.13.7
from typing import Any


class Lock:
    def release(self, *args, **kwargs) -> Any:
        ...

    def locked(self, *args, **kwargs) -> Any:
        ...

    acquire: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...
