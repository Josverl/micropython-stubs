"""
Module: 'esp' on micropython-v1.20.0-449-esp32-Generic_ESP32_module_with_SPIRAM_with_ESP32
"""
# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'family': 'micropython', 'build': '449', 'arch': 'xtensawin', 'ver': 'v1.20.0-449', 'cpu': 'SPIRAM'})
# Stubber: v1.13.7
from typing import Any

LOG_NONE = 0  # type: int
LOG_WARNING = 2  # type: int
LOG_VERBOSE = 5  # type: int
LOG_DEBUG = 4  # type: int
LOG_INFO = 3  # type: int
LOG_ERROR = 1  # type: int


def osdebug(*args, **kwargs) -> Any:
    ...


def flash_write(*args, **kwargs) -> Any:
    ...


def gpio_matrix_in(*args, **kwargs) -> Any:
    ...


def gpio_matrix_out(*args, **kwargs) -> Any:
    ...


def flash_user_start(*args, **kwargs) -> Any:
    ...


def flash_erase(*args, **kwargs) -> Any:
    ...


def flash_read(*args, **kwargs) -> Any:
    ...


def flash_size(*args, **kwargs) -> Any:
    ...
