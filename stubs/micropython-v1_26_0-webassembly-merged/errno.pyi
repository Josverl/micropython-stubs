"""
System error codes.

MicroPython module: https://docs.micropython.org/en/v1.26.0/library/errno.html

CPython module: :mod:`python:errno` https://docs.python.org/3/library/errno.html .

This module provides access to symbolic error codes for `OSError` exception.
A particular inventory of codes depends on :term:`MicroPython port`.

---
Module: 'errno' on micropython-v1.26.0-preview-webassembly-pyscript
"""

# MCU: {'family': 'micropython', 'version': '1.26.0-preview', 'build': '293', 'ver': '1.26.0-preview-293', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.26.2
from __future__ import annotations
from typing import Dict, Any, Final, Generator
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
EALREADY: Final[int] = 114
EBADF: Final[int] = 9
EADDRINUSE: Final[int] = 98
EACCES: Final[int] = 13
EINPROGRESS: Final[int] = 115
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
EHOSTUNREACH: Final[int] = 113
ECONNABORTED: Final[int] = 103
ECONNRESET: Final[int] = 104
ECONNREFUSED: Final[int] = 111
ENOTSUP: Final[int] = ...
