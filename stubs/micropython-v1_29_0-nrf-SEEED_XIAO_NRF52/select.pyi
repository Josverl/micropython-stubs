"""
Module: 'select' on micropython-v1.29.0-nrf-SEEED_XIAO_NRF52
"""

# MCU: {'variant': '', 'build': '', 'arch': 'armv7emsp', 'port': 'nrf', 'board': 'SEEED_XIAO_NRF52', 'board_id': 'SEEED_XIAO_NRF52', 'mpy': 'v6.3', 'ver': '1.29.0', 'family': 'micropython', 'cpu': 'NRF52840', 'version': '1.29.0'}
# Stubber: v1.28.6
from __future__ import annotations

from typing import Final

from _typeshed import Incomplete

POLLOUT: Final[int] = 4
POLLIN: Final[int] = 1
POLLHUP: Final[int] = 16
POLLERR: Final[int] = 8

def select(*args, **kwargs) -> Incomplete: ...
def poll(*args, **kwargs) -> Incomplete: ...
