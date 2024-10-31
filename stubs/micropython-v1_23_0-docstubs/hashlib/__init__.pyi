"""
Hashing algorithms.

MicroPython module: https://docs.micropython.org/en/v1.23.0/library/hashlib.html

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
"""

# source version: v1.23.0
# origin module:: repos/micropython/docs/library/hashlib.rst
from __future__ import annotations
from typing import Any, Optional
from _typeshed import Incomplete

class sha256:
    """
    Create an SHA256 hasher object and optionally feed ``data`` into it.
    """

    def __init__(self, data: Optional[Any] = None) -> None: ...

class sha1:
    """
    Create an SHA1 hasher object and optionally feed ``data`` into it.
    """

    def __init__(self, data: Optional[Any] = None) -> None: ...

class md5:
    """
    Create an MD5 hasher object and optionally feed ``data`` into it.
    """

    def __init__(self, data: Optional[Any] = None) -> None: ...

class hash:
    """ """

    def update(self, data) -> Incomplete:
        """
        Feed more binary data into hash.
        """
        ...

    def digest(self) -> bytes:
        """
        Return hash for all data passed through hash, as a bytes object. After this
        method is called, more data cannot be fed into the hash any longer.
        """
        ...

    def hexdigest(self) -> Incomplete:
        """
        This method is NOT implemented. Use ``binascii.hexlify(hash.digest())``
        to achieve a similar effect.
        """
        ...
