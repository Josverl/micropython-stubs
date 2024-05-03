"""
Module: 'uasyncio.lock' on micropython-v1.22.0-rp2-ARDUINO_NANO_RP2040_CONNECT
"""

# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'rp2', 'board': 'ARDUINO_NANO_RP2040_CONNECT', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.16.2
from _typeshed import Incomplete


class Lock:
    def locked(self, *args, **kwargs) -> Incomplete: ...

    def release(self, *args, **kwargs) -> Incomplete: ...

    acquire: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...
