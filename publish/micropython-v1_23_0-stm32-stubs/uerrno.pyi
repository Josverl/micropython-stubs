"""
System error codes.

MicroPython module: https://docs.micropython.org/en/v1.23.0/library/errno.html

CPython module: :mod:`python:errno` https://docs.python.org/3/library/errno.html .

This module provides access to symbolic error codes for `OSError` exception.
A particular inventory of codes depends on :term:`MicroPython port`.

---
Module: 'uerrno' on micropython-v1.23.0-stm32-PYBV11
"""

# MCU: {'version': '1.23.0', 'mpy': 'v6.3', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': '', 'arch': 'armv7emsp', 'ver': '1.23.0', 'cpu': 'STM32F405RG'}
# Stubber: v1.23.0
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
