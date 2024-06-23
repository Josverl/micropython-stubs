"""
Pack and unpack primitive data types.

MicroPython module: https://docs.micropython.org/en/v1.24.0-preview/library/struct.html

CPython module: :mod:`python:struct` https://docs.python.org/3/library/struct.html .

The following byte orders are supported:

+-----------+------------------------+----------+-----------+
| Character | Byte order             | Size     | Alignment |
+===========+========================+==========+===========+
| @         | native                 | native   | native    |
+-----------+------------------------+----------+-----------+
| <         | little-endian          | standard | none      |
+-----------+------------------------+----------+-----------+
| >         | big-endian             | standard | none      |
+-----------+------------------------+----------+-----------+
| !         | network (= big-endian) | standard | none      |
+-----------+------------------------+----------+-----------+

The following data types are supported:

+--------+--------------------+-------------------+---------------+
| Format | C Type             | Python type       | Standard size |
+========+====================+===================+===============+
| b      | signed char        | integer           | 1             |
+--------+--------------------+-------------------+---------------+
| B      | unsigned char      | integer           | 1             |
+--------+--------------------+-------------------+---------------+
| h      | short              | integer           | 2             |
+--------+--------------------+-------------------+---------------+
| H      | unsigned short     | integer           | 2             |
+--------+--------------------+-------------------+---------------+
| i      | int                | integer (`1<fn>`) | 4             |
+--------+--------------------+-------------------+---------------+
| I      | unsigned int       | integer (`1<fn>`) | 4             |
+--------+--------------------+-------------------+---------------+
| l      | long               | integer (`1<fn>`) | 4             |
+--------+--------------------+-------------------+---------------+
| L      | unsigned long      | integer (`1<fn>`) | 4             |
+--------+--------------------+-------------------+---------------+
| q      | long long          | integer (`1<fn>`) | 8             |
+--------+--------------------+-------------------+---------------+
| Q      | unsigned long long | integer (`1<fn>`) | 8             |
+--------+--------------------+-------------------+---------------+
| e      | n/a (half-float)   | float (`2<fn>`)   | 2             |
+--------+--------------------+-------------------+---------------+
| f      | float              | float (`2<fn>`)   | 4             |
+--------+--------------------+-------------------+---------------+
| d      | double             | float (`2<fn>`)   | 8             |
+--------+--------------------+-------------------+---------------+
| s      | char[]             | bytes             |               |
+--------+--------------------+-------------------+---------------+
| P      | void *             | integer           |               |
+--------+--------------------+-------------------+---------------+

---
Module: 'ustruct' on micropython-v1.24.0-preview-esp32-ESP32_GENERIC_S3
"""

# MCU: {'version': '1.24.0-preview', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'family': 'micropython', 'build': 'preview.60.gcebc9b0ae', 'arch': 'xtensawin', 'ver': '1.24.0-preview-preview.60.gcebc9b0ae', 'cpu': 'ESP32S3'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete
from typing import Tuple

def pack_into(fmt, buffer, offset, v1, *args, **kwargs) -> Incomplete:
    """
    Pack the values *v1*, *v2*, ... according to the format string *fmt*
    into a *buffer* starting at *offset*. *offset* may be negative to count
    from the end of *buffer*.
    """
    ...

def unpack(fmt, data) -> Tuple:
    """
    Unpack from the *data* according to the format string *fmt*.
    The return value is a tuple of the unpacked values.
    """
    ...

def unpack_from(
    fmt,
    data,
    offset=0,
) -> Tuple:
    """
    Unpack from the *data* starting at *offset* according to the format string
    *fmt*. *offset* may be negative to count from the end of *data*. The return
    value is a tuple of the unpacked values.
    """
    ...

def pack(fmt, v1, *args, **kwargs) -> bytes:
    """
    Pack the values *v1*, *v2*, ... according to the format string *fmt*.
    The return value is a bytes object encoding the values.
    """
    ...

def calcsize(fmt) -> int:
    """
    Return the number of bytes needed to store the given *fmt*.
    """
    ...
