"""
Binary/ASCII conversions.

MicroPython module: https://docs.micropython.org/en/v1.25.0/library/binascii.html

CPython module: :mod:`python:binascii` https://docs.python.org/3/library/binascii.html .

This module implements conversions between binary data and various
encodings of it in ASCII form (in both directions).

---
Module: 'binascii' on micropython-v1.25.0-esp8266-ESP8266_GENERIC
"""

# MCU: {'version': '1.25.0', 'mpy': 'v6.3', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensa', 'ver': '1.25.0', 'cpu': 'ESP8266'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Optional, Any, Final, Generator
from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar

def unhexlify(data: str | bytes, /) -> bytes:
    """
    Convert hexadecimal data to binary representation. Returns bytes string.
    (i.e. inverse of hexlify)
    """
    ...

def hexlify(data: bytes, sep: str | bytes = ..., /) -> bytes:
    """
    Convert the bytes in the *data* object to a hexadecimal representation.
    Returns a bytes object.

    If the additional argument *sep* is supplied it is used as a separator
    between hexadecimal values.
    """
    ...

def b2a_base64(data: bytes, /) -> bytes:
    """
    Encode binary data in base64 format, as in `RFC 3548
    <https://tools.ietf.org/html/rfc3548.html>`_. Returns the encoded data
    followed by a newline character if newline is true, as a bytes object.
    """
    ...

def a2b_base64(data: str | bytes, /) -> bytes:
    """
    Decode base64-encoded data, ignoring invalid characters in the input.
    Conforms to `RFC 2045 s.6.8 <https://tools.ietf.org/html/rfc2045#section-6.8>`_.
    Returns a bytes object.
    """
    ...
