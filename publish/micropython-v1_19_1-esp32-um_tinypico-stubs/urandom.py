"""
random numbers. See: https://docs.micropython.org/en/v1.19.1/library/random.html

This module implements a pseudo-random number generator (PRNG).

|see_cpython_module| :mod:`python:random` https://docs.python.org/3/library/random.html . .

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
   available if the ``MICROPY_PY_URANDOM_EXTRA_FUNCS`` configuration option is
   enabled.

"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.5.6
from typing import Callable, Coroutine, Dict, Generator, IO, Iterator, List, NoReturn, Optional, Tuple, Union, Any


def choice(sequence) -> Any:
    """
    Chooses and returns one item at random from *sequence* (tuple, list or
    any object that supports the subscript operation).
    """
    ...


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

class random:
    """
    Return a random floating point number in the range [0.0, 1.0).
    """

    def __init__(self) -> None: ...


def randrange(start, stop, step: Optional[Any] = None) -> int:
    """
    The first form returns a random integer from the range [0, *stop*).
    The second form returns a random integer from the range [*start*, *stop*).
    The third form returns a random integer from the range [*start*, *stop*) in
    steps of *step*.  For instance, calling ``randrange(1, 10, 2)`` will
    return odd numbers between 1 and 9 inclusive.

    """
    ...


def seed(n=None, /) -> None:
    """
    Initialise the random number generator module with the seed *n* which should
    be an integer.  When no argument (or ``None``) is passed in it will (if
    supported by the port) initialise the PRNG with a true random number
    (usually a hardware generated random number).

    The ``None`` case only works if ``MICROPY_PY_URANDOM_SEED_INIT_FUNC`` is
    enabled by the port, otherwise it raises ``ValueError``.
    """
    ...


def uniform(a, b) -> int:
    """
    Return a random floating point number N such that *a* <= N <= *b* for *a* <= *b*,
    and *b* <= N <= *a* for *b* < *a*.

    """
    ...
