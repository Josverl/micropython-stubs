"""
heap queue algorithm. See: https://docs.micropython.org/en/v1.15/library/uheapq.html

|see_cpython_module| :mod:`python:heapq` https://docs.python.org/3/library/heapq.html .

This module implements the heap queue algorithm.

A heap queue is simply a list that has its elements stored in a certain way.
"""

# source version: v1.15
# origin module:: micropython/docs/library/uheapq.rst
from typing import IO, Any, Callable, Coroutine, Dict, Generator, Iterator, List, NoReturn, Optional, Tuple, Union
def heappush(heap, item) -> Any:
    """
       Push the ``item`` onto the ``heap``.
    """
    ...
def heappop(heap) -> Any:
    """
       Pop the first item from the ``heap``, and return it.  Raises IndexError if
       heap is empty.
    """
    ...
def heapify(x) -> Any:
    """
       Convert the list ``x`` into a heap.  This is an in-place operation.
    """
    ...
