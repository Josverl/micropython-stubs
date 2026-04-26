"""
Mathematical functions for complex numbers.

MicroPython module: https://docs.micropython.org/en/v1.27.0/library/cmath.html

CPython module: :mod:`python:cmath` https://docs.python.org/3/library/cmath.html .

The ``cmath`` module provides some basic mathematical functions for
working with complex numbers.

Availability: not available on WiPy and ESP8266. Floating point support
required for this module.
"""

# source version: v1.27.0
# origin module:: repos/micropython/docs/library/cmath.rst
from __future__ import annotations
from _typeshed import Incomplete
from typing import SupportsComplex, SupportsFloat, SupportsIndex
from typing_extensions import TypeVar, TypeAlias, Awaitable
from typing_extensions import TypeAlias
e: float
"""base of the natural logarithm"""
pi: float
"""the ratio of a circle's circumference to its diameter"""
_C: TypeAlias = SupportsFloat | SupportsComplex | SupportsIndex | complex
def cos(z: _C, /) -> complex:
    """
       Return the cosine of ``z``.
    """
    ...
def exp(z: _C, /) -> complex:
    """
       Return the exponential of ``z``.
    """
    ...
def log(z: _C, /) -> complex:
    """
       Return the natural logarithm of ``z``.  The branch cut is along the negative real axis.
    """
    ...
def log10(z: _C, /) -> complex:
    """
       Return the base-10 logarithm of ``z``.  The branch cut is along the negative real axis.
    """
    ...
def phase(z: _C, /) -> float:
    """
       Returns the phase of the number ``z``, in the range (-pi, +pi].
    """
    ...
def polar(z: _C, /) -> tuple[float, float]:
    """
       Returns, as a tuple, the polar form of ``z``.
    """
    ...
def rect(r: float, phi: float, /) -> complex:
    """
       Returns the complex number with modulus ``r`` and phase ``phi``.
    """
    ...
def sin(z: _C, /) -> complex:
    """
       Return the sine of ``z``.
    """
    ...
def sqrt(z: _C, /) -> complex:
    """
       Return the square-root of ``z``.
    """
    ...
