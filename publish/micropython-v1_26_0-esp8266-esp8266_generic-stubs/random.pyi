"""
Random numbers.

MicroPython module: https://docs.micropython.org/en/v1.26.0/library/random.html

This module implements a pseudo-random number generator (PRNG).

CPython module: :mod:`python:random` https://docs.python.org/3/library/random.html . .

.. note::

   The following notation is used for intervals:

   - () are open interval brackets and do not include their endpoints.
     For example, (0, 1) means greater than 0 and less than 1.
     In set notation: (0, 1) = {x | 0 < x < 1}.

   - [] are closed interval brackets which include all their limit points.
     For example, [0, 1] means greater than or equal to 0 and less than
     or equal to 1.
     In set notation: [0, 1] = {x | 0 <= x <= 1}.

.. note::

   The :func:`randrange`, :func:`randint` and :func:`choice` functions are only
   available if the ``MICROPY_PY_RANDOM_EXTRA_FUNCS`` configuration option is
   enabled.

---
Module: 'random' on micropython-v1.26.0-esp8266-ESP8266_GENERIC
"""

# MCU: {'variant': '', 'build': '', 'arch': 'xtensa', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'board_id': 'ESP8266_GENERIC', 'mpy': 'v6.3', 'ver': '1.26.0', 'family': 'micropython', 'cpu': 'ESP8266', 'version': '1.26.0'}
# Stubber: v1.26.0
from __future__ import annotations
from _typeshed import Incomplete
from _mpy_shed import Subscriptable
from typing import overload
from typing_extensions import Awaitable, TypeAlias, TypeVar

_T = TypeVar("_T")

def seed(n: int | None = None, /) -> None:
    """
    Initialise the random number generator module with the seed *n* which should
    be an integer.  When no argument (or ``None``) is passed in it will (if
    supported by the port) initialise the PRNG with a true random number
    (usually a hardware generated random number).

    The ``None`` case only works if ``MICROPY_PY_RANDOM_SEED_INIT_FUNC`` is
    enabled by the port, otherwise it raises ``ValueError``.
    """
    ...

def getrandbits(n: int, /) -> int:
    """
    Return an integer with *n* random bits (0 <= n <= 32).
    """
    ...

@overload
def randrange(stop: int, /) -> int:
    """
    The first form returns a random integer from the range [0, *stop*).
    The second form returns a random integer from the range [*start*, *stop*).
    The third form returns a random integer from the range [*start*, *stop*) in
    steps of *step*.  For instance, calling ``randrange(1, 10, 2)`` will
    return odd numbers between 1 and 9 inclusive.
    """

@overload
def randrange(start: int, stop: int, /) -> int:
    """
    The first form returns a random integer from the range [0, *stop*).
    The second form returns a random integer from the range [*start*, *stop*).
    The third form returns a random integer from the range [*start*, *stop*) in
    steps of *step*.  For instance, calling ``randrange(1, 10, 2)`` will
    return odd numbers between 1 and 9 inclusive.
    """

@overload
def randrange(start: int, stop: int, step: int, /) -> int:
    """
    The first form returns a random integer from the range [0, *stop*).
    The second form returns a random integer from the range [*start*, *stop*).
    The third form returns a random integer from the range [*start*, *stop*) in
    steps of *step*.  For instance, calling ``randrange(1, 10, 2)`` will
    return odd numbers between 1 and 9 inclusive.
    """
