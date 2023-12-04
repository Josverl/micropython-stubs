"""
Module: 'umachine' on micropython-v1.22.0.preview-win32-GENERIC
"""
# MCU: {'version': '1.22.0.preview', 'mpy': '', 'port': 'win32', 'board': 'GENERIC', 'family': 'micropython', 'build': '', 'arch': '', 'ver': 'v1.22.0.preview', 'cpu': ''}
# Stubber: v1.15.0
from typing import Any
from _typeshed import Incomplete


def idle(*args, **kwargs) -> Incomplete:
    ...


def soft_reset(*args, **kwargs) -> Incomplete:
    ...


def time_pulse_us(*args, **kwargs) -> Incomplete:
    ...


mem8: Incomplete  ## <class 'mem'> = <8-bit memory>


class PinBase:
    def __init__(self, *argv, **kwargs) -> None:
        ...


class Signal:
    def off(self, *args, **kwargs) -> Incomplete:
        ...

    def on(self, *args, **kwargs) -> Incomplete:
        ...

    def value(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


mem32: Incomplete  ## <class 'mem'> = <32-bit memory>
mem16: Incomplete  ## <class 'mem'> = <16-bit memory>
