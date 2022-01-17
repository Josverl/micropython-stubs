""" """

from typing import Any


class bool:
    def __init__(self) -> None:
        ...


class bytearray:
    def __init__(self) -> None:
        ...


class bytes:
    """
    |see_cpython| `python:bytes`.
    """

    def __init__(self) -> None:
        ...


class complex:
    def __init__(self) -> None:
        ...


class dict:
    def __init__(self) -> None:
        ...


class float:
    def __init__(self) -> None:
        ...


class frozenset:
    def __init__(self) -> None:
        ...


class int:
    def __init__(self) -> None:
        ...

    @classmethod
    def from_bytes(cls, bytes, byteorder) -> Any:
        """
        In MicroPython, `byteorder` parameter must be positional (this is
        compatible with CPython).
        """
        ...

    def to_bytes(self, size, byteorder) -> Any:
        """
        In MicroPython, `byteorder` parameter must be positional (this is
        compatible with CPython).
        """
        ...


class list:
    def __init__(self) -> None:
        ...


class memoryview:
    def __init__(self) -> None:
        ...


class object:
    def __init__(self) -> None:
        ...


class set:
    def __init__(self) -> None:
        ...


class slice:
    """
    The *slice* builtin is the type that slice objects have.
    """

    def __init__(self) -> None:
        ...


class str:
    def __init__(self) -> None:
        ...


class tuple:
    def __init__(self) -> None:
        ...


class AssertionError(Exception):
    ...


class AttributeError(Exception):
    ...


class ImportError(Exception):
    ...


class IndexError(Exception):
    ...


class KeyboardInterrupt(Exception):
    ...


class KeyError(Exception):
    ...


class MemoryError(Exception):
    ...


class NameError(Exception):
    ...


class NotImplementedError(Exception):
    ...


class OSError(Exception):
    ...


class RuntimeError(Exception):
    ...


class StopIteration(Exception):
    ...


class SyntaxError(Exception):
    ...


class SystemExit(Exception):
    ...


class TypeError(Exception):
    ...


class ValueError(Exception):
    ...


class ZeroDivisionError(Exception):
    ...


def abs() -> Any:
    ...


def all() -> Any:
    ...


def any() -> Any:
    ...


def bin() -> Any:
    ...


def callable() -> Any:
    ...


def chr() -> Any:
    ...


def compile() -> Any:
    ...


def delattr(obj, name) -> Any:
    """
    The argument *name* should be a string, and this function deletes the named
    attribute from the object given by *obj*.
    """
    ...


def dir() -> Any:
    ...


def divmod() -> Any:
    ...


def enumerate() -> Any:
    ...


def eval() -> Any:
    ...


def exec() -> Any:
    ...


def filter() -> Any:
    ...


def getattr() -> Any:
    ...


def globals() -> Any:
    ...


def hasattr() -> Any:
    ...


def hash() -> Any:
    ...


def hex() -> Any:
    ...


def id() -> Any:
    ...


def input() -> Any:
    ...


def isinstance() -> Any:
    ...


def issubclass() -> Any:
    ...


def iter() -> Any:
    ...


def len() -> Any:
    ...


def locals() -> Any:
    ...


def map() -> Any:
    ...


def max() -> Any:
    ...


def min() -> Any:
    ...


def next() -> Any:
    ...


def oct() -> Any:
    ...


def open() -> Any:
    ...


def ord() -> Any:
    ...


def pow() -> Any:
    ...


def print() -> Any:
    ...


def property() -> Any:
    ...


def range() -> Any:
    ...


def repr() -> Any:
    ...


def reversed() -> Any:
    ...


def round() -> Any:
    ...


def setattr() -> Any:
    ...


def sorted() -> Any:
    ...


def sum() -> Any:
    ...


def super() -> Any:
    ...


def type() -> Any:
    ...


def zip() -> Any:
    ...
