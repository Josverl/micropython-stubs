"""
Mathematical functions.

MicroPython module: https://docs.micropython.org/en/v1.26.0/library/math.html

CPython module: :mod:`python:math` https://docs.python.org/3/library/math.html .

The ``math`` module provides some basic mathematical functions for
working with floating-point numbers.

*Note:* On the pyboard, floating-point numbers have 32-bit precision.

Availability: not available on WiPy. Floating point support required
for this module.

---
Module: 'math' on micropython-v1.26.0-esp8266-ESP8266_GENERIC
"""

# MCU: {'variant': '', 'build': '', 'arch': 'xtensa', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'board_id': 'ESP8266_GENERIC', 'mpy': 'v6.3', 'ver': '1.26.0', 'family': 'micropython', 'cpu': 'ESP8266', 'version': '1.26.0'}
# Stubber: v1.26.0
from __future__ import annotations
from _typeshed import Incomplete
from typing import SupportsFloat, Tuple
from typing_extensions import Awaitable, TypeAlias, TypeVar

pi: float = 3.141593
e: float = 2.718282

def isnan(x: SupportsFloat, /) -> bool:
    """
    Return ``True`` if ``x`` is not-a-number
    """
    ...

def ldexp(x: SupportsFloat, exp: int, /) -> float:
    """
    Return ``x * (2**exp)``.
    """
    ...

def frexp(x: SupportsFloat, /) -> tuple[float, int]:
    """
    Decomposes a floating-point number into its mantissa and exponent.
    The returned value is the tuple ``(m, e)`` such that ``x == m * 2**e``
    exactly.  If ``x == 0`` then the function returns ``(0.0, 0)``, otherwise
    the relation ``0.5 <= abs(m) < 1`` holds.
    """
    ...

def isinf(x: SupportsFloat, /) -> bool:
    """
    Return ``True`` if ``x`` is infinite.
    """
    ...

def isfinite(x: SupportsFloat, /) -> bool:
    """
    Return ``True`` if ``x`` is finite.
    """
    ...

def trunc(x: SupportsFloat, /) -> int:
    """
    Return an integer, being ``x`` rounded towards 0.
    """
    ...

def sqrt(x: SupportsFloat, /) -> float:
    """
    Return the square root of ``x``.
    """
    ...

def log(x: SupportsFloat, /) -> float:
    """
    With one argument, return the natural logarithm of *x*.

    With two arguments, return the logarithm of *x* to the given *base*.
    """
    ...

def tan(x: SupportsFloat, /) -> float:
    """
    Return the tangent of ``x``.
    """
    ...

def modf(x: SupportsFloat, /) -> Tuple:
    """
    Return a tuple of two floats, being the fractional and integral parts of
    ``x``.  Both return values have the same sign as ``x``.
    """
    ...

def sin(x: SupportsFloat, /) -> float:
    """
    Return the sine of ``x``.
    """
    ...

def radians(x: SupportsFloat, /) -> float:
    """
    Return degrees ``x`` converted to radians.
    """
    ...

def atan(x: SupportsFloat, /) -> float:
    """
    Return the inverse tangent of ``x``.
    """
    ...

def ceil(x: SupportsFloat, /) -> int:
    """
    Return an integer, being ``x`` rounded towards positive infinity.
    """
    ...

def atan2(y: SupportsFloat, x: SupportsFloat, /) -> float:
    """
    Return the principal value of the inverse tangent of ``y/x``.
    """
    ...

def pow(x: SupportsFloat, y: SupportsFloat, /) -> float:
    """
    Returns ``x`` to the power of ``y``.
    """
    ...

def asin(x: SupportsFloat, /) -> float:
    """
    Return the inverse sine of ``x``.
    """
    ...

def acos(x: SupportsFloat, /) -> float:
    """
    Return the inverse cosine of ``x``.
    """
    ...

def fmod(x: SupportsFloat, y: SupportsFloat, /) -> float:
    """
    Return the remainder of ``x/y``.
    """
    ...

def fabs(x: SupportsFloat, /) -> float:
    """
    Return the absolute value of ``x``.
    """
    ...

def copysign(x: SupportsFloat, y: SupportsFloat, /) -> float:
    """
    Return ``x`` with the sign of ``y``.
    """
    ...

def floor(x: SupportsFloat, /) -> int:
    """
    Return an integer, being ``x`` rounded towards negative infinity.
    """
    ...

def cos(x: SupportsFloat, /) -> float:
    """
    Return the cosine of ``x``.
    """
    ...

def exp(x: SupportsFloat, /) -> float:
    """
    Return the exponential of ``x``.
    """
    ...

def degrees(x: SupportsFloat, /) -> float:
    """
    Return radians ``x`` converted to degrees.
    """
    ...
