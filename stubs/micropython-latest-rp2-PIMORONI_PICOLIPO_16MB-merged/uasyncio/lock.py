"""
Module: 'uasyncio.lock' on micropython-v1.20.0-rp2-PIMORONI_PICOLIPO_16MB
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'rp2', 'board': 'PIMORONI_PICOLIPO_16MB', 'cpu': 'RP2040', 'mpy': 'v6.1', 'arch': 'armv6m'})
# Stubber: v1.13.7
from typing import Any


class Lock:
    def locked(self, *args, **kwargs) -> Any:
        ...

    def release(self, *args, **kwargs) -> Any:
        ...

    acquire: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...
