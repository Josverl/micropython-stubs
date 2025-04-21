"""
Convert Python objects to and from a binary format.

MicroPython module: https://docs.micropython.org/en/v1.26.0/library/marshal.html

CPython module: :mod:`python:marshal` https://docs.python.org/3/library/marshal.html .

This module implements conversion between Python objects and a binary format.
The format is specific to MicroPython but does not depend on the machine
architecture, so the data can be transferred and used on a different MicroPython
instance, as long as the version of the binary data matches (it's currently
versioned as the mpy file version, see :ref:`mpy_files`).
"""

# source version: v1.26.0-preview
# origin module:: repos/micropython/docs/library/marshal.rst
from __future__ import annotations
from _typeshed import Incomplete
from typing_extensions import TypeVar, TypeAlias, Awaitable

def dumps(value, /) -> Incomplete:
    """
    Convert the given *value* to binary format and return a corresponding ``bytes``
    object.

    Currently, code objects are the only supported values that can be converted.
    """
    ...

def loads(data, /) -> Incomplete:
    """
    Convert the given bytes-like *data* to its corresponding Python object, and
    return it.
    """
    ...
