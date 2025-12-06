"""
Binary/ASCII conversions.

MicroPython module: https://docs.micropython.org/en/v1.26.0/library/binascii.html

CPython module: :mod:`python:binascii` https://docs.python.org/3/library/binascii.html .

This module implements conversions between binary data and various
encodings of it in ASCII form (in both directions).
"""

from __future__ import annotations
from ubinascii import *
from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar

def unhexlify(data) -> bytes:
    """
    Convert hexadecimal data to binary representation. Returns bytes string.
    (i.e. inverse of hexlify)
    """
    ...

b2a_hex = hexlify
a2b_hex = unhexlify
PAD: str
table_a2b_base64: Incomplete

def _transform(n): ...
def a2b_base64(ascii) -> bytes:
    """
    Decode base64-encoded data, ignoring invalid characters in the input.
    Conforms to `RFC 2045 s.6.8 <https://tools.ietf.org/html/rfc2045#section-6.8>`_.
    Returns a bytes object.
    """

table_b2a_base64: str

def b2a_base64(bin, newline: bool = True) -> bytes:
    """
    Encode binary data in base64 format, as in `RFC 3548
    <https://tools.ietf.org/html/rfc3548.html>`_. Returns the encoded data
    followed by a newline character if newline is true, as a bytes object.
    """
