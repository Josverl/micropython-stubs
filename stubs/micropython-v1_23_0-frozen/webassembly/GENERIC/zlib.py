# MicroPython zlib module
# MIT license; Copyright (c) 2023 Jim Mussared

"""
Zlib compression & decompression.

MicroPython module: https://docs.micropython.org/en/v1.23.0/library/zlib.html

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
from __future__ import annotations
import io, deflate
from _typeshed import Incomplete

_MAX_WBITS = 15


def _decode_wbits(wbits, decompress):
    if -15 <= wbits <= -5:
        return (
            deflate.RAW,
            -wbits,
        )
    elif 5 <= wbits <= 15:
        return (deflate.ZLIB, wbits)
    elif decompress and wbits == 0:
        return (deflate.ZLIB,)
    elif 21 <= wbits <= 31:
        return (deflate.GZIP, wbits - 16)
    elif decompress and 35 <= wbits <= 47:
        return (deflate.AUTO, wbits - 32)
    else:
        raise ValueError("wbits")


if hasattr(deflate.DeflateIO, "write"):

    def compress(data, wbits=_MAX_WBITS) -> Incomplete:
        """
        Compresses *data* into a bytes object.

        *wbits* allows you to configure the DEFLATE dictionary window size and the
        output format. The window size allows you to trade-off memory usage for
        compression level. A larger window size will allow the compressor to
        reference fragments further back in the input. The output formats are "raw"
        DEFLATE (no header/footer), zlib, and gzip, where the latter two
        include a header and checksum.

        The low four bits of the absolute value of *wbits* set the base-2 logarithm of
        the DEFLATE dictionary window size. So for example, ``wbits=10``,
        ``wbits=-10``, and ``wbits=26`` all set the window size to 1024 bytes. Valid
        window sizes are ``5`` to ``15`` inclusive (corresponding to 32 to 32k bytes).

        Negative values of *wbits* between ``-5`` and ``-15`` correspond to "raw"
        output mode, positive values between ``5`` and ``15`` correspond to zlib
        output mode, and positive values between ``21`` and ``31`` correspond to
        gzip output mode.

        See the :mod:`CPython documentation for zlib <python:zlib>` for more
        information about the *wbits* parameter. Note that MicroPython allows
        for smaller window sizes, which is useful when memory is constrained while
        still achieving a reasonable level of compression. It also speeds up
        the compressor. See more :ref:`MicroPython-specific details <deflate_wbits>`
        in the :mod:`deflate <deflate>` module documentation.
        """
        f = io.BytesIO()
        with deflate.DeflateIO(f, *_decode_wbits(wbits, False)) as g:
            g.write(data)
        return f.getvalue()


def decompress(data, wbits=_MAX_WBITS) -> Incomplete:
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
    f = io.BytesIO(data)
    with deflate.DeflateIO(f, *_decode_wbits(wbits, True)) as g:
        return g.read()
