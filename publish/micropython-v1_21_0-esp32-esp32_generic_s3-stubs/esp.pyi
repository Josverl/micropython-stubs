"""
Functions related to the ESP8266 and ESP32.

MicroPython module: https://docs.micropython.org/en/v1.21.0/library/esp.html

The ``esp`` module contains specific functions related to both the ESP8266 and
ESP32 modules.  Some functions are only available on one or the other of these
ports.

---
Module: 'esp' on micropython-v1.21.0-esp32-ESP32_GENERIC_S3
"""

# MCU: {'version': '1.21.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': '1.21.0', 'cpu': 'ESP32S3'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete
from typing import Any, Optional

LOG_NONE: int = 0
LOG_WARNING: int = 2
LOG_VERBOSE: int = 5
LOG_DEBUG: int = 4
LOG_INFO: int = 3
LOG_ERROR: int = 1

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

def flash_write(byte_offset, bytes) -> Incomplete: ...
def gpio_matrix_in(*args, **kwargs) -> Incomplete: ...
def gpio_matrix_out(*args, **kwargs) -> Incomplete: ...
def flash_user_start() -> Incomplete:
    """
    Read the memory offset at which the user flash space begins.
    """
    ...

def flash_erase(sector_no) -> Incomplete: ...
def flash_read(byte_offset, length_or_buffer) -> Incomplete: ...
def flash_size() -> Incomplete:
    """
    Read the total size of the flash memory.
    """
    ...
