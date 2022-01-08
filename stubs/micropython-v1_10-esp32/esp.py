"""
Module: 'esp' on micropython-v1.10-esp32
"""
# MCU: {'ver': 'v1.10', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module with ESP32', 'release': '1.10.0', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.10.0'}
# Stubber: 1.5.0
from typing import Any

LOG_DEBUG = 4  # type: int
LOG_ERROR = 1  # type: int
LOG_INFO = 3  # type: int
LOG_NONE = 0  # type: int
LOG_VERBOSE = 5  # type: int
LOG_WARNING = 2  # type: int


def dht_readinto(*args) -> Any:
    ...


def flash_erase(*args) -> Any:
    ...


def flash_read(*args) -> Any:
    ...


def flash_size(*args) -> Any:
    ...


def flash_user_start(*args) -> Any:
    ...


def flash_write(*args) -> Any:
    ...


def gpio_matrix_in(*args) -> Any:
    ...


def gpio_matrix_out(*args) -> Any:
    ...


def neopixel_write(*args) -> Any:
    ...


def osdebug(*args) -> Any:
    ...
