"""
mathematical functions for complex numbers. See: https://docs.micropython.org/en/latest/library/cmath.html

|see_cpython_module| :mod:`python:cmath` https://docs.python.org/3/library/cmath.html .

The ``cmath`` module provides some basic mathematical functions for
working with complex numbers.

Availability: not available on WiPy and ESP8266. Floating point support
required for this module.
"""

# source version: latest
# origin module:: micropython/docs/library/cmath.rst
from typing import IO, Any, Callable, Coroutine, Dict, Generator, Iterator, List, NoReturn, Optional, Tuple, Union

#    base of the natural logarithm
e: float
#    the ratio of a circle's circumference to its diameter
pi: float

def cos(z) -> float:
    """
    Return the cosine of ``z``.
    """
    ...

def exp(z) -> float:
    """
    Return the exponential of ``z``.
    """
    ...

def log(z) -> float:
    """
    Return the natural logarithm of ``z``.  The branch cut is along the negative real axis.
    """
    ...

def log10(z) -> float:
    """
    Return the base-10 logarithm of ``z``.  The branch cut is along the negative real axis.
    """
    ...

def phase(z) -> float:
    """
    Returns the phase of the number ``z``, in the range (-pi, +pi].
    """
    ...

def polar(z) -> Tuple:
    """
    Returns, as a tuple, the polar form of ``z``.
    """
    ...

def rect(r, phi) -> float:
    """
    Returns the complex number with modulus ``r`` and phase ``phi``.
    """
    ...

def sin(z) -> float:
    """
    Return the sine of ``z``.
    """
    ...

def sqrt(z) -> Any:
    """
    Return the square-root of ``z``.
    """
    ...
