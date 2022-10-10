"""
heap queue algorithm. See: https://docs.micropython.org/en/v1.19.1/library/heapq.html

|see_cpython_module| :mod:`python:heapq` https://docs.python.org/3/library/heapq.html .

This module implements the
`min heap queue algorithm <https://en.wikipedia.org/wiki/Heap_%28data_structure%29>`_.

A heap queue is essentially a list that has its elements stored in such a way
that the first item of the list is always the smallest.
"""
from typing import Callable, Coroutine, Dict, Generator, IO, Iterator, List, NoReturn, Optional, Tuple, Union, Any

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
