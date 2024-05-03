"""
Module: 'uasyncio.lock' on micropython-v1.22.0-samd-SEEED_WIO_TERMINAL
"""

# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'cpu': 'SAMD51P19A', 'mpy': 'v6.2', 'arch': 'armv7emsp'}
# Stubber: v1.16.2
from _typeshed import Incomplete


class Lock:
    def locked(self, *args, **kwargs) -> Incomplete: ...

    def release(self, *args, **kwargs) -> Incomplete: ...

    acquire: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...
