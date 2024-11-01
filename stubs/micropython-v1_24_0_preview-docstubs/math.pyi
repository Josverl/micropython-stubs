"""
Mathematical functions.

MicroPython module: https://docs.micropython.org/en/v1.24.0-preview/library/math.html

CPython module: :mod:`python:math` https://docs.python.org/3/library/math.html .

The ``math`` module provides some basic mathematical functions for
working with floating-point numbers.

*Note:* On the pyboard, floating-point numbers have 32-bit precision.

Availability: not available on WiPy. Floating point support required
for this module.
"""

# source version: v1.24.0-preview
# origin module:: repos/micropython/docs/library/math.rst
from __future__ import annotations
from typing import Tuple
from _typeshed import Incomplete

e: float
"""base of the natural logarithm"""
pi: float
"""the ratio of a circle's circumference to its diameter"""

def acos(x) -> float:
    """
    Return the inverse cosine of ``x``.
    """
    ...

def acosh(x) -> float:
    """
    Return the inverse hyperbolic cosine of ``x``.
    """
    ...

def asin(x) -> float:
    """
    Return the inverse sine of ``x``.
    """
    ...

def asinh(x) -> float:
    """
    Return the inverse hyperbolic sine of ``x``.
    """
    ...

def atan(x) -> float:
    """
    Return the inverse tangent of ``x``.
    """
    ...

def atan2(y, x) -> float:
    """
    Return the principal value of the inverse tangent of ``y/x``.
    """
    ...

def atanh(x) -> float:
    """
    Return the inverse hyperbolic tangent of ``x``.
    """
    ...

def ceil(x) -> int:
    """
    Return an integer, being ``x`` rounded towards positive infinity.
    """
    ...

def copysign(x, y) -> Incomplete:
    """
    Return ``x`` with the sign of ``y``.
    """
    ...

def cos(x) -> float:
    """
    Return the cosine of ``x``.
    """
    ...

def cosh(x) -> float:
    """
    Return the hyperbolic cosine of ``x``.
    """
    ...

def degrees(x) -> Incomplete:
    """
    Return radians ``x`` converted to degrees.
    """
    ...

def erf(x) -> Incomplete:
    """
    Return the error function of ``x``.
    """
    ...

def erfc(x) -> Incomplete:
    """
    Return the complementary error function of ``x``.
    """
    ...

def exp(x) -> float:
    """
    Return the exponential of ``x``.
    """
    ...

def expm1(x) -> Incomplete:
    """
    Return ``exp(x) - 1``.
    """
    ...

def fabs(x) -> Incomplete:
    """
    Return the absolute value of ``x``.
    """
    ...

def floor(x) -> int:
    """
    Return an integer, being ``x`` rounded towards negative infinity.
    """
    ...

def fmod(x, y) -> Incomplete:
    """
    Return the remainder of ``x/y``.
    """
    ...

def frexp(x) -> Incomplete:
    """
    Decomposes a floating-point number into its mantissa and exponent.
    The returned value is the tuple ``(m, e)`` such that ``x == m * 2**e``
    exactly.  If ``x == 0`` then the function returns ``(0.0, 0)``, otherwise
    the relation ``0.5 <= abs(m) < 1`` holds.
    """
    ...

def gamma(x) -> Incomplete:
    """
    Return the gamma function of ``x``.
    """
    ...

def isfinite(x) -> bool:
    """
    Return ``True`` if ``x`` is finite.
    """
    ...

def isinf(x) -> bool:
    """
    Return ``True`` if ``x`` is infinite.
    """
    ...

def isnan(x) -> bool:
    """
    Return ``True`` if ``x`` is not-a-number
    """
    ...

def ldexp(x, exp) -> Incomplete:
    """
    Return ``x * (2**exp)``.
    """
    ...

def lgamma(x) -> float:
    """
    Return the natural logarithm of the gamma function of ``x``.
    """
    ...

def log(x, base) -> float:
    """
    With one argument, return the natural logarithm of *x*.

    With two arguments, return the logarithm of *x* to the given *base*.
    """
    ...

def log10(x) -> float:
    """
    Return the base-10 logarithm of ``x``.
    """
    ...

def log2(x) -> float:
    """
    Return the base-2 logarithm of ``x``.
    """
    ...

def modf(x) -> Tuple:
    """
    Return a tuple of two floats, being the fractional and integral parts of
    ``x``.  Both return values have the same sign as ``x``.
    """
    ...

def pow(x, y) -> Incomplete:
    """
    Returns ``x`` to the power of ``y``.
    """
    ...

def radians(x) -> Incomplete:
    """
    Return degrees ``x`` converted to radians.
    """
    ...

def sin(x) -> float:
    """
    Return the sine of ``x``.
    """
    ...

def sinh(x) -> float:
    """
    Return the hyperbolic sine of ``x``.
    """
    ...

def sqrt(x) -> Incomplete:
    """
    Return the square root of ``x``.
    """
    ...

def tan(x) -> float:
    """
    Return the tangent of ``x``.
    """
    ...

def tanh(x) -> float:
    """
    Return the hyperbolic tangent of ``x``.
    """
    ...

def trunc(x) -> int:
    """
    Return an integer, being ``x`` rounded towards 0.
    """
    ...
