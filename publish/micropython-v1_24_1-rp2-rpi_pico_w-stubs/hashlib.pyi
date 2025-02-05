"""
Hashing algorithms.

MicroPython module: https://docs.micropython.org/en/v1.24.0/library/hashlib.html

CPython module: :mod:`python:hashlib` https://docs.python.org/3/library/hashlib.html .

This module implements binary data hashing algorithms. The exact inventory
of available algorithms depends on a board. Among the algorithms which may
be implemented:

* SHA256 - The current generation, modern hashing algorithm (of SHA2 series).
  It is suitable for cryptographically-secure purposes. Included in the
  MicroPython core and any board is recommended to provide this, unless
  it has particular code size constraints.

* SHA1 - A previous generation algorithm. Not recommended for new usages,
  but SHA1 is a part of number of Internet standards and existing
  applications, so boards targeting network connectivity and
  interoperability will try to provide this.

* MD5 - A legacy algorithm, not considered cryptographically secure. Only
  selected boards, targeting interoperability with legacy applications,
  will offer this.

---
Module: 'hashlib' on micropython-v1.24.1-rp2-RPI_PICO_W
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'rp2', 'board': 'RPI_PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.3', 'arch': 'armv6m'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete
from _mpy_shed import AnyReadableBuf, AnyWritableBuf, _Hash
from typing import overload
from typing_extensions import Awaitable, TypeAlias, TypeVar

class sha256(_Hash):
    """
    The current generation, modern hashing algorithm (of SHA2 series).
    It is suitable for cryptographically-secure purposes. Included in the
    MicroPython core and any board is recommended to provide this, unless
    it has particular code size constraints.
    """

    def digest(self, *args, **kwargs) -> Incomplete: ...
    def update(self, *args, **kwargs) -> Incomplete: ...
    @overload
    def __init__(self):
        """
        Create an SHA256 hasher object and optionally feed ``data`` into it.
        """

    @overload
    def __init__(self, data: AnyReadableBuf):
        """
        Create an SHA256 hasher object and optionally feed ``data`` into it.
        """

    @overload
    def __init__(self):
        """
        Create an SHA256 hasher object and optionally feed ``data`` into it.
        """

    @overload
    def __init__(self, data: AnyReadableBuf):
        """
        Create an SHA256 hasher object and optionally feed ``data`` into it.
        """

class sha1(_Hash):
    """
    A previous generation algorithm. Not recommended for new usages,
    but SHA1 is a part of number of Internet standards and existing
    applications, so boards targeting network connectivity and
    interoperability will try to provide this.
    """

    def digest(self, *args, **kwargs) -> Incomplete: ...
    def update(self, *args, **kwargs) -> Incomplete: ...
    @overload
    def __init__(self):
        """
        Create an SHA1 hasher object and optionally feed ``data`` into it.
        """

    @overload
    def __init__(self, data: AnyReadableBuf):
        """
        Create an SHA1 hasher object and optionally feed ``data`` into it.
        """

    @overload
    def __init__(self):
        """
        Create an SHA1 hasher object and optionally feed ``data`` into it.
        """

    @overload
    def __init__(self, data: AnyReadableBuf):
        """
        Create an SHA1 hasher object and optionally feed ``data`` into it.
        """
