"""
Module: 'umachine' on micropython-v1.21.0-unix-linux_[GCC_9.4.0]_version
"""
# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'unix', 'board': 'linux_[GCC_9.4.0]_version', 'cpu': '', 'mpy': '', 'arch': ''}
# Stubber: v1.15.1
from typing import Any
from _typeshed import Incomplete


def time_pulse_us(*args, **kwargs) -> Incomplete:
    ...


def idle(*args, **kwargs) -> Incomplete:
    ...


mem32: Incomplete  ## <class 'mem'> = <32-bit memory>
mem8: Incomplete  ## <class 'mem'> = <8-bit memory>


class Signal:
    def off(self, *args, **kwargs) -> Incomplete:
        ...

    def on(self, *args, **kwargs) -> Incomplete:
        ...

    def value(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


mem16: Incomplete  ## <class 'mem'> = <16-bit memory>


class PinBase:
    def __init__(self, *argv, **kwargs) -> None:
        ...
