"""
Collection and container types.

MicroPython module: https://docs.micropython.org/en/v1.25.0/library/collections.html

CPython module: :mod:`python:collections` https://docs.python.org/3/library/collections.html .

This module implements advanced collection and container types to
hold/accumulate various objects.
"""

from __future__ import annotations
from ucollections import *
from .defaultdict import defaultdict as defaultdict
from _typeshed import Incomplete
from collections.abc import Mapping
from typing import overload
from typing_extensions import Awaitable, TypeAlias, TypeVar

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

class MutableMapping: ...

class OrderedDict:
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
