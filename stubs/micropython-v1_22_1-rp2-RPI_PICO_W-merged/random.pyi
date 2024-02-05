"""
Random numbers.

MicroPython module: https://docs.micropython.org/en/v1.22.1/library/random.html

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
Module: 'random' on micropython-v1.22.1-rp2-RPI_PICO_W
"""
# MCU: {'family': 'micropython', 'version': '1.22.1', 'build': '', 'ver': '1.22.1', 'port': 'rp2', 'board': 'RPI_PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.17.1
from __future__ import annotations
from _typeshed import Incomplete
from typing import Any, Optional

def randrange(start, stop, step: Optional[Any] = None) -> int:
    """
    The first form returns a random integer from the range [0, *stop*).
    The second form returns a random integer from the range [*start*, *stop*).
    The third form returns a random integer from the range [*start*, *stop*) in
    steps of *step*.  For instance, calling ``randrange(1, 10, 2)`` will
    return odd numbers between 1 and 9 inclusive.
    """
    ...

def random() -> int:
    """
    Return a random floating point number in the range [0.0, 1.0).
    """
    ...

def seed(n=None, /) -> None:
    """
    Initialise the random number generator module with the seed *n* which should
    be an integer.  When no argument (or ``None``) is passed in it will (if
    supported by the port) initialise the PRNG with a true random number
    (usually a hardware generated random number).

    The ``None`` case only works if ``MICROPY_PY_RANDOM_SEED_INIT_FUNC`` is
    enabled by the port, otherwise it raises ``ValueError``.
    """
    ...

def uniform(a, b) -> int:
    """
    Return a random floating point number N such that *a* <= N <= *b* for *a* <= *b*,
    and *b* <= N <= *a* for *b* < *a*.
    """
    ...

def choice(sequence) -> Incomplete:
    """
    Chooses and returns one item at random from *sequence* (tuple, list or
    any object that supports the subscript operation).
    """
    ...

def randint(a, b) -> int:
    """
    Return a random integer in the range [*a*, *b*].
    """
    ...

def getrandbits(n) -> int:
    """
    Return an integer with *n* random bits (0 <= n <= 32).
    """
    ...
