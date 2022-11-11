"""
binary/ASCII conversions. See: https://docs.micropython.org/en/v1.17/library/binascii.html

|see_cpython_module| :mod:`python:binascii` https://docs.python.org/3/library/binascii.html .

This module implements conversions between binary data and various
encodings of it in ASCII form (in both directions).
"""
# MCU: {'ver': 'v1.17', 'port': 'pyboard', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.17.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.17.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'pyboard', 'family': 'micropython'}
# Stubber: 1.5.4
from typing import Optional, Any


def a2b_base64(data) -> bytes:
    """
    Decode base64-encoded data, ignoring invalid characters in the input.
    Conforms to `RFC 2045 s.6.8 <https://tools.ietf.org/html/rfc2045#section-6.8>`_.
    Returns a bytes object.
    """
    ...


def b2a_base64(data) -> bytes:
    """
    Encode binary data in base64 format, as in `RFC 3548
    <https://tools.ietf.org/html/rfc3548.html>`_. Returns the encoded data
    followed by a newline character, as a bytes object.
    """
    ...


def crc32(*args, **kwargs) -> Any:
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
