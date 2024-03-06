"""
System error codes.

MicroPython module: https://docs.micropython.org/en/v1.21.0/library/errno.html

CPython module: :mod:`python:errno` https://docs.python.org/3/library/errno.html .

This module provides access to symbolic error codes for `OSError` exception.
A particular inventory of codes depends on :term:`MicroPython port`.

---
Module: 'errno' on micropython-v1.21.0-win32-GENERIC
"""
# MCU: {'version': '1.21.0', 'mpy': '', 'port': 'win32', 'board': 'GENERIC', 'family': 'micropython', 'build': '', 'arch': '', 'ver': 'v1.21.0', 'cpu': ''}
# Stubber: v1.15.0
from typing import Dict, Any
from _typeshed import Incomplete

ENOBUFS = 119  # type: int
ENODEV = 19  # type: int
ENOENT = 2  # type: int
EISDIR = 21  # type: int
EIO = 5  # type: int
EINVAL = 22  # type: int
EPERM = 1  # type: int
ETIMEDOUT = 138  # type: int
ENOMEM = 12  # type: int
EOPNOTSUPP = 130  # type: int
ENOTCONN = 126  # type: int
errorcode = {}  # type: dict
EAGAIN = 11  # type: int
EALREADY = 103  # type: int
EBADF = 9  # type: int
EADDRINUSE = 100  # type: int
EACCES = 13  # type: int
EINPROGRESS = 112  # type: int
EEXIST = 17  # type: int
EHOSTUNREACH = 110  # type: int
ECONNABORTED = 106  # type: int
ECONNRESET = 108  # type: int
ECONNREFUSED = 107  # type: int
