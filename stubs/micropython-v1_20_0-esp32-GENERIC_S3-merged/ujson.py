"""
JSON encoding and decoding.

MicroPython module: https://docs.micropython.org/en/v1.20.0/library/json.html

CPython module: :mod:`python:json` https://docs.python.org/3/library/json.html .

This modules allows to convert between Python objects and the JSON
data format.

---
Module: 'ujson' on micropython-v1.20.0-esp32-GENERIC_S3
"""
# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'GENERIC_S3', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': 'v1.20.0', 'cpu': 'ESP32S3'})
# Stubber: v1.13.7
from typing import Any
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
