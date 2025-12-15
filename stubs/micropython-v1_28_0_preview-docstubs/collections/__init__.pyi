"""
Collection and container types.

MicroPython module: https://docs.micropython.org/en/v1.28.0/library/collections.html

CPython module: :mod:`python:collections` https://docs.python.org/3/library/collections.html .

This module implements advanced collection and container types to
hold/accumulate various objects.
"""

# source version: v1.28.0-preview
# origin module:: repos/micropython/docs/library/collections.rst
from __future__ import annotations
from _typeshed import Incomplete
from typing import Dict, Generic, Any, Tuple
from typing_extensions import TypeVar, TypeAlias, Awaitable
from collections.abc import Iterable

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_T = TypeVar("_T")
class deque():
    """
    Minimal implementation of a deque that implements a FIFO buffer.
    """
    def __init__(self, iterable: tuple[Any], maxlen: int, flags: int = 0, /) -> None:
        """
        Deques (double-ended queues) are a list-like container that support O(1)
        appends and pops from either side of the deque.  New deques are created
        using the following arguments:

            - *iterable* must be the empty tuple, and the new deque is created empty.

            - *maxlen* must be specified and the deque will be bounded to this
              maximum length.  Once the deque is full, any new items added will
              discard items from the opposite end.

            - The optional *flags* can be 1 to check for overflow when adding items.
        """
        ...
    def append(self, x: _T, /) -> None:
        """
                Add *x* to the right side of the deque.
                Raises ``IndexError`` if overflow checking is enabled and there is
                no more room in the queue.
        """
        ...
    def appendleft(self, x: _T, /) -> Incomplete:
        """
                Add *x* to the left side of the deque.
                Raises ``IndexError`` if overflow checking is enabled and there is
                no more room in the queue.
        """
        ...
    def pop(self) -> Incomplete:
        """
                Remove and return an item from the right side of the deque.
                Raises ``IndexError`` if no items are present.
        """
        ...
    def popleft(self) -> Any:
        """
                Remove and return an item from the left side of the deque.
                Raises ``IndexError`` if no items are present.
        """
        ...
    def extend(self, iterable: Iterable[_T], /) -> Incomplete:
        """
                Extend the deque by appending all the items from *iterable* to
                the right of the deque.
                Raises ``IndexError`` if overflow checking is enabled and there is
                no more room in the deque.
        """
        ...
class OrderedDict(Dict[_KT, _VT], Generic[_KT, _VT]):
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
    def __init__(self, *args, **kwargs) -> None:
        ...
    def popitem(self) -> Incomplete:
        """
                Remove and return a (key, value) pair from the dictionary.
                Pairs are returned in LIFO order.
        
                Admonition:Difference to CPython
                    :class: attention
        
                    ``OrderedDict.popitem()`` does not support the ``last=False`` argument and
                    will always remove and return the last item if present.
        
                    A workaround for this is to use ``pop(<first_key>)`` to remove the first item::
        
                        first_key = next(iter(d))
                        d.pop(first_key)
        """
        ...
def namedtuple(name: str, fields: str | Iterable[str]) -> type[Tuple[Any, ...]]:
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
