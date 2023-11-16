"""
Module: 'uheapq' on micropython-v1.19.1-stm32
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'stm32', 'port': 'stm32', 'machine': 'PYBv1.1 with STM32F405RG', 'release': '1.19.1', 'nodename': 'pyboard', 'name': 'micropython', 'family': 'micropython', 'sysname': 'pyboard', 'version': '1.19.1'}
# Stubber: 1.9.11
from typing import Any
from _typeshed import Incomplete as Incomplete


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
