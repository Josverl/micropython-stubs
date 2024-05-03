"""
Module: 'asyncio.event' on micropython-v1.21.0-samd-SEEED_WIO_TERMINAL
"""

# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'cpu': 'SAMD51P19A', 'mpy': 'v6.1', 'arch': 'armv7emsp'}
# Stubber: v1.16.2
from _typeshed import Incomplete


class ThreadSafeFlag:
    def set(self, *args, **kwargs) -> Incomplete: ...

    def ioctl(self, *args, **kwargs) -> Incomplete: ...

    def clear(self, *args, **kwargs) -> Incomplete: ...

    wait: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class Event:
    def set(self, *args, **kwargs) -> Incomplete: ...

    def is_set(self, *args, **kwargs) -> Incomplete: ...

    def clear(self, *args, **kwargs) -> Incomplete: ...

    wait: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...
