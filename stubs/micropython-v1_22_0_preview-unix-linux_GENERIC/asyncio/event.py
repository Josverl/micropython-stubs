"""
Module: 'asyncio.event' on micropython-v1.22.0.preview-unix-linux_[GCC_9.4.0]_version
"""
# MCU: {'family': 'micropython', 'version': '1.22.0.preview', 'build': '', 'ver': 'v1.22.0.preview', 'port': 'unix', 'board': 'linux_[GCC_9.4.0]_version', 'cpu': '', 'mpy': '', 'arch': ''}
# Stubber: v1.15.1
from typing import Any
from _typeshed import Incomplete


class ThreadSafeFlag:
    def set(self, *args, **kwargs) -> Incomplete:
        ...

    def ioctl(self, *args, **kwargs) -> Incomplete:
        ...

    def clear(self, *args, **kwargs) -> Incomplete:
        ...

    wait: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Event:
    def set(self, *args, **kwargs) -> Incomplete:
        ...

    def is_set(self, *args, **kwargs) -> Incomplete:
        ...

    def clear(self, *args, **kwargs) -> Incomplete:
        ...

    wait: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...
