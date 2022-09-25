"""
system error codes. See: https://docs.micropython.org/en/v1.19.1/library/errno.html

|see_cpython_module| :mod:`python:errno` https://docs.python.org/3/library/errno.html .

This module provides access to symbolic error codes for `OSError` exception.
A particular inventory of codes depends on :term:`MicroPython port`.
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.5.6
from typing import Callable, Coroutine, Dict, Generator, IO, Iterator, List, NoReturn, Optional, Tuple, Union, Any

EACCES = 13  # type: int
EADDRINUSE = 112  # type: int
EAGAIN = 11  # type: int
EALREADY = 120  # type: int
EBADF = 9  # type: int
ECONNABORTED = 113  # type: int
ECONNREFUSED = 111  # type: int
ECONNRESET = 104  # type: int
EEXIST = 17  # type: int
EHOSTUNREACH = 118  # type: int
EINPROGRESS = 119  # type: int
EINVAL = 22  # type: int
EIO = 5  # type: int
EISDIR = 21  # type: int
ENOBUFS = 105  # type: int
ENODEV = 19  # type: int
ENOENT = 2  # type: int
ENOMEM = 12  # type: int
ENOTCONN = 128  # type: int
EOPNOTSUPP = 95  # type: int
EPERM = 1  # type: int
ETIMEDOUT = 116  # type: int
errorcode = {}  # type: dict
