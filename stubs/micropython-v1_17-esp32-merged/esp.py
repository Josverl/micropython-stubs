"""
functions related to the ESP8266 and ESP32. See: https://docs.micropython.org/en/v1.17/library/esp.html

The ``esp`` module contains specific functions related to both the ESP8266 and
ESP32 modules.  Some functions are only available on one or the other of these
ports.

"""
# MCU: {'ver': 'v1.17', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.17.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.17.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.4
from typing import Optional, Any

LOG_DEBUG = 4  # type: int
LOG_ERROR = 1  # type: int
LOG_INFO = 3  # type: int
LOG_NONE = 0  # type: int
LOG_VERBOSE = 5  # type: int
LOG_WARNING = 2  # type: int


def dht_readinto(*args, **kwargs) -> Any:
    ...


def flash_erase(sector_no) -> Any:
    ...


def flash_read(byte_offset, length_or_buffer) -> Any:
    ...


def flash_size() -> Any:
    """
    Read the total size of the flash memory.
    """
    ...


def flash_user_start() -> Any:
    """
    Read the memory offset at which the user flash space begins.
    """
    ...


def flash_write(byte_offset, bytes) -> Any:
    ...


def gpio_matrix_in(*args, **kwargs) -> Any:
    ...


def gpio_matrix_out(*args, **kwargs) -> Any:
    ...


def osdebug(*args, **kwargs) -> Any:
    ...
