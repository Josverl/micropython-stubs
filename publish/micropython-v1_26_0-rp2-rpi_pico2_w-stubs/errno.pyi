"""
System error codes.

MicroPython module: https://docs.micropython.org/en/v1.26.0/library/errno.html

CPython module: :mod:`python:errno` https://docs.python.org/3/library/errno.html .

This module provides access to symbolic error codes for `OSError` exception.
A particular inventory of codes depends on :term:`MicroPython port`.

---
Module: 'errno' on micropython-v1.26.0-rp2-RPI_PICO2_W
"""

# MCU: {'mpy': 'v6.3', 'build': '', 'ver': '1.26.0', 'arch': 'armv7emsp', 'version': '1.26.0', 'port': 'rp2', 'board': 'RPI_PICO2_W', 'family': 'micropython', 'board_id': 'RPI_PICO2_W', 'variant': '', 'cpu': 'RP2350'}
# Stubber: v1.25.1
from __future__ import annotations
from typing import Dict, Final
from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar

ENOBUFS: Final[int] = 105
ENODEV: Final[int] = 19
ENOENT: Final[int] = 2
EISDIR: Final[int] = 21
EIO: Final[int] = 5
EINVAL: Final[int] = 22
EPERM: Final[int] = 1
ETIMEDOUT: Final[int] = 110
ENOMEM: Final[int] = 12
EOPNOTSUPP: Final[int] = 95
ENOTCONN: Final[int] = 107
errorcode: dict = {}
EAGAIN: Final[int] = 11
EALREADY: Final[int] = 114
EBADF: Final[int] = 9
EADDRINUSE: Final[int] = 98
EACCES: Final[int] = 13
EINPROGRESS: Final[int] = 115
EEXIST: Final[int] = 17
EHOSTUNREACH: Final[int] = 113
ECONNABORTED: Final[int] = 103
ECONNRESET: Final[int] = 104
ECONNREFUSED: Final[int] = 111
ENOTSUP: Final[int] = ...
