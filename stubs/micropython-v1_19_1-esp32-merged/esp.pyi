"""
functions related to the ESP8266 and ESP32. See: https://docs.micropython.org/en/v1.19.1/library/esp.html

The ``esp`` module contains specific functions related to both the ESP8266 and
ESP32 modules.  Some functions are only available on one or the other of these
ports.

"""
from typing import Optional, Any

LOG_NONE: int
LOG_WARNING: int
LOG_VERBOSE: int
LOG_DEBUG: int
LOG_INFO: int
LOG_ERROR: int

def flash_user_start() -> Any:
    """
    Read the memory offset at which the user flash space begins.
    """
    ...

def flash_write(byte_offset, bytes) -> Any: ...
def gpio_matrix_in(*args, **kwargs) -> Any: ...
def gpio_matrix_out(*args, **kwargs) -> Any: ...
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

def flash_size() -> Any:
    """
    Read the total size of the flash memory.
    """
    ...

def dht_readinto(*args, **kwargs) -> Any: ...
def flash_erase(sector_no) -> Any: ...
def flash_read(byte_offset, length_or_buffer) -> Any: ...
