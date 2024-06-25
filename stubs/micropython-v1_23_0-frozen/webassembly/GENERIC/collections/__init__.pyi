"""
Collection and container types.

MicroPython module: https://docs.micropython.org/en/v1.23.0/library/collections.html

CPython module: :mod:`python:collections` https://docs.python.org/3/library/collections.html .

This module implements advanced collection and container types to
hold/accumulate various objects.
"""

from __future__ import annotations
from ucollections import *
from .defaultdict import defaultdict as defaultdict
from stdlib.collections import OrderedDict as stdlib_OrderedDict, deque as stdlib_deque, namedtuple as stdlib_namedtuple
from _typeshed import Incomplete

class MutableMapping: ...
