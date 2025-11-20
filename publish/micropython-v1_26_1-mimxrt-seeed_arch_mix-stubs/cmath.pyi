"""
Mathematical functions for complex numbers.

MicroPython module: https://docs.micropython.org/en/v1.26.0/library/cmath.html

CPython module: :mod:`python:cmath` https://docs.python.org/3/library/cmath.html .

The ``cmath`` module provides some basic mathematical functions for
working with complex numbers.

Availability: not available on WiPy and ESP8266. Floating point support
required for this module.

---
Module: 'cmath' on micropython-v1.26.1-mimxrt-SEEED_ARCH_MIX
"""

# MCU: {'variant': '', 'build': '', 'arch': 'armv7emdp', 'port': 'mimxrt', 'board': 'SEEED_ARCH_MIX', 'board_id': 'SEEED_ARCH_MIX', 'mpy': 'v6.3', 'ver': '1.26.1', 'family': 'micropython', 'cpu': 'MIMXRT1052DVL5B', 'version': '1.26.1'}
# Stubber: v1.26.3
from __future__ import annotations
from _typeshed import Incomplete
from typing import SupportsComplex, SupportsFloat, SupportsIndex, Tuple
from typing_extensions import Awaitable, TypeAlias, TypeVar

_C: TypeAlias = SupportsFloat | SupportsComplex | SupportsIndex | complex

e: float = 2.718281828459045
"""base of the natural logarithm"""
pi: float = 3.141592653589793
"""the ratio of a circle's circumference to its diameter"""

def polar(z: _C, /) -> Tuple:
    """
    Returns, as a tuple, the polar form of ``z``.
    """
    ...

def sqrt(z: _C, /) -> complex:
    """
    Return the square-root of ``z``.
    """
    ...

def rect(r: float, phi: float, /) -> float:
    """
    Returns the complex number with modulus ``r`` and phase ``phi``.
    """
    ...

def sin(z: _C, /) -> float:
    """
    Return the sine of ``z``.
    """
    ...

def exp(z: _C, /) -> float:
    """
    Return the exponential of ``z``.
    """
    ...

def cos(z: _C, /) -> float:
    """
    Return the cosine of ``z``.
    """
    ...

def phase(z: _C, /) -> float:
    """
    Returns the phase of the number ``z``, in the range (-pi, +pi].
    """
    ...

def log(z: _C, /) -> float:
    """
    Return the natural logarithm of ``z``.  The branch cut is along the negative real axis.
    """
    ...

def log10(z: _C, /) -> float:
    """
    Return the base-10 logarithm of ``z``.  The branch cut is along the negative real axis.
    """
    ...
