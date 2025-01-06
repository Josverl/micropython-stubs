"""
Collection and container types.

MicroPython module: https://docs.micropython.org/en/v1.24.1/library/collections.html

CPython module: :mod:`python:collections` https://docs.python.org/3/library/collections.html .

This module implements advanced collection and container types to
hold/accumulate various objects.
"""

# source version: v1.24.1
# origin module:: repos/micropython/docs/library/collections.rst
from __future__ import annotations

from collections.abc import Iterable, Mapping, MutableSequence
from typing import Any, Tuple, TypeVar, overload

from _collections_abc import *
from typing_extensions import TypeVar

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_S = TypeVar("_S")
_T = TypeVar("_T")
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_KT_co = TypeVar("_KT_co", covariant=True)
_VT_co = TypeVar("_VT_co", covariant=True)

class deque(MutableSequence[_T]):
    """
    Minimal implementation of a deque that implements a FIFO buffer.
    """

    @overload
    def __init__(self, *, maxlen: int | None = None) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[_T], maxlen: int | None = None) -> None: ...
    def append(self, x: _T, /) -> None:
        """
        Add *x* to the right side of the deque.
        Raises ``IndexError`` if overflow checking is enabled and there is
        no more room in the queue.
        """
        ...

    def appendleft(self, x: _T, /) -> None:
        """
        Add *x* to the left side of the deque.
        Raises ``IndexError`` if overflow checking is enabled and there is
        no more room in the queue.
        """
        ...

    def pop(self) -> _T:
        """
        Remove and return an item from the right side of the deque.
        Raises ``IndexError`` if no items are present.
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
