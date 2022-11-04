"""
heap queue algorithm. See: https://docs.micropython.org/en/v1.18/library/heapq.html

|see_cpython_module| :mod:`python:heapq` https://docs.python.org/3/library/heapq.html .

This module implements the
`min heap queue algorithm <https://en.wikipedia.org/wiki/Heap_%28data_structure%29>`_.

A heap queue is essentially a list that has its elements stored in such a way
that the first item of the list is always the smallest.
"""
# MCU: {'ver': 'v1.18', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.18.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.18.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.4
from typing import Any


def heapify(x) -> Any:
    """
    Convert the list ``x`` into a heap.  This is an in-place operation.
    """
    ...


def heappop(heap) -> Any:
    """
    Pop the first item from the ``heap``, and return it.  Raise ``IndexError`` if
    ``heap`` is empty.

    The returned item will be the smallest item in the ``heap``.
    """
    ...


def heappush(heap, item) -> Any:
    """
    Push the ``item`` onto the ``heap``.
    """
    ...
