"""
System error codes.

MicroPython module: https://docs.micropython.org/en/v1.19.1/library/errno.html

CPython module: :mod:`python:errno` https://docs.python.org/3/library/errno.html .

This module provides access to symbolic error codes for `OSError` exception.
A particular inventory of codes depends on :term:`MicroPython port`.
"""

from _typeshed import Incomplete
from typing import Dict

EACCES: int
EADDRINUSE: int
EAGAIN: int
EALREADY: int
EBADF: int
ECONNABORTED: int
ECONNREFUSED: int
ECONNRESET: int
EEXIST: int
EHOSTUNREACH: int
EINPROGRESS: int
EINVAL: int
EIO: int
EISDIR: int
ENOBUFS: int
ENODEV: int
ENOENT: int
ENOMEM: int
ENOTCONN: int
EOPNOTSUPP: int
EPERM: int
ETIMEDOUT: int
errorcode: dict
