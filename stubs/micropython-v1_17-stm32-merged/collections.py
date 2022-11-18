"""
collection and container types. See: https://docs.micropython.org/en/v1.17/library/collections.html

|see_cpython_module| :mod:`python:collections` https://docs.python.org/3/library/collections.html .

This module implements advanced collection and container types to
hold/accumulate various objects.
"""
# MCU: {'ver': 'v1.17', 'port': 'pyboard', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.17.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.17.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'pyboard', 'family': 'micropython'}
# Stubber: 1.5.4
from typing import Optional, Any


class OrderedDict:
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

    def __init__(self, *args) -> None:
        """"""
        ...

    def clear(self, *args, **kwargs) -> Any:
        ...

    def copy(self, *args, **kwargs) -> Any:
        ...

    def get(self, *args, **kwargs) -> Any:
        ...

    def items(self, *args, **kwargs) -> Any:
        ...

    def keys(self, *args, **kwargs) -> Any:
        ...

    def pop(self, *args, **kwargs) -> Any:
        ...

    def popitem(self, *args, **kwargs) -> Any:
        ...

    def setdefault(self, *args, **kwargs) -> Any:
        ...

    def update(self, *args, **kwargs) -> Any:
        ...

    def values(self, *args, **kwargs) -> Any:
        ...

    @classmethod
    def fromkeys(cls, *args, **kwargs) -> Any:
        ...


class deque:
    """
    Deques (double-ended queues) are a list-like container that support O(1)
    appends and pops from either side of the deque.  New deques are created
    using the following arguments:

        - *iterable* must be the empty tuple, and the new deque is created empty.

        - *maxlen* must be specified and the deque will be bounded to this
          maximum length.  Once the deque is full, any new items added will
          discard items from the opposite end.

        - The optional *flags* can be 1 to check for overflow when adding items.

    As well as supporting `bool` and `len`, deque objects have the following
    methods:
    """

    def __init__(self, iterable, maxlen, flags: Optional[Any] = None) -> None:
        """"""
        ...

    def append(self, x) -> Any:
        """
        Add *x* to the right side of the deque.
        Raises IndexError if overflow checking is enabled and there is no more room left.
        """
        ...

    def popleft(self) -> Any:
        """
        Remove and return an item from the left side of the deque.
        Raises IndexError if no items are present.
        """
        ...


def namedtuple(name, fields) -> Any:
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