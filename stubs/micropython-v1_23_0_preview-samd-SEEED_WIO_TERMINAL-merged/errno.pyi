"""
System error codes.

MicroPython module: https://docs.micropython.org/en/v1.23.0-preview/library/errno.html

CPython module: :mod:`python:errno` https://docs.python.org/3/library/errno.html .

This module provides access to symbolic error codes for `OSError` exception.
A particular inventory of codes depends on :term:`MicroPython port`.

---
Module: 'errno' on micropython-v1.23.0-preview-samd-SEEED_WIO_TERMINAL
"""
# MCU: {'version': '1.23.0-preview', 'mpy': 'v6.2', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'family': 'micropython', 'build': '203', 'arch': 'armv7emsp', 'ver': '1.23.0-preview-203', 'cpu': 'SAMD51P19A'}
# Stubber: v1.17.3
from __future__ import annotations
from _typeshed import Incomplete
from typing import Dict

ENOBUFS: int = 105
ENODEV: int = 19
ENOENT: int = 2
EISDIR: int = 21
EIO: int = 5
EINVAL: int = 22
EPERM: int = 1
ETIMEDOUT: int = 110
ENOMEM: int = 12
EOPNOTSUPP: int = 95
ENOTCONN: int = 107
errorcode: dict = {}
EAGAIN: int = 11
EALREADY: int = 114
EBADF: int = 9
EADDRINUSE: int = 98
EACCES: int = 13
EINPROGRESS: int = 115
EEXIST: int = 17
EHOSTUNREACH: int = 113
ECONNABORTED: int = 103
ECONNRESET: int = 104
ECONNREFUSED: int = 111
