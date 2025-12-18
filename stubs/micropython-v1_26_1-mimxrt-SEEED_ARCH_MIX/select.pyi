"""
Module: 'select' on micropython-v1.26.1-mimxrt-SEEED_ARCH_MIX
"""

# MCU: {'variant': '', 'build': '', 'arch': 'armv7emdp', 'port': 'mimxrt', 'board': 'SEEED_ARCH_MIX', 'board_id': 'SEEED_ARCH_MIX', 'mpy': 'v6.3', 'ver': '1.26.1', 'family': 'micropython', 'cpu': 'MIMXRT1052DVL5B', 'version': '1.26.1'}
# Stubber: v1.26.3
from __future__ import annotations
from typing import Final
from _typeshed import Incomplete

POLLOUT: Final[int] = 4
POLLIN: Final[int] = 1
POLLHUP: Final[int] = 16
POLLERR: Final[int] = 8

def select(*args, **kwargs) -> Incomplete: ...
def poll(*args, **kwargs) -> Incomplete: ...
