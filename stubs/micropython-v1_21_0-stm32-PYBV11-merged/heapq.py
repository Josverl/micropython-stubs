"""
Module: 'heapq' on micropython-v1.21.0-stm32-PYBV11
"""
# MCU: {'version': '1.21.0', 'mpy': 'v6.1', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': '', 'arch': 'armv7emsp', 'ver': 'v1.21.0', 'cpu': 'STM32F405RG'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete as Incomplete, Incomplete


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
