"""
JSON encoding and decoding.

MicroPython module: https://docs.micropython.org/en/v1.24.0/library/json.html

CPython module: :mod:`python:json` https://docs.python.org/3/library/json.html .

This modules allows to convert between Python objects and the JSON
data format.

---
Module: 'json' on micropython-v1.24.1-rp2-RPI_PICO_W
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'rp2', 'board': 'RPI_PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.3', 'arch': 'armv6m'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete
from _mpy_shed import IOBase_mp
from typing import Any, AnyStr, Tuple, overload
from typing_extensions import Awaitable, TypeAlias, TypeVar

def loads(str: AnyStr) -> Any:
    """
    Parse the JSON *str* and return an object.  Raises :exc:`ValueError` if the
    string is not correctly formed.
    """
    ...

def load(stream: IOBase_mp | Incomplete) -> Any:
    """
    Parse the given *stream*, interpreting it as a JSON string and
    deserialising the data to a Python object.  The resulting object is
    returned.

    Parsing continues until end-of-file is encountered.
    A :exc:`ValueError` is raised if the data in *stream* is not correctly formed.
    """
    ...

@overload
def dumps(obj: Any) -> str:
    """
    Return *obj* represented as a JSON string.

    The arguments have the same meaning as in `dump`.
    """
    ...

@overload
def dumps(obj: Any, separators: Tuple[str, str]) -> str:
    """
    Return *obj* represented as a JSON string.

    The arguments have the same meaning as in `dump`.
    """
    ...

@overload
def dump(obj: Any, stream: IOBase_mp | Incomplete, /) -> None:
    """
    Serialise *obj* to a JSON string, writing it to the given *stream*.

    If specified, separators should be an ``(item_separator, key_separator)``
    tuple. The default is ``(', ', ': ')``. To get the most compact JSON
    representation, you should specify ``(',', ':')`` to eliminate whitespace.
    """
    ...

@overload
def dump(obj: Any, stream: IOBase_mp | Incomplete, separators: Tuple[str, str], /) -> None:
    """
    Serialise *obj* to a JSON string, writing it to the given *stream*.

    If specified, separators should be an ``(item_separator, key_separator)``
    tuple. The default is ``(', ', ': ')``. To get the most compact JSON
    representation, you should specify ``(',', ':')`` to eliminate whitespace.
    """
    ...
