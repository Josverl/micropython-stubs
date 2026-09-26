"""
Module: 'builtins' on micropython-v1.29.0-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.29.0
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete

def eval(*args, **kwargs) -> Incomplete:
    ...

def dir(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=2
def divmod(*args, **kwargs) -> Incomplete:
    ...

def globals() -> Incomplete:
    ...

def exec(*args, **kwargs) -> Incomplete:
    ...

def getattr(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=2
def hasattr(*args, **kwargs) -> Incomplete:
    ...

def sum(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=3
def setattr(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def any(*args, **kwargs) -> Incomplete:
    ...

def sorted(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def callable(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def chr(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def all(*args, **kwargs) -> Incomplete:
    ...

def next(*args, **kwargs) -> Incomplete:
    ...

def locals() -> Incomplete:
    ...

# inspect: arity=1
def repr(*args, **kwargs) -> Incomplete:
    ...

def pow(*args, **kwargs) -> Incomplete:
    ...

def open(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def ord(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def hash(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=2
def isinstance(*args, **kwargs) -> Incomplete:
    ...

def round(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def id(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def len(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=2
def issubclass(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def iter(*args, **kwargs) -> Incomplete:
    ...

def print(*args, **kwargs) -> Incomplete:
    ...

def execfile(*args, **kwargs) -> Incomplete:
    ...

def help(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def abs(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=2
def delattr(*args, **kwargs) -> Incomplete:
    ...

def compile(*args, **kwargs) -> Incomplete:
    ...

def min(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def oct(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def hex(*args, **kwargs) -> Incomplete:
    ...

def max(*args, **kwargs) -> Incomplete:
    ...

def input(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def bin(*args, **kwargs) -> Incomplete:
    ...

Ellipsis: Incomplete ## <class ''> = Ellipsis
NotImplemented: Incomplete ## <class ''> = NotImplemented

class tuple():
    def index(self, *args, **kwargs) -> Incomplete:
        ...

    def count(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class memoryview():
    def hex(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class str():
    def rstrip(self, *args, **kwargs) -> Incomplete:
        ...

    def startswith(self, *args, **kwargs) -> Incomplete:
        ...

    def split(self, *args, **kwargs) -> Incomplete:
        ...

    def rfind(self, *args, **kwargs) -> Incomplete:
        ...

    def rsplit(self, *args, **kwargs) -> Incomplete:
        ...

    def rindex(self, *args, **kwargs) -> Incomplete:
        ...

    def replace(self, *args, **kwargs) -> Incomplete:
        ...

    def partition(self, *args, **kwargs) -> Incomplete:
        ...

    def strip(self, *args, **kwargs) -> Incomplete:
        ...

    def rpartition(self, *args, **kwargs) -> Incomplete:
        ...

    def upper(self, *args, **kwargs) -> Incomplete:
        ...

    def encode(self, *args, **kwargs) -> Incomplete:
        ...

    def center(self, *args, **kwargs) -> Incomplete:
        ...

    def splitlines(self, *args, **kwargs) -> Incomplete:
        ...

    def format(self, *args, **kwargs) -> Incomplete:
        ...

    def isalpha(self, *args, **kwargs) -> Incomplete:
        ...

    def index(self, *args, **kwargs) -> Incomplete:
        ...

    def count(self, *args, **kwargs) -> Incomplete:
        ...

    def find(self, *args, **kwargs) -> Incomplete:
        ...

    def endswith(self, *args, **kwargs) -> Incomplete:
        ...

    def lstrip(self, *args, **kwargs) -> Incomplete:
        ...

    def join(self, *args, **kwargs) -> Incomplete:
        ...

    def isdigit(self, *args, **kwargs) -> Incomplete:
        ...

    def lower(self, *args, **kwargs) -> Incomplete:
        ...

    def islower(self, *args, **kwargs) -> Incomplete:
        ...

    def isupper(self, *args, **kwargs) -> Incomplete:
        ...

    def isspace(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class range():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class reversed():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class property():
    def getter(self, *args, **kwargs) -> Incomplete:
        ...

    def setter(self, *args, **kwargs) -> Incomplete:
        ...

    def deleter(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class super():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class UnicodeError(Exception):
    ...

class filter():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class enumerate():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class StopAsyncIteration():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class complex():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class type():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class float():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class zip():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class frozenset():
    def union(self, *args, **kwargs) -> Incomplete:
        ...

    def issubset(self, *args, **kwargs) -> Incomplete:
        ...

    def issuperset(self, *args, **kwargs) -> Incomplete:
        ...

    def symmetric_difference(self, *args, **kwargs) -> Incomplete:
        ...

    def isdisjoint(self, *args, **kwargs) -> Incomplete:
        ...

    def copy(self, *args, **kwargs) -> Incomplete:
        ...

    def difference(self, *args, **kwargs) -> Incomplete:
        ...

    def intersection(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class set():
    def discard(self, *args, **kwargs) -> Incomplete:
        ...

    def isdisjoint(self, *args, **kwargs) -> Incomplete:
        ...

    def intersection_update(self, *args, **kwargs) -> Incomplete:
        ...

    def intersection(self, *args, **kwargs) -> Incomplete:
        ...

    def issubset(self, *args, **kwargs) -> Incomplete:
        ...

    def symmetric_difference_update(self, *args, **kwargs) -> Incomplete:
        ...

    def symmetric_difference(self, *args, **kwargs) -> Incomplete:
        ...

    def issuperset(self, *args, **kwargs) -> Incomplete:
        ...

    def union(self, *args, **kwargs) -> Incomplete:
        ...

    def difference_update(self, *args, **kwargs) -> Incomplete:
        ...

    def pop(self, *args, **kwargs) -> Incomplete:
        ...

    def copy(self, *args, **kwargs) -> Incomplete:
        ...

    def clear(self, *args, **kwargs) -> Incomplete:
        ...

    def remove(self, *args, **kwargs) -> Incomplete:
        ...

    def difference(self, *args, **kwargs) -> Incomplete:
        ...

    def add(self, *args, **kwargs) -> Incomplete:
        ...

    def update(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class slice():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class IndentationError(Exception):
    ...

class KeyboardInterrupt(Exception):
    ...

class KeyError(Exception):
    ...

class IndexError(Exception):
    ...

class LookupError(Exception):
    ...

class NotImplementedError(Exception):
    ...

class NameError(Exception):
    ...

class MemoryError(Exception):
    ...

class object():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ImportError(Exception):
    ...

class AttributeError(Exception):
    ...

class AssertionError(Exception):
    ...

class ArithmeticError(Exception):
    ...

class GeneratorExit():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class EOFError(Exception):
    ...

class bool():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class bytes():
    def split(self, *args, **kwargs) -> Incomplete:
        ...

    def rstrip(self, *args, **kwargs) -> Incomplete:
        ...

    def startswith(self, *args, **kwargs) -> Incomplete:
        ...

    def splitlines(self, *args, **kwargs) -> Incomplete:
        ...

    def rfind(self, *args, **kwargs) -> Incomplete:
        ...

    def rsplit(self, *args, **kwargs) -> Incomplete:
        ...

    def rindex(self, *args, **kwargs) -> Incomplete:
        ...

    def partition(self, *args, **kwargs) -> Incomplete:
        ...

    def hex(self, *args, **kwargs) -> Incomplete:
        ...

    def rpartition(self, *args, **kwargs) -> Incomplete:
        ...

    def strip(self, *args, **kwargs) -> Incomplete:
        ...

    def upper(self, *args, **kwargs) -> Incomplete:
        ...

    def decode(self, *args, **kwargs) -> Incomplete:
        ...

    def center(self, *args, **kwargs) -> Incomplete:
        ...

    def index(self, *args, **kwargs) -> Incomplete:
        ...

    def format(self, *args, **kwargs) -> Incomplete:
        ...

    def isalpha(self, *args, **kwargs) -> Incomplete:
        ...

    def replace(self, *args, **kwargs) -> Incomplete:
        ...

    def count(self, *args, **kwargs) -> Incomplete:
        ...

    def find(self, *args, **kwargs) -> Incomplete:
        ...

    def endswith(self, *args, **kwargs) -> Incomplete:
        ...

    def isdigit(self, *args, **kwargs) -> Incomplete:
        ...

    def join(self, *args, **kwargs) -> Incomplete:
        ...

    def lower(self, *args, **kwargs) -> Incomplete:
        ...

    def lstrip(self, *args, **kwargs) -> Incomplete:
        ...

    def isspace(self, *args, **kwargs) -> Incomplete:
        ...

    def islower(self, *args, **kwargs) -> Incomplete:
        ...

    def isupper(self, *args, **kwargs) -> Incomplete:
        ...

    @classmethod
    def fromhex(cls, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class bytearray():
    def rstrip(self, *args, **kwargs) -> Incomplete:
        ...

    def rsplit(self, *args, **kwargs) -> Incomplete:
        ...

    def split(self, *args, **kwargs) -> Incomplete:
        ...

    def startswith(self, *args, **kwargs) -> Incomplete:
        ...

    def replace(self, *args, **kwargs) -> Incomplete:
        ...

    def rindex(self, *args, **kwargs) -> Incomplete:
        ...

    def rfind(self, *args, **kwargs) -> Incomplete:
        ...

    def splitlines(self, *args, **kwargs) -> Incomplete:
        ...

    def partition(self, *args, **kwargs) -> Incomplete:
        ...

    def hex(self, *args, **kwargs) -> Incomplete:
        ...

    def rpartition(self, *args, **kwargs) -> Incomplete:
        ...

    def strip(self, *args, **kwargs) -> Incomplete:
        ...

    def upper(self, *args, **kwargs) -> Incomplete:
        ...

    def decode(self, *args, **kwargs) -> Incomplete:
        ...

    def center(self, *args, **kwargs) -> Incomplete:
        ...

    def find(self, *args, **kwargs) -> Incomplete:
        ...

    def extend(self, *args, **kwargs) -> Incomplete:
        ...

    def format(self, *args, **kwargs) -> Incomplete:
        ...

    def index(self, *args, **kwargs) -> Incomplete:
        ...

    def append(self, *args, **kwargs) -> Incomplete:
        ...

    def endswith(self, *args, **kwargs) -> Incomplete:
        ...

    def count(self, *args, **kwargs) -> Incomplete:
        ...

    def lstrip(self, *args, **kwargs) -> Incomplete:
        ...

    def isalpha(self, *args, **kwargs) -> Incomplete:
        ...

    def isupper(self, *args, **kwargs) -> Incomplete:
        ...

    def join(self, *args, **kwargs) -> Incomplete:
        ...

    def lower(self, *args, **kwargs) -> Incomplete:
        ...

    def islower(self, *args, **kwargs) -> Incomplete:
        ...

    def isdigit(self, *args, **kwargs) -> Incomplete:
        ...

    def isspace(self, *args, **kwargs) -> Incomplete:
        ...

    @classmethod
    def fromhex(cls, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class dict():
    def popitem(self, *args, **kwargs) -> Incomplete:
        ...

    def pop(self, *args, **kwargs) -> Incomplete:
        ...

    def values(self, *args, **kwargs) -> Incomplete:
        ...

    def setdefault(self, *args, **kwargs) -> Incomplete:
        ...

    def update(self, *args, **kwargs) -> Incomplete:
        ...

    def copy(self, *args, **kwargs) -> Incomplete:
        ...

    def clear(self, *args, **kwargs) -> Incomplete:
        ...

    def keys(self, *args, **kwargs) -> Incomplete:
        ...

    def get(self, *args, **kwargs) -> Incomplete:
        ...

    def items(self, *args, **kwargs) -> Incomplete:
        ...

    @classmethod
    def fromkeys(cls, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class map():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class list():
    def pop(self, *args, **kwargs) -> Incomplete:
        ...

    def insert(self, *args, **kwargs) -> Incomplete:
        ...

    def index(self, *args, **kwargs) -> Incomplete:
        ...

    def remove(self, *args, **kwargs) -> Incomplete:
        ...

    def reverse(self, *args, **kwargs) -> Incomplete:
        ...

    def sort(self, *args, **kwargs) -> Incomplete:
        ...

    def clear(self, *args, **kwargs) -> Incomplete:
        ...

    def append(self, *args, **kwargs) -> Incomplete:
        ...

    def extend(self, *args, **kwargs) -> Incomplete:
        ...

    def copy(self, *args, **kwargs) -> Incomplete:
        ...

    def count(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class int():
    def to_bytes(self, *args, **kwargs) -> Incomplete:
        ...

    @classmethod
    def from_bytes(cls, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class OSError(Exception):
    ...

class ZeroDivisionError(Exception):
    ...

class StopIteration(Exception):
    ...

class RuntimeError(Exception):
    ...

class OverflowError(Exception):
    ...

class SyntaxError(Exception):
    ...

class ValueError(Exception):
    ...

class TypeError(Exception):
    ...

class SystemExit(Exception):
    ...
