"""
Gzip compression & decompression.

MicroPython module: https://docs.micropython.org/en/v1.29.0/library/gzip.html

CPython module: :mod:`python:gzip` https://docs.python.org/3/library/gzip.html .

This module allows compression and decompression of binary data with the
`DEFLATE algorithm <https://en.wikipedia.org/wiki/DEFLATE>`_ used by the gzip
file format.

``Note:`` Prefer to use :class:`deflate.DeflateIO` instead of the functions in this
   module as it provides a streaming interface to compression and decompression
   which is convenient and more memory efficient when working with reading or
   writing compressed data to a file, socket, or stream.

**Availability:**

* This module is **not present by default** in official MicroPython firmware
  releases as it duplicates functionality available in the :mod:`deflate
  <deflate>` module.

* A copy of this module can be installed (or frozen)
  from :term:`micropython-lib` (`source <https://github.com/micropython/micropython-lib/blob/master/python-stdlib/gzip/gzip.py>`_).
  See :ref:`packages` for more information. This documentation describes that module.

* Compression support will only be available if compression support is enabled
  in the built-in :mod:`deflate <deflate>` module.
"""

# source version: v1.29.0-preview
# origin module:: repos/micropython/docs/library/gzip.rst
from __future__ import annotations
from _typeshed import Incomplete
from typing_extensions import TypeVar, TypeAlias, Awaitable
class GzipFile():
    """
  Wrap a stream-like object with gzip decompression/compression support.
  """
    def __init__(self, *, fileobj, mode) -> None:
        ...
def open(filename, mode: str = "rb", /) -> Incomplete:
    """
       Wrapper around built-in :func:`open` returning a GzipFile instance.
    """
    ...
def decompress(data: bytes, /) -> bytes:
    """
       Decompresses *data* into a bytes object.
    """
    ...
def compress(data: bytes, /) -> bytes:
    """
       Compresses *data* into a bytes object.
    """
    ...
