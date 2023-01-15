"""
functions related to the ESP8266 and ESP32. See: https://docs.micropython.org/en/v1.17/library/esp.html

The ``esp`` module contains specific functions related to both the ESP8266 and
ESP32 modules.  Some functions are only available on one or the other of these
ports.

"""
from typing import Optional, Any

LOG_DEBUG: int
LOG_ERROR: int
LOG_INFO: int
LOG_NONE: int
LOG_VERBOSE: int
LOG_WARNING: int

def dht_readinto(*args, **kwargs) -> Any: ...
def flash_erase(sector_no) -> Any: ...
def flash_read(byte_offset, length_or_buffer) -> Any: ...
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

def flash_write(byte_offset, bytes) -> Any: ...
def gpio_matrix_in(*args, **kwargs) -> Any: ...
def gpio_matrix_out(*args, **kwargs) -> Any: ...
def osdebug(*args, **kwargs) -> Any: ...
