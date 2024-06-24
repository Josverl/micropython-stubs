"""
Heap queue algorithm.

MicroPython module: https://docs.micropython.org/en/v1.22.2/library/heapq.html

CPython module: :mod:`python:heapq` https://docs.python.org/3/library/heapq.html .

This module implements the
`min heap queue algorithm <https://en.wikipedia.org/wiki/Heap_%28data_structure%29>`_.

A heap queue is essentially a list that has its elements stored in such a way
that the first item of the list is always the smallest.

---
Module: 'uheapq' on micropython-v1.22.2-rp2-RPI_PICO
"""

# MCU: {'build': '', 'ver': '1.22.2', 'version': '1.22.2', 'port': 'rp2', 'board': 'RPI_PICO', 'mpy': 'v6.2', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete

def heappop(heap) -> Incomplete:
    """
    Pop the first item from the ``heap``, and return it.  Raise ``IndexError`` if
    ``heap`` is empty.

    The returned item will be the smallest item in the ``heap``.
    """
    ...

def heappush(heap, item) -> Incomplete:
    """
    Push the ``item`` onto the ``heap``.
    """
    ...

def heapify(x) -> Incomplete:
    """
    Convert the list ``x`` into a heap.  This is an in-place operation.
    """
    ...
