"""
Module: 'machine' on micropython-v1.24.1-unix
"""
# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'unix', 'board': '', 'cpu': 'linux [GCC 12.4.0] version', 'mpy': 'v6.3', 'arch': 'x64'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

def idle(*args, **kwargs) -> Incomplete:
    ...

def soft_reset(*args, **kwargs) -> Incomplete:
    ...

def time_pulse_us(*args, **kwargs) -> Incomplete:
    ...

mem8: Incomplete ## <class 'mem'> = <8-bit memory>

class PinBase():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class Signal():
    def off(self, *args, **kwargs) -> Incomplete:
        ...

    def on(self, *args, **kwargs) -> Incomplete:
        ...

    def value(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

mem32: Incomplete ## <class 'mem'> = <32-bit memory>
mem16: Incomplete ## <class 'mem'> = <16-bit memory>
