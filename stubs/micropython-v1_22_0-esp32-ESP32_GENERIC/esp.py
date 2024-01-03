"""
Module: 'esp' on micropython-v1.22.0-esp32-ESP32_GENERIC
"""
# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'cpu': 'ESP32', 'mpy': 'v6.2', 'arch': 'xtensawin'}
# Stubber: v1.16.2
from _typeshed import Incomplete

LOG_NONE = 0  # type: int
LOG_WARNING = 2  # type: int
LOG_VERBOSE = 5  # type: int
LOG_DEBUG = 4  # type: int
LOG_INFO = 3  # type: int
LOG_ERROR = 1  # type: int


def osdebug(*args, **kwargs) -> Incomplete:
    ...


def flash_write(*args, **kwargs) -> Incomplete:
    ...


def gpio_matrix_in(*args, **kwargs) -> Incomplete:
    ...


def gpio_matrix_out(*args, **kwargs) -> Incomplete:
    ...


def flash_user_start(*args, **kwargs) -> Incomplete:
    ...


def flash_erase(*args, **kwargs) -> Incomplete:
    ...


def flash_read(*args, **kwargs) -> Incomplete:
    ...


def flash_size(*args, **kwargs) -> Incomplete:
    ...
