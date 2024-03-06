"""
Random numbers.

MicroPython module: https://docs.micropython.org/en/v1.21.0/library/random.html

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
Module: 'random' on micropython-v1.21.0-win32-GENERIC
"""
# MCU: {'version': '1.21.0', 'mpy': '', 'port': 'win32', 'board': 'GENERIC', 'family': 'micropython', 'build': '', 'arch': '', 'ver': 'v1.21.0', 'cpu': ''}
# Stubber: v1.15.0
from typing import Optional, Any
from _typeshed import Incomplete


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


def getrandbits(n) -> int:
    """
    Return an integer with *n* random bits (0 <= n <= 32).
    """
    ...
