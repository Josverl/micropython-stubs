"""
Module: 'machine' on micropython-v1.27.0-preview-windows-standard
"""
# MCU: {'family': 'micropython', 'version': '1.27.0-preview', 'build': '218', 'ver': '1.27.0-preview-218', 'port': 'windows', 'board': 'standard', 'board_id': 'standard', 'variant': '', 'cpu': 'win32 [GCC 12.0.0] version', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.26.2
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
