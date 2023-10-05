"""
Zlib compression & decompression.

MicroPython module: https://docs.micropython.org/en/latest/library/zlib.html

CPython module: :mod:`python:zlib` https://docs.python.org/3/library/zlib.html .

This module allows compression and decompression of binary data with the
`DEFLATE algorithm <https://en.wikipedia.org/wiki/DEFLATE>`_
(commonly used in the zlib library and gzip archiver).

``Note:`` Prefer to use :class:`deflate.DeflateIO` instead of the functions in this
   module as it provides a streaming interface to compression and decompression
   which is convenient and more memory efficient when working with reading or
   writing compressed data to a file, socket, or stream.

**Availability:**

* From MicroPython v1.21 onwards, this module may not be present by default on
  all MicroPython firmware as it duplicates functionality available in
  the :mod:`deflate <deflate>` module.

* A copy of this module can be installed (or frozen)
  from :term:`micropython-lib` (`source <https://github.com/micropython/micropython-lib/blob/master/python-stdlib/zlib/zlib.py>`_).
  See :ref:`packages` for more information. This documentation describes that module.

* Requires the built-in :mod:`deflate <deflate>` module (available since MicroPython v1.21)

* Compression support will only be available if compression support is enabled
  in the built-in :mod:`deflate <deflate>` module.
"""
# MCU: OrderedDict({'build': '', 'ver': 'v1.20.0', 'version': '1.20.0', 'port': 'samd', 'board': 'ADAFRUIT_ITSYBITSY_M4_EXPRESS', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'SAMD51G19A', 'arch': 'armv7emsp'})
# Stubber: v1.13.7
from typing import Any
from _typeshed import Incomplete


def decompress(data, wbits=15, /) -> Incomplete:
    """
    Decompresses *data* into a bytes object.

    The *wbits* parameter works the same way as for :meth:`zlib.compress`
    with the following additional valid values:

    * ``0``: Automatically determine the window size from the zlib header
      (*data* must be in zlib format).
    * ``35`` to ``47``: Auto-detect either the zlib or gzip format.

    As for :meth:`zlib.compress`, see the :mod:`CPython documentation for zlib <python:zlib>`
    for more information about the *wbits* parameter. As for :meth:`zlib.compress`,
    MicroPython also supports smaller window sizes than CPython. See more
    :ref:`MicroPython-specific details <deflate_wbits>` in the
    :mod:`deflate <deflate>` module documentation.

    If the data to be decompressed requires a larger window size, it will
    fail during decompression.
    """
    ...


class DecompIO:
    def readinto(self, *args, **kwargs) -> Any:
        ...

    def readline(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
