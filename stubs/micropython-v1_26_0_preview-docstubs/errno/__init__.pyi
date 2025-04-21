"""
System error codes.

MicroPython module: https://docs.micropython.org/en/v1.26.0/library/errno.html

CPython module: :mod:`python:errno` https://docs.python.org/3/library/errno.html .

This module provides access to symbolic error codes for `OSError` exception.
A particular inventory of codes depends on :term:`MicroPython port`.
"""

# source version: v1.26.0-preview
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
ENOENT: Final[int] = 2
EIO: Final[int] = 5
EBADF: Final[int] = 9
ENOMEM: Final[int] = 12
EACCES: Final[int] = 13
ENODEV: Final[int] = 19
EISDIR: Final[int] = 21
EINVAL: Final[int] = 22
EOPNOTSUPP: Final[int] = 95
EADDRINUSE: Final[int] = 98
ECONNABORTED: Final[int] = 103
ECONNRESET: Final[int] = 104
ENOBUFS: Final[int] = 105
ENOTCONN: Final[int] = 107
ETIMEDOUT: Final[int] = 110
ECONNREFUSED: Final[int] = 111
EHOSTUNREACH: Final[int] = 113
EALREADY: Final[int] = 114
EINPROGRESS: Final[int] = 115
ENOTSUP: Final[int] = ...
