"""
Heap queue algorithm.

MicroPython module: https://docs.micropython.org/en/v1.21.0/library/heapq.html

CPython module: :mod:`python:heapq` https://docs.python.org/3/library/heapq.html .

This module implements the
`min heap queue algorithm <https://en.wikipedia.org/wiki/Heap_%28data_structure%29>`_.

A heap queue is essentially a list that has its elements stored in such a way
that the first item of the list is always the smallest.
"""
from _typeshed import Incomplete, Incomplete as Incomplete

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
