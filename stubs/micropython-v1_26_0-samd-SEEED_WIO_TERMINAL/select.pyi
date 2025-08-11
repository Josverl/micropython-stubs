"""
Module: 'select' on micropython-v1.26.0-samd-SEEED_WIO_TERMINAL
"""

# MCU: {'variant': '', 'build': '', 'arch': 'armv7emsp', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'board_id': 'SEEED_WIO_TERMINAL', 'mpy': 'v6.3', 'ver': '1.26.0', 'family': 'micropython', 'cpu': 'SAMD51P19A', 'version': '1.26.0'}
# Stubber: v1.25.1
from __future__ import annotations
from typing import Final
from _typeshed import Incomplete

POLLOUT: Final[int] = 4
POLLIN: Final[int] = 1
POLLHUP: Final[int] = 16
POLLERR: Final[int] = 8

def select(*args, **kwargs) -> Incomplete: ...
def poll(*args, **kwargs) -> Incomplete: ...
