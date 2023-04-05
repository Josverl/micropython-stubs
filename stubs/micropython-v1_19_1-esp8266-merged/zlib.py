"""
zlib decompression. See: https://docs.micropython.org/en/v1.19.1/library/zlib.html

|see_cpython_module| :mod:`python:zlib` https://docs.python.org/3/library/zlib.html .

This module allows to decompress binary data compressed with
`DEFLATE algorithm <https://en.wikipedia.org/wiki/DEFLATE>`_
(commonly used in zlib library and gzip archiver). Compression
is not yet implemented.
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp8266', 'port': 'esp8266', 'machine': 'ESP module (1M) with ESP8266', 'release': '1.19.1', 'nodename': 'esp8266', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp8266', 'version': '1.19.1'}
# Stubber: 1.9.11
from typing import IO, Any


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


class DecompIO(IO):
    """
    Create a `stream` wrapper which allows transparent decompression of
    compressed data in another *stream*. This allows to process compressed
    streams with data larger than available heap size. In addition to
    values described in :func:`decompress`, *wbits* may take values
    24..31 (16 + 8..15), meaning that input stream has gzip header.
    """

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def readline(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, stream, wbits=0, /) -> None:
        ...
