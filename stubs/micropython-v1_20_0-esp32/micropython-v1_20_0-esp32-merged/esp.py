"""
Functions related to the ESP8266 and ESP32.

MicroPython module: https://docs.micropython.org/en/v1.20.0/library/esp.html

The ``esp`` module contains specific functions related to both the ESP8266 and
ESP32 modules.  Some functions are only available on one or the other of these
ports.
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'esp32', 'board': 'GENERIC', 'cpu': 'ESP32', 'mpy': 'v6.1', 'arch': 'xtensawin'})
# Stubber: v1.13.4
from typing import Optional, Any
from _typeshed import Incomplete

LOG_NONE = 0  # type: int
LOG_WARNING = 2  # type: int
LOG_VERBOSE = 5  # type: int
LOG_DEBUG = 4  # type: int
LOG_INFO = 3  # type: int
LOG_ERROR = 1  # type: int


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


def flash_write(byte_offset, bytes) -> Incomplete:
    ...


def gpio_matrix_in(*args, **kwargs) -> Any:
    ...


def gpio_matrix_out(*args, **kwargs) -> Any:
    ...


def flash_user_start() -> Incomplete:
    """
    Read the memory offset at which the user flash space begins.
    """
    ...


def flash_erase(sector_no) -> Incomplete:
    ...


def flash_read(byte_offset, length_or_buffer) -> Incomplete:
    ...


def flash_size() -> Incomplete:
    """
    Read the total size of the flash memory.
    """
    ...
