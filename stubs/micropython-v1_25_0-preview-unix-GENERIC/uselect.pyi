"""
Module: 'uselect' on micropython-v1.25.0-preview-unix
"""
# MCU: {'family': 'micropython', 'version': '1.25.0-preview', 'build': '301', 'ver': '1.25.0-preview-301', 'port': 'unix', 'board': '', 'cpu': 'linux [GCC 12.4.0] version', 'mpy': 'v6.3', 'arch': 'x64'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

POLLOUT: Final[int] = 4
POLLIN: Final[int] = 1
POLLHUP: Final[int] = 16
POLLERR: Final[int] = 8
def poll(*args, **kwargs) -> Incomplete:
    ...

