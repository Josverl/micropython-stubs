"""
functions related to the ESP8266 and ESP32. See: https://docs.micropython.org/en/v1.19.1/library/esp.html

The ``esp`` module contains specific functions related to both the ESP8266 and
ESP32 modules.  Some functions are only available on one or the other of these
ports.

"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.5.6
from typing import Callable, Coroutine, Dict, Generator, IO, Iterator, List, NoReturn, Optional, Tuple, Union, Any

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


def osdebug(level) -> None:
    """
    Turn esp os debugging messages on or off.

    The *level* parameter sets the threshold for the log messages for all esp components.
    The log levels are defined as constants:

        * ``LOG_NONE`` -- No log output
        * ``LOG_ERROR`` -- Critical errors, software module can not recover on its own
        * ``LOG_WARN`` -- Error conditions from which recovery measures have been taken
        * ``LOG_INFO`` -- Information messages which describe normal flow of events
        * ``LOG_DEBUG`` -- Extra information which is not necessary for normal use (values, pointers, sizes, etc)
        * ``LOG_VERBOSE`` -- Bigger chunks of debugging information, or frequent messages
          which can potentially flood the output
    """
    ...
