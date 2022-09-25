"""
hashing algorithms. See: https://docs.micropython.org/en/v1.19.1/library/hashlib.html

|see_cpython_module| :mod:`python:hashlib` https://docs.python.org/3/library/hashlib.html .

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
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.5.6
from typing import Callable, Coroutine, Dict, Generator, IO, Iterator, List, NoReturn, Optional, Tuple, Union, Any


class sha1:
    """
    Create an SHA1 hasher object and optionally feed ``data`` into it.
    """

    def __init__(self, data: Optional[Any] = None) -> None:
        """"""
        ...

    def update(self, *args, **kwargs) -> Any:
        ...

    def digest(self, *args, **kwargs) -> Any:
        ...


class sha256:
    """
    Create an SHA256 hasher object and optionally feed ``data`` into it.
    """

    def __init__(self, data: Optional[Any] = None) -> None:
        """"""
        ...

    def update(self, *args, **kwargs) -> Any:
        ...

    def digest(self, *args, **kwargs) -> Any:
        ...
