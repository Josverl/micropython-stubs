"""
Module: 'asyncio.lock' on micropython-v1.21.0-rp2-RPI_PICO_W
"""
# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete


class Lock:
    def locked(self, *args, **kwargs) -> Incomplete:
        ...

    def release(self, *args, **kwargs) -> Incomplete:
        ...

    acquire: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...
