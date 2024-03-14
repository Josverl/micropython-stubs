"""
JSON encoding and decoding.

MicroPython module: https://docs.micropython.org/en/v1.23.0-preview/library/json.html

CPython module: :mod:`python:json` https://docs.python.org/3/library/json.html .

This modules allows to convert between Python objects and the JSON
data format.

---
Module: 'ujson' on micropython-v1.23.0-preview-rp2-RPI_PICO
"""
# MCU: {'build': 'preview.205.g2b6f81f2b', 'ver': '1.23.0-preview-preview.205.g2b6f81f2b', 'version': '1.23.0-preview', 'port': 'rp2', 'board': 'RPI_PICO', 'mpy': 'v6.2', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.17.3
from __future__ import annotations
from _typeshed import Incomplete

def loads(str) -> Incomplete:
    """
    Parse the JSON *str* and return an object.  Raises :exc:`ValueError` if the
    string is not correctly formed.
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

def dumps(obj, separators=None) -> str:
    """
    Return *obj* represented as a JSON string.

    The arguments have the same meaning as in `dump`.
    """
    ...

def dump(obj, stream, separators=None) -> Incomplete:
    """
    Serialise *obj* to a JSON string, writing it to the given *stream*.

    If specified, separators should be an ``(item_separator, key_separator)``
    tuple. The default is ``(', ', ': ')``. To get the most compact JSON
    representation, you should specify ``(',', ':')`` to eliminate whitespace.
    """
    ...
