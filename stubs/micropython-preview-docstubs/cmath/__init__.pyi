"""
Mathematical functions for complex numbers.

<<<<<<<< HEAD:stubs/micropython-v1_24_1-docstubs/cmath/__init__.pyi
MicroPython module: https://docs.micropython.org/en/v1.24.0/library/cmath.html
========
MicroPython module: https://docs.micropython.org/en/preview.0/library/cmath.html
>>>>>>>> reference/rp2:stubs/micropython-preview-docstubs/cmath/__init__.pyi

CPython module: :mod:`python:cmath` https://docs.python.org/3/library/cmath.html .

The ``cmath`` module provides some basic mathematical functions for
working with complex numbers.

Availability: not available on WiPy and ESP8266. Floating point support
required for this module.
"""

# source version: preview
# origin module:: repos/micropython/docs/library/cmath.rst
from __future__ import annotations
from _typeshed import Incomplete
from typing import Tuple
from typing_extensions import TypeVar, TypeAlias, Awaitable
from typing_extensions import TypeAlias

e: float
"""base of the natural logarithm"""
pi: float
"""the ratio of a circle's circumference to its diameter"""

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

def sqrt(z) -> Incomplete:
    """
    Return the square-root of ``z``.
    """
    ...
