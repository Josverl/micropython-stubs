"""
System error codes.

MicroPython module: https://docs.micropython.org/en/v1.26.0/library/errno.html

CPython module: :mod:`python:errno` https://docs.python.org/3/library/errno.html .

This module provides access to symbolic error codes for `OSError` exception.
A particular inventory of codes depends on :term:`MicroPython port`.

---
Module: 'errno' on micropython-v1.26.1-windows-standard
"""

# MCU: {'family': 'micropython', 'version': '1.26.1', 'build': '', 'ver': '1.26.1', 'port': 'windows', 'board': 'standard', 'board_id': 'standard', 'variant': '', 'cpu': 'win32 [GCC 12.0.0] version', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.26.2
from __future__ import annotations
from typing import Dict, Any, Final, Generator
from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar

ENOBUFS: Final[int] = 119
"""No buffer space available"""
ENODEV: Final[int] = 19
"""No such device"""
ENOENT: Final[int] = 2
"""No such file or directory"""
EISDIR: Final[int] = 21
"""Is a directory"""
EIO: Final[int] = 5
"""I/O error"""
EINVAL: Final[int] = 22
"""Invalid argument"""
EPERM: Final[int] = 1
"""Operation not permitted"""
ETIMEDOUT: Final[int] = 138
"""Connection timed out"""
ENOMEM: Final[int] = 12
"""Out of memory"""
EOPNOTSUPP: Final[int] = 130
"""Operation not supported"""
ENOTCONN: Final[int] = 126
"""Transport endpoint is not connected"""
errorcode: dict = {}
"""\
Dictionary mapping numeric error codes to strings with symbolic error
code (see above)::

>>> print(errno.errorcode[errno.EEXIST])
EEXIST
"""
EAGAIN: Final[int] = 11
"""\
Error codes, based on ANSI C/POSIX standard. All error codes start with
"E". As mentioned above, inventory of the codes depends on
:term:`MicroPython port`. Errors are usually accessible as ``exc.errno``
where ``exc`` is an instance of `OSError`. Usage example::

try:
os.mkdir("my_dir")
except OSError as exc:
if exc.errno == errno.EEXIST:
print("Directory already exists")
"""
EALREADY: Final[int] = 103
"""Operation already in progress"""
EBADF: Final[int] = 9
"""Bad file descriptor"""
EADDRINUSE: Final[int] = 100
"""Address already in use"""
EACCES: Final[int] = 13
"""Permission denied"""
EINPROGRESS: Final[int] = 112
"""Operation now in progress"""
EEXIST: Final[int] = 17
"""\
Error codes, based on ANSI C/POSIX standard. All error codes start with
"E". As mentioned above, inventory of the codes depends on
:term:`MicroPython port`. Errors are usually accessible as ``exc.errno``
where ``exc`` is an instance of `OSError`. Usage example::

try:
os.mkdir("my_dir")
except OSError as exc:
if exc.errno == errno.EEXIST:
print("Directory already exists")
"""
EHOSTUNREACH: Final[int] = 110
"""Host is unreachable"""
ECONNABORTED: Final[int] = 106
"""Connection aborted"""
ECONNRESET: Final[int] = 108
"""Connection reset by peer"""
ECONNREFUSED: Final[int] = 107
"""Connection refused"""
ENOTSUP: Final[int] = ...
"""Operation not supported"""
