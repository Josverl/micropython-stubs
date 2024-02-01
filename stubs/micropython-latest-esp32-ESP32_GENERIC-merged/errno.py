"""
System error codes.

MicroPython module: https://docs.micropython.org/en/latest/library/errno.html

CPython module: :mod:`python:errno` https://docs.python.org/3/library/errno.html .

This module provides access to symbolic error codes for `OSError` exception.
A particular inventory of codes depends on :term:`MicroPython port`.

---
Module: 'errno' on micropython-v1.21.0-esp32-Generic_ESP32_module_with_SPIRAM_with_ESP32
"""
# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'cpu': 'SPIRAM', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.14.0
from _typeshed import Incomplete
from typing import Dict

ENOBUFS = 105  # type: int
ENODEV = 19  # type: int
ENOENT = 2  # type: int
EISDIR = 21  # type: int
EIO = 5  # type: int
EINVAL = 22  # type: int
EPERM = 1  # type: int
ETIMEDOUT = 116  # type: int
ENOMEM = 12  # type: int
EOPNOTSUPP = 95  # type: int
ENOTCONN = 128  # type: int
errorcode = {}  # type: dict
EAGAIN = 11  # type: int
EALREADY = 120  # type: int
EBADF = 9  # type: int
EADDRINUSE = 112  # type: int
EACCES = 13  # type: int
EINPROGRESS = 119  # type: int
EEXIST = 17  # type: int
EHOSTUNREACH = 118  # type: int
ECONNABORTED = 113  # type: int
ECONNRESET = 104  # type: int
ECONNREFUSED = 111  # type: int
