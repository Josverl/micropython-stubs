"""
Random numbers.

<<<<<<<< HEAD:stubs/micropython-v1_24_1-docstubs/random/__init__.pyi
MicroPython module: https://docs.micropython.org/en/v1.24.0/library/random.html
========
MicroPython module: https://docs.micropython.org/en/preview.0/library/random.html
>>>>>>>> reference/rp2:stubs/micropython-preview-docstubs/random/__init__.pyi

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
"""

# source version: preview
# origin module:: repos/micropython/docs/library/random.rst
from __future__ import annotations
from _typeshed import Incomplete
from typing import Any, Optional
from typing_extensions import TypeVar, TypeAlias, Awaitable

def getrandbits(n) -> int:
    """
    Return an integer with *n* random bits (0 <= n <= 32).
    """
    ...

def randint(a, b) -> int:
    """
    Return a random integer in the range [*a*, *b*].
    """
    ...

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

def uniform(a, b) -> int:
    """
    Return a random floating point number N such that *a* <= N <= *b* for *a* <= *b*,
    and *b* <= N <= *a* for *b* < *a*.
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

def choice(sequence) -> Incomplete:
    """
    Chooses and returns one item at random from *sequence* (tuple, list or
    any object that supports the subscript operation).
    """
    ...
