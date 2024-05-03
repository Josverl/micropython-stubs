"""
Module: 'uasyncio.lock' on micropython-v1.20.0-samd-ADAFRUIT_ITSYBITSY_M4_EXPRESS
"""

# MCU: OrderedDict({'build': '', 'ver': 'v1.20.0', 'version': '1.20.0', 'port': 'samd', 'board': 'ADAFRUIT_ITSYBITSY_M4_EXPRESS', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'SAMD51G19A', 'arch': 'armv7emsp'})
# Stubber: v1.13.7
from typing import Any


class Lock:
    def release(self, *args, **kwargs) -> Any: ...

    def locked(self, *args, **kwargs) -> Any: ...

    acquire: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...
