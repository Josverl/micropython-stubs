"""
Binary/ASCII conversions.

MicroPython module: https://docs.micropython.org/en/v1.25.0/library/binascii.html

CPython module: :mod:`python:binascii` https://docs.python.org/3/library/binascii.html .

This module implements conversions between binary data and various
encodings of it in ASCII form (in both directions).

---
Module: 'binascii' on micropython-v1.25.0-esp32-ESP32_GENERIC_C6
"""

# MCU: {'version': '1.25.0', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC_C6', 'family': 'micropython', 'build': '', 'arch': 'rv32imc', 'ver': '1.25.0', 'cpu': 'ESP32C6'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete
from typing import Any, Optional
from typing_extensions import Awaitable, TypeAlias, TypeVar

def crc32(data, value: Optional[Any] = None) -> Incomplete:
    """
    Compute CRC-32, the 32-bit checksum of *data*, starting with an initial CRC
    of *value*. The default initial CRC is zero. The algorithm is consistent
    with the ZIP file checksum.
    """
    ...

def hexlify(data, sep: Optional[Any] = None) -> bytes:
    """
    Convert the bytes in the *data* object to a hexadecimal representation.
    Returns a bytes object.

    If the additional argument *sep* is supplied it is used as a separator
    between hexadecimal values.
    """
    ...

def unhexlify(data) -> bytes:
    """
    Convert hexadecimal data to binary representation. Returns bytes string.
    (i.e. inverse of hexlify)
    """
    ...

def b2a_base64(data, *, newline=True) -> bytes:
    """
    Encode binary data in base64 format, as in `RFC 3548
    <https://tools.ietf.org/html/rfc3548.html>`_. Returns the encoded data
    followed by a newline character if newline is true, as a bytes object.
    """
    ...

def a2b_base64(data) -> bytes:
    """
    Decode base64-encoded data, ignoring invalid characters in the input.
    Conforms to `RFC 2045 s.6.8 <https://tools.ietf.org/html/rfc2045#section-6.8>`_.
    Returns a bytes object.
    """
    ...
