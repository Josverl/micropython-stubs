"""
System error codes.

MicroPython module: https://docs.micropython.org/en/v1.25.0/library/errno.html

CPython module: :mod:`python:errno` https://docs.python.org/3/library/errno.html .

This module provides access to symbolic error codes for `OSError` exception.
A particular inventory of codes depends on :term:`MicroPython port`.
"""

# source version: v1.25.0
# origin module:: repos/micropython/docs/library/errno.rst
from __future__ import annotations
from _typeshed import Incomplete
from typing import Final, Dict
from typing_extensions import TypeVar, TypeAlias, Awaitable
EEXIST: Incomplete
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
EAGAIN: Incomplete
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
errorcode: Dict
"""\
Dictionary mapping numeric error codes to strings with symbolic error
code (see above)::

>>> print(errno.errorcode[errno.EEXIST])
EEXIST
"""
EPERM: Final[int] = 1
"""Operation not permitted"""
ENOENT: Final[int] = 2
"""No such file or directory"""
EIO: Final[int] = 5
"""I/O error"""
EBADF: Final[int] = 9
"""Bad file descriptor"""
ENOMEM: Final[int] = 12
"""Out of memory"""
EACCES: Final[int] = 13
"""Permission denied"""
ENODEV: Final[int] = 19
"""No such device"""
EISDIR: Final[int] = 21
"""Is a directory"""
EINVAL: Final[int] = 22
"""Invalid argument"""
EOPNOTSUPP: Final[int] = 95
"""Operation not supported"""
EADDRINUSE: Final[int] = 98
"""Address already in use"""
ECONNABORTED: Final[int] = 103
"""Connection aborted"""
ECONNRESET: Final[int] = 104
"""Connection reset by peer"""
ENOBUFS: Final[int] = 105
"""No buffer space available"""
ENOTCONN: Final[int] = 107
"""Transport endpoint is not connected"""
ETIMEDOUT: Final[int] = 110
"""Connection timed out"""
ECONNREFUSED: Final[int] = 111
"""Connection refused"""
EHOSTUNREACH: Final[int] = 113
"""Host is unreachable"""
EALREADY: Final[int] = 114
"""Operation already in progress"""
EINPROGRESS: Final[int] = 115
"""Operation now in progress"""
ENOTSUP : Final[int] = ...
"""Operation not supported"""
