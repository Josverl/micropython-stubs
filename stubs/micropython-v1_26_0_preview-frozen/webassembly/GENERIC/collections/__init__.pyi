"""
Collection and container types.

MicroPython module: https://docs.micropython.org/en/v1.26.0/library/collections.html

CPython module: :mod:`python:collections` https://docs.python.org/3/library/collections.html .

This module implements advanced collection and container types to
hold/accumulate various objects.
"""

from __future__ import annotations
from ucollections import *
from .defaultdict import defaultdict as defaultdict
from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

class MutableMapping: ...
