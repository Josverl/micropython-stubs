"""
JSON encoding and decoding. See: https://docs.micropython.org/en/v1.18/library/json.html

|see_cpython_module| :mod:`python:json` https://docs.python.org/3/library/json.html .

This modules allows to convert between Python objects and the JSON
data format.
"""
# MCU: {'family': 'micropython', 'sysname': 'rp2', 'version': '1.18.0', 'build': '', 'mpy': 5637, 'port': 'rp2', 'platform': 'rp2', 'name': 'micropython', 'arch': 'armv7m', 'machine': 'Arduino Nano RP2040 Connect with RP2040', 'nodename': 'rp2', 'ver': 'v1.18', 'release': '1.18.0'}
# Stubber: 1.5.3
from typing import Any


def dump(obj, stream, separators=None) -> Any:
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


def load(stream) -> Any:
    """
    Parse the given *stream*, interpreting it as a JSON string and
    deserialising the data to a Python object.  The resulting object is
    returned.

    Parsing continues until end-of-file is encountered.
    A :exc:`ValueError` is raised if the data in *stream* is not correctly formed.
    """
    ...


def loads(str) -> Any:
    """
    Parse the JSON *str* and return an object.  Raises :exc:`ValueError` if the
    string is not correctly formed.
    """
    ...
