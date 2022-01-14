"""
Module: 'builtins' on micropython-v1.10-esp32
"""
# MCU: {'ver': 'v1.10', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module with ESP32', 'release': '1.10.0', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.10.0'}
# Stubber: 1.5.0
from typing import Any


class ArithmeticError(Exception):
    """"""


class AssertionError(Exception):
    """"""


class AttributeError(Exception):
    """"""


class EOFError(Exception):
    """"""


Ellipsis: Any  ## <class ''> = Ellipsis


class Exception:
    """"""


class GeneratorExit:
    """"""


class ImportError(Exception):
    """"""


class IndentationError(Exception):
    """"""


class IndexError(Exception):
    """"""


class KeyError(Exception):
    """"""


class KeyboardInterrupt:
    """"""


class LookupError(Exception):
    """"""


class MemoryError(Exception):
    """"""


class NameError(Exception):
    """"""


NotImplemented: Any  ## <class ''> = NotImplemented


class NotImplementedError(Exception):
    """"""


class OSError(Exception):
    """"""


class OverflowError(Exception):
    """"""


class RuntimeError(Exception):
    """"""


class StopAsyncIteration:
    """"""


class StopIteration:
    """"""


class SyntaxError(Exception):
    """"""


class SystemExit:
    """"""


class TypeError(Exception):
    """"""


class UnicodeError(Exception):
    """"""


class ValueError(Exception):
    """"""


class ZeroDivisionError(Exception):
    """"""


def abs(*args) -> Any:
    ...


def all(*args) -> Any:
    ...


def any(*args) -> Any:
    ...


def bin(*args) -> Any:
    ...


class bool:
    """"""


class bytearray:
    """"""

    def append(self, *args) -> Any:
        ...

    def extend(self, *args) -> Any:
        ...


class bytes:
    """"""

    def center(self, *args) -> Any:
        ...

    def count(self, *args) -> Any:
        ...

    def decode(self, *args) -> Any:
        ...

    def endswith(self, *args) -> Any:
        ...

    def find(self, *args) -> Any:
        ...

    def format(self, *args) -> Any:
        ...

    def index(self, *args) -> Any:
        ...

    def isalpha(self, *args) -> Any:
        ...

    def isdigit(self, *args) -> Any:
        ...

    def islower(self, *args) -> Any:
        ...

    def isspace(self, *args) -> Any:
        ...

    def isupper(self, *args) -> Any:
        ...

    def join(self, *args) -> Any:
        ...

    def lower(self, *args) -> Any:
        ...

    def lstrip(self, *args) -> Any:
        ...

    def partition(self, *args) -> Any:
        ...

    def replace(self, *args) -> Any:
        ...

    def rfind(self, *args) -> Any:
        ...

    def rindex(self, *args) -> Any:
        ...

    def rpartition(self, *args) -> Any:
        ...

    def rsplit(self, *args) -> Any:
        ...

    def rstrip(self, *args) -> Any:
        ...

    def split(self, *args) -> Any:
        ...

    def splitlines(self, *args) -> Any:
        ...

    def startswith(self, *args) -> Any:
        ...

    def strip(self, *args) -> Any:
        ...

    def upper(self, *args) -> Any:
        ...


def callable(*args) -> Any:
    ...


def chr(*args) -> Any:
    ...


def compile(*args) -> Any:
    ...


class complex:
    """"""


def delattr(*args) -> Any:
    ...


class dict:
    """"""

    def clear(self, *args) -> Any:
        ...

    def copy(self, *args) -> Any:
        ...

    @classmethod
    def fromkeys(cls, *args) -> Any:
        ...

    def get(self, *args) -> Any:
        ...

    def items(self, *args) -> Any:
        ...

    def keys(self, *args) -> Any:
        ...

    def pop(self, *args) -> Any:
        ...

    def popitem(self, *args) -> Any:
        ...

    def setdefault(self, *args) -> Any:
        ...

    def update(self, *args) -> Any:
        ...

    def values(self, *args) -> Any:
        ...


def dir(*args) -> Any:
    ...


def divmod(*args) -> Any:
    ...


class enumerate:
    """"""


def eval(*args) -> Any:
    ...


def exec(*args) -> Any:
    ...


def execfile(*args) -> Any:
    ...


class filter:
    """"""


class float:
    """"""


class frozenset:
    """"""

    def copy(self, *args) -> Any:
        ...

    def difference(self, *args) -> Any:
        ...

    def intersection(self, *args) -> Any:
        ...

    def isdisjoint(self, *args) -> Any:
        ...

    def issubset(self, *args) -> Any:
        ...

    def issuperset(self, *args) -> Any:
        ...

    def symmetric_difference(self, *args) -> Any:
        ...

    def union(self, *args) -> Any:
        ...


def getattr(*args) -> Any:
    ...


def globals(*args) -> Any:
    ...


def hasattr(*args) -> Any:
    ...


def hash(*args) -> Any:
    ...


def help(*args) -> Any:
    ...


def hex(*args) -> Any:
    ...


def id(*args) -> Any:
    ...


def input(*args) -> Any:
    ...


class int:
    """"""

    @classmethod
    def from_bytes(cls, *args) -> Any:
        ...

    def to_bytes(self, *args) -> Any:
        ...


def isinstance(*args) -> Any:
    ...


def issubclass(*args) -> Any:
    ...


def iter(*args) -> Any:
    ...


def len(*args) -> Any:
    ...


class list:
    """"""

    def append(self, *args) -> Any:
        ...

    def clear(self, *args) -> Any:
        ...

    def copy(self, *args) -> Any:
        ...

    def count(self, *args) -> Any:
        ...

    def extend(self, *args) -> Any:
        ...

    def index(self, *args) -> Any:
        ...

    def insert(self, *args) -> Any:
        ...

    def pop(self, *args) -> Any:
        ...

    def remove(self, *args) -> Any:
        ...

    def reverse(self, *args) -> Any:
        ...

    def sort(self, *args) -> Any:
        ...


def locals(*args) -> Any:
    ...


class map:
    """"""


def max(*args) -> Any:
    ...


class memoryview:
    """"""


def min(*args) -> Any:
    ...


def next(*args) -> Any:
    ...


class object:
    """"""

    def __init__(self, *args) -> None:
        ...


def oct(*args) -> Any:
    ...


def open(*args) -> Any:
    ...


def ord(*args) -> Any:
    ...


def pow(*args) -> Any:
    ...


def print(*args) -> Any:
    ...


class property:
    """"""

    def deleter(self, *args) -> Any:
        ...

    def getter(self, *args) -> Any:
        ...

    def setter(self, *args) -> Any:
        ...


class range:
    """"""


def repr(*args) -> Any:
    ...


class reversed:
    """"""


def round(*args) -> Any:
    ...


class set:
    """"""

    def add(self, *args) -> Any:
        ...

    def clear(self, *args) -> Any:
        ...

    def copy(self, *args) -> Any:
        ...

    def difference(self, *args) -> Any:
        ...

    def difference_update(self, *args) -> Any:
        ...

    def discard(self, *args) -> Any:
        ...

    def intersection(self, *args) -> Any:
        ...

    def intersection_update(self, *args) -> Any:
        ...

    def isdisjoint(self, *args) -> Any:
        ...

    def issubset(self, *args) -> Any:
        ...

    def issuperset(self, *args) -> Any:
        ...

    def pop(self, *args) -> Any:
        ...

    def remove(self, *args) -> Any:
        ...

    def symmetric_difference(self, *args) -> Any:
        ...

    def symmetric_difference_update(self, *args) -> Any:
        ...

    def union(self, *args) -> Any:
        ...

    def update(self, *args) -> Any:
        ...


def setattr(*args) -> Any:
    ...


class slice:
    """"""


def sorted(*args) -> Any:
    ...


class str:
    """"""

    def center(self, *args) -> Any:
        ...

    def count(self, *args) -> Any:
        ...

    def encode(self, *args) -> Any:
        ...

    def endswith(self, *args) -> Any:
        ...

    def find(self, *args) -> Any:
        ...

    def format(self, *args) -> Any:
        ...

    def index(self, *args) -> Any:
        ...

    def isalpha(self, *args) -> Any:
        ...

    def isdigit(self, *args) -> Any:
        ...

    def islower(self, *args) -> Any:
        ...

    def isspace(self, *args) -> Any:
        ...

    def isupper(self, *args) -> Any:
        ...

    def join(self, *args) -> Any:
        ...

    def lower(self, *args) -> Any:
        ...

    def lstrip(self, *args) -> Any:
        ...

    def partition(self, *args) -> Any:
        ...

    def replace(self, *args) -> Any:
        ...

    def rfind(self, *args) -> Any:
        ...

    def rindex(self, *args) -> Any:
        ...

    def rpartition(self, *args) -> Any:
        ...

    def rsplit(self, *args) -> Any:
        ...

    def rstrip(self, *args) -> Any:
        ...

    def split(self, *args) -> Any:
        ...

    def splitlines(self, *args) -> Any:
        ...

    def startswith(self, *args) -> Any:
        ...

    def strip(self, *args) -> Any:
        ...

    def upper(self, *args) -> Any:
        ...


def sum(*args) -> Any:
    ...


class super:
    """"""


class tuple:
    """"""

    def count(self, *args) -> Any:
        ...

    def index(self, *args) -> Any:
        ...


class type:
    """"""


class zip:
    """"""
