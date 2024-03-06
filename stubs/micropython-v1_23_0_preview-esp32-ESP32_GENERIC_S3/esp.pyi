"""
Module: 'esp' on micropython-v1.23.0-preview-esp32-ESP32_GENERIC_S3
"""
# MCU: {'version': '1.23.0-preview', 'mpy': 'v6.2', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'family': 'micropython', 'build': 'preview.176.g90e517862', 'arch': 'xtensawin', 'ver': '1.23.0-preview-preview.176.g90e517862', 'cpu': 'ESP32S3'}
# Stubber: v1.17.3
from __future__ import annotations
from _typeshed import Incomplete

LOG_NONE: int = 0
LOG_WARNING: int = 2
LOG_VERBOSE: int = 5
LOG_DEBUG: int = 4
LOG_INFO: int = 3
LOG_ERROR: int = 1

def osdebug(*args, **kwargs) -> Incomplete: ...
def flash_write(*args, **kwargs) -> Incomplete: ...
def gpio_matrix_in(*args, **kwargs) -> Incomplete: ...
def gpio_matrix_out(*args, **kwargs) -> Incomplete: ...
def flash_user_start(*args, **kwargs) -> Incomplete: ...
def flash_erase(*args, **kwargs) -> Incomplete: ...
def flash_read(*args, **kwargs) -> Incomplete: ...
def flash_size(*args, **kwargs) -> Incomplete: ...
