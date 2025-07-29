"""
Heap queue algorithm.

MicroPython module: https://docs.micropython.org/en/v1.26.0/library/heapq.html

CPython module: :mod:`python:heapq` https://docs.python.org/3/library/heapq.html .

This module implements the
`min heap queue algorithm <https://en.wikipedia.org/wiki/Heap_%28data_structure%29>`_.

A heap queue is essentially a list that has its elements stored in such a way
that the first item of the list is always the smallest.

---
Module: 'heapq' on micropython-v1.26.0-preview-esp32-ESP32_GENERIC_S3
"""

# MCU: {'variant': '', 'build': 'preview.434.g096ff8b9e', 'arch': 'xtensawin', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'board_id': 'ESP32_GENERIC_S3', 'mpy': 'v6.3', 'ver': '1.26.0-preview-preview.434.g096ff8b9e', 'family': 'micropython', 'cpu': 'ESP32S3', 'version': '1.26.0-preview'}
# Stubber: v1.25.0
from __future__ import annotations
from _typeshed import Incomplete
from typing import Any
from typing_extensions import Awaitable, TypeAlias, TypeVar

_T = TypeVar("_T")

def heappop(heap: list[_T], /) -> _T:
    """
    Pop the first item from the ``heap``, and return it.  Raise ``IndexError`` if
    ``heap`` is empty.

    The returned item will be the smallest item in the ``heap``.
    """
    ...

def heappush(heap: list[_T], item: _T, /) -> None:
    """
    Push the ``item`` onto the ``heap``.
    """
    ...

def heapify(x: list[Any], /) -> None:
    """
    Convert the list ``x`` into a heap.  This is an in-place operation.
    """
    ...
