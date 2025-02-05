"""
JSON encoding and decoding.

<<<<<<<< HEAD:stubs/micropython-v1_24_1-docstubs/json/__init__.pyi
MicroPython module: https://docs.micropython.org/en/v1.24.0/library/json.html
========
MicroPython module: https://docs.micropython.org/en/preview.0/library/json.html
>>>>>>>> reference/rp2:stubs/micropython-preview-docstubs/json/__init__.pyi

CPython module: :mod:`python:json` https://docs.python.org/3/library/json.html .

This modules allows to convert between Python objects and the JSON
data format.
"""

# source version: preview
# origin module:: repos/micropython/docs/library/json.rst
from __future__ import annotations
from _typeshed import Incomplete
from typing_extensions import TypeVar, TypeAlias, Awaitable

def dump(obj, stream, separators=None) -> Incomplete:
    """
    Serialise *obj* to a JSON string, writing it to the given *stream*.

    If specified, separators should be an ``(item_separator, key_separator)``
    tuple. The default is ``(', ', ': ')``. To get the most compact JSON
    representation, you should specify ``(',', ':')`` to eliminate whitespace.
    """
    ...

def dumps(obj, separators=None) -> str:
    """
    Return *obj* represented as a JSON string.

    The arguments have the same meaning as in `dump`.
    """
    ...

def load(stream) -> Incomplete:
    """
    Parse the given *stream*, interpreting it as a JSON string and
    deserialising the data to a Python object.  The resulting object is
    returned.

    Parsing continues until end-of-file is encountered.
    A :exc:`ValueError` is raised if the data in *stream* is not correctly formed.
    """
    ...

def loads(str) -> Incomplete:
    """
    Parse the JSON *str* and return an object.  Raises :exc:`ValueError` if the
    string is not correctly formed.
    """
    ...
