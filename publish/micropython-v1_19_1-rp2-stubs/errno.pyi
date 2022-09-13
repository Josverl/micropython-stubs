"""
system error codes. See: https://docs.micropython.org/en/v1.19.1/library/errno.html

|see_cpython_module| :mod:`python:errno` https://docs.python.org/3/library/errno.html .

This module provides access to symbolic error codes for `OSError` exception.
A particular inventory of codes depends on :term:`MicroPython port`.
"""
from typing import Any, Callable, Coroutine, Dict, Generator, IO, Iterator, List, NoReturn, Optional, Tuple, Union

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
