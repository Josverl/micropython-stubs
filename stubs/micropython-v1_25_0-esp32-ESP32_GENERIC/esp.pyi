"""
Module: 'esp' on micropython-v1.25.0-esp32-ESP32_GENERIC
"""

# MCU: {'version': '1.25.0', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': '1.25.0', 'cpu': 'ESP32'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Final
from _typeshed import Incomplete

LOG_NONE: Final[int] = 0
LOG_WARNING: Final[int] = 2
LOG_VERBOSE: Final[int] = 5
LOG_DEBUG: Final[int] = 4
LOG_INFO: Final[int] = 3
LOG_ERROR: Final[int] = 1

def osdebug(*args, **kwargs) -> Incomplete: ...
def flash_write(*args, **kwargs) -> Incomplete: ...
def gpio_matrix_in(*args, **kwargs) -> Incomplete: ...
def gpio_matrix_out(*args, **kwargs) -> Incomplete: ...
def flash_user_start(*args, **kwargs) -> Incomplete: ...
def flash_erase(*args, **kwargs) -> Incomplete: ...
def flash_read(*args, **kwargs) -> Incomplete: ...
def flash_size(*args, **kwargs) -> Incomplete: ...
