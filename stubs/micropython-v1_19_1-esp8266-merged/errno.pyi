"""
system error codes. See: https://docs.micropython.org/en/v1.19.1/library/errno.html

|see_cpython_module| :mod:`python:errno` https://docs.python.org/3/library/errno.html .

This module provides access to symbolic error codes for `OSError` exception.
A particular inventory of codes depends on :term:`MicroPython port`.
"""
from typing import Any, Dict

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
