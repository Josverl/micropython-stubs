"""
Collection and container types.

MicroPython module: https://docs.micropython.org/en/v1.24.1/library/collections.html

CPython module: :mod:`python:collections` https://docs.python.org/3/library/collections.html .

This module implements advanced collection and container types to
hold/accumulate various objects.

---
Module: 'ucollections' on micropython-v1.24.1-esp32-ESP32_GENERIC
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'cpu': 'ESP32', 'mpy': 'v6.3', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import SupportsItems, SupportsKeysAndGetItem, SupportsRichComparison, SupportsRichComparisonT, Incomplete
from _collections_abc import *
from collections.abc import (
    Callable,
    ItemsView,
    Iterator,
    KeysView,
    MutableMapping,
    Sequence,
    ValuesView,
    Iterable,
    Mapping,
    MutableSequence,
)
from typing import Generic, NoReturn, SupportsIndex, TypeVar, final, Any, Tuple, overload
from typing_extensions import Self, TypeVar
import sys
from _mpy_shed import GenericAlias

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_S = TypeVar("_S")
_T = TypeVar("_T")
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_KT_co = TypeVar("_KT_co", covariant=True)
_VT_co = TypeVar("_VT_co", covariant=True)

def namedtuple(
    typename: str,
    field_names: str | Iterable[str],
    *,
    rename: bool = False,
    module: str | None = None,
    defaults: Iterable[Any] | None = None,
) -> type[Tuple[Any, ...]]:
    """
    This is factory function to create a new namedtuple type with a specific
    name and set of fields. A namedtuple is a subclass of tuple which allows
    to access its fields not just by numeric index, but also with an attribute
    access syntax using symbolic field names. Fields is a sequence of strings
    specifying field names. For compatibility with CPython it can also be a
    a string with space-separated field named (but this is less efficient).
    Example of use::

        from collections import namedtuple

        MyTuple = namedtuple("MyTuple", ("id", "name"))
        t1 = MyTuple(1, "foo")
        t2 = MyTuple(2, "bar")
        print(t1.name)
        assert t2.name == t2[1]
    """
    ...

class OrderedDict(dict[_KT, _VT]):
    """
    ``dict`` type subclass which remembers and preserves the order of keys
    added. When ordered dict is iterated over, keys/items are returned in
    the order they were added::

        from collections import OrderedDict

        # To make benefit of ordered keys, OrderedDict should be initialized
        # from sequence of (key, value) pairs.
        d = OrderedDict([("z", 1), ("a", 2)])
        # More items can be added as usual
        d["w"] = 5
        d["b"] = 3
        for k, v in d.items():
            print(k, v)

    Output::

        z 1
        a 2
        w 5
        b 3
    """

    def popitem(self, last: bool = True) -> tuple[_KT, _VT]: ...
    # Same as dict.pop, but accepts keyword arguments
    @overload
    def pop(self, key: _KT) -> _VT: ...
    @overload
    def pop(self, key: _KT, default: _VT) -> _VT: ...
    @overload
    def pop(self, key: _KT, default: _T) -> _VT | _T: ...
    def values(self) -> _odict_values[_KT, _VT]: ...
    # Keep OrderedDict.setdefault in line with MutableMapping.setdefault, modulo positional-only differences.
    @overload
    def setdefault(self: OrderedDict[_KT, _T | None], key: _KT, default: None = None) -> _T | None: ...
    @overload
    def setdefault(self, key: _KT, default: _VT) -> _VT: ...
    def update(self, *args, **kwargs) -> Incomplete: ...
    def copy(self) -> Self: ...
    def clear(self, *args, **kwargs) -> Incomplete: ...
    def keys(self) -> _odict_keys[_KT, _VT]: ...
    def get(self, *args, **kwargs) -> Incomplete: ...
    def items(self) -> _odict_items[_KT, _VT]: ...
    # The signature of OrderedDict.fromkeys should be kept in line with `dict.fromkeys`, modulo positional-only differences.
    # Like dict.fromkeys, its true signature is not expressible in the current type system.
    # See #3800 & https://github.com/python/typing/issues/548#issuecomment-683336963.
    @classmethod
    @overload
    def fromkeys(cls, iterable: Iterable[_T], value: None = None) -> OrderedDict[_T, Any | None]: ...
    @classmethod
    @overload
    def fromkeys(cls, iterable: Iterable[_T], value: _S) -> OrderedDict[_T, _S]: ...
    @overload
    def __init__(self):
        """
        ``dict`` type subclass which remembers and preserves the order of keys
        added. When ordered dict is iterated over, keys/items are returned in
        the order they were added::

            from collections import OrderedDict

            # To make benefit of ordered keys, OrderedDict should be initialized
            # from sequence of (key, value) pairs.
            d = OrderedDict([("z", 1), ("a", 2)])
            # More items can be added as usual
            d["w"] = 5
            d["b"] = 3
            for k, v in d.items():
                print(k, v)

        Output::

            z 1
            a 2
            w 5
            b 3
        """

    @overload
    def __init__(self, **kwargs: _VT):
        """
        ``dict`` type subclass which remembers and preserves the order of keys
        added. When ordered dict is iterated over, keys/items are returned in
        the order they were added::

            from collections import OrderedDict

            # To make benefit of ordered keys, OrderedDict should be initialized
            # from sequence of (key, value) pairs.
            d = OrderedDict([("z", 1), ("a", 2)])
            # More items can be added as usual
            d["w"] = 5
            d["b"] = 3
            for k, v in d.items():
                print(k, v)

        Output::

            z 1
            a 2
            w 5
            b 3
        """

    @overload
    def __init__(self, map: Mapping[_KT, _VT], **kwargs: _VT):
        """
        ``dict`` type subclass which remembers and preserves the order of keys
        added. When ordered dict is iterated over, keys/items are returned in
        the order they were added::

            from collections import OrderedDict

            # To make benefit of ordered keys, OrderedDict should be initialized
            # from sequence of (key, value) pairs.
            d = OrderedDict([("z", 1), ("a", 2)])
            # More items can be added as usual
            d["w"] = 5
            d["b"] = 3
            for k, v in d.items():
                print(k, v)

        Output::

            z 1
            a 2
            w 5
            b 3
        """

class deque(MutableSequence[_T]):
    """
    Minimal implementation of a deque that implements a FIFO buffer.
    """

    def pop(self) -> _T:
        """
        Remove and return an item from the right side of the deque.
        Raises ``IndexError`` if no items are present.
        """
        ...

    def appendleft(self, x: _T, /) -> None:
        """
        Add *x* to the left side of the deque.
        Raises ``IndexError`` if overflow checking is enabled and there is
        no more room in the queue.
        """
        ...

    def popleft(self) -> _T:
        """
        Remove and return an item from the left side of the deque.
        Raises ``IndexError`` if no items are present.
        """
        ...

    def extend(self, iterable: Iterable[_T], /) -> None:
        """
        Extend the deque by appending all the items from *iterable* to
        the right of the deque.
        Raises ``IndexError`` if overflow checking is enabled and there is
        no more room in the deque.
        """
        ...

    def append(self, x: _T, /) -> None:
        """
        Add *x* to the right side of the deque.
        Raises ``IndexError`` if overflow checking is enabled and there is
        no more room in the queue.
        """
        ...

    @overload
    def __init__(self, *, maxlen: int | None = None) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[_T], maxlen: int | None = None) -> None: ...
    @overload
    def __init__(self, *, maxlen: int | None = None) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[_T], maxlen: int | None = None) -> None: ...
