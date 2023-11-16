"""
Module: 'struct' on micropython-v1.21.0-esp32-Generic_ESP32_module_with_SPIRAM_with_ESP32
"""
# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'cpu': 'SPIRAM', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.14.0
from _typeshed import Incomplete as Incomplete, Incomplete
from typing import Tuple


def pack_into(fmt, buffer, offset, v1, *args, **kwargs) -> Incomplete:
    """
    Pack the values *v1*, *v2*, ... according to the format string *fmt*
    into a *buffer* starting at *offset*. *offset* may be negative to count
    from the end of *buffer*.
    """


def unpack(fmt, data) -> Tuple:
    """
    Unpack from the *data* according to the format string *fmt*.
    The return value is a tuple of the unpacked values.
    """


def unpack_from(fmt, data, offset: int = ...) -> Tuple:
    """
    Unpack from the *data* starting at *offset* according to the format string
    *fmt*. *offset* may be negative to count from the end of *data*. The return
    value is a tuple of the unpacked values.
    """


def pack(fmt, v1, *args, **kwargs) -> bytes:
    """
    Pack the values *v1*, *v2*, ... according to the format string *fmt*.
    The return value is a bytes object encoding the values.
    """


def calcsize(fmt) -> int:
    """
    Return the number of bytes needed to store the given *fmt*.
    """
