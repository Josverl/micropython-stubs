"""
Module: 'network' on micropython-v1.17-pyboard
"""
# MCU: {'ver': 'v1.17', 'port': 'pyboard', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.17.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.17.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'pyboard', 'family': 'micropython'}
# Stubber: 1.5.2
from typing import Any


class CC3K:
    """"""

    WEP = 1  # type: int
    WPA = 2  # type: int
    WPA2 = 3  # type: int

    def connect(self, *args) -> Any:
        ...

    def disconnect(self, *args) -> Any:
        ...

    def ifconfig(self, *args) -> Any:
        ...

    def isconnected(self, *args) -> Any:
        ...

    def patch_program(self, *args) -> Any:
        ...

    def patch_version(self, *args) -> Any:
        ...


class WIZNET5K:
    """"""

    def ifconfig(self, *args) -> Any:
        ...

    def isconnected(self, *args) -> Any:
        ...

    def regs(self, *args) -> Any:
        ...


def route(*args) -> Any:
    ...
