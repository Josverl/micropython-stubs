"""
Gzip compression & decompression.

MicroPython module: https://docs.micropython.org/en/v1.23.0/library/gzip.html

|see_cpython_module| :mod:`python:gzip`.

This module allows compression and decompression of binary data with the
`DEFLATE algorithm <https://en.wikipedia.org/wiki/DEFLATE>`_ used by the gzip
file format.

.. note:: Prefer to use :class:`deflate.DeflateIO` instead of the functions in this
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

# source version: v1.23.0
# origin module:: repos/micropython/docs/library/gzip.rst
from __future__ import annotations
from _typeshed import Incomplete

class GzipFile:
    """
    This class can be used to wrap a *fileobj* which is any
    :term:`stream-like <stream>` object such as a file, socket, or stream
    (including :class:`io.BytesIO`). It is itself a stream and implements the
    standard read/readinto/write/close methods.

    When the *mode* argument is ``"rb"``, reads from the GzipFile instance will
    decompress the data in the underlying stream and return decompressed data.

    If compression support is enabled then the *mode* argument can be set to
    ``"wb"``, and writes to the GzipFile instance will be compressed and written
    to the underlying stream.

    By default the GzipFile class will read and write data using the gzip file
    format, including a header and footer with checksum and a window size of 512
    bytes.

    The **file**, **compresslevel**, and **mtime** arguments are not
    supported. **fileobj** and **mode** must always be specified as keyword
    arguments.
    """

    def __init__(self, *, fileobj, mode) -> None: ...

def open(
    filename,
    mode,
) -> Incomplete:
    """
    Wrapper around built-in :func:`open` returning a GzipFile instance.
    """
    ...

def decompress(
    data,
) -> Incomplete:
    """
    Decompresses *data* into a bytes object.
    """
    ...

def compress(
    data,
) -> Incomplete:
    """
    Compresses *data* into a bytes object.
    """
    ...
