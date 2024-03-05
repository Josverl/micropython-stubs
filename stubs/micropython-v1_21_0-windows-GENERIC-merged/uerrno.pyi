"""
System error codes.

MicroPython module: https://docs.micropython.org/en/v1.21.0/library/errno.html

CPython module: :mod:`python:errno` https://docs.python.org/3/library/errno.html .

This module provides access to symbolic error codes for `OSError` exception.
A particular inventory of codes depends on :term:`MicroPython port`.
"""
from _typeshed import Incomplete, Incomplete as Incomplete
from typing import Dict

ENOBUFS: int
ENODEV: int
ENOENT: int
EISDIR: int
EIO: int
EINVAL: int
EPERM: int
ETIMEDOUT: int
ENOMEM: int
EOPNOTSUPP: int
ENOTCONN: int
errorcode: dict
EAGAIN: int
EALREADY: int
EBADF: int
EADDRINUSE: int
EACCES: int
EINPROGRESS: int
EEXIST: int
EHOSTUNREACH: int
ECONNABORTED: int
ECONNRESET: int
ECONNREFUSED: int
