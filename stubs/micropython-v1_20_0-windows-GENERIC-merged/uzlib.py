"""
Zlib decompression.

MicroPython module: https://docs.micropython.org/en/v1.20.0/library/zlib.html

CPython module: :mod:`python:zlib` https://docs.python.org/3/library/zlib.html .

This module allows to decompress binary data compressed with
`DEFLATE algorithm <https://en.wikipedia.org/wiki/DEFLATE>`_
(commonly used in zlib library and gzip archiver). Compression
is not yet implemented.

---
Module: 'uzlib' on micropython-v1.20.0-win32-GENERIC
"""
# MCU: {'version': '1.20.0', 'mpy': '', 'port': 'win32', 'board': 'GENERIC', 'family': 'micropython', 'build': '', 'arch': '', 'ver': 'v1.20.0', 'cpu': ''}
# Stubber: v1.15.0
from typing import Any
from _typeshed import Incomplete


def decompress(data, wbits=0, bufsize=0, /) -> bytes:
    """
    Return decompressed *data* as bytes. *wbits* is DEFLATE dictionary window
    size used during compression (8-15, the dictionary size is power of 2 of
    that value). Additionally, if value is positive, *data* is assumed to be
    zlib stream (with zlib header). Otherwise, if it's negative, it's assumed
    to be raw DEFLATE stream. *bufsize* parameter is for compatibility with
    CPython and is ignored.
    """
    ...


class DecompIO:
    """
    Create a `stream` wrapper which allows transparent decompression of
    compressed data in another *stream*. This allows to process compressed
    streams with data larger than available heap size. In addition to
    values described in :func:`decompress`, *wbits* may take values
    24..31 (16 + 8..15), meaning that input stream has gzip header.

    Difference to CPython

       This class is MicroPython extension. It's included on provisional
       basis and may be changed considerably or removed in later versions.
    """

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def readline(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
