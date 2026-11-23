"""
Mathematical functions.

MicroPython module: https://docs.micropython.org/en/v1.29.0/library/math.html

CPython module: :mod:`python:math` https://docs.python.org/3/library/math.html .

The ``math`` module provides some basic mathematical functions for
working with floating-point numbers.

*Note:* On the pyboard, floating-point numbers have 32-bit precision.

Availability: not available on WiPy. Floating point support required
for this module.

---
Module: 'math' on micropython-v1.29.0-webassembly-pyscript
"""

# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.29.0
from __future__ import annotations

from typing import Any, AsyncGenerator, Final, Generator, SupportsFloat, overload

from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar

inf: float = inf
nan: float = nan
pi: float = 3.141592653589793
"""the ratio of a circle's circumference to its diameter"""
e: float = 2.718281828459045
"""base of the natural logarithm"""
tau: float = 6.283185307179586

# inspect: arity=2
def ldexp(x: SupportsFloat, exp: int, /) -> float:
    """
    Return ``x * (2**exp)``.
    """
    ...

# inspect: arity=1
def lgamma(x: SupportsFloat, /) -> float:
    """
    Return the natural logarithm of the gamma function of ``x``.
    """
    ...

# inspect: arity=1
def trunc(x: SupportsFloat, /) -> int:
    """
    Return an integer, being ``x`` rounded towards 0.
    """
    ...

def isclose(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def gamma(x: SupportsFloat, /) -> float:
    """
    Return the gamma function of ``x``.
    """
    ...

# inspect: arity=1
def isnan(x: SupportsFloat, /) -> bool:
    """
    Return ``True`` if ``x`` is not-a-number
    """
    ...

# inspect: arity=1
def isfinite(x: SupportsFloat, /) -> bool:
    """
    Return ``True`` if ``x`` is finite.
    """
    ...

# inspect: arity=1
def isinf(x: SupportsFloat, /) -> bool:
    """
    Return ``True`` if ``x`` is infinite.
    """
    ...

# inspect: arity=1
def sqrt(x: SupportsFloat, /) -> float:
    """
    Return the square root of ``x``.
    """
    ...

# inspect: arity=1
def sinh(x: SupportsFloat, /) -> float:
    """
    Return the hyperbolic sine of ``x``.
    """
    ...

@overload
def log(x: SupportsFloat, /) -> float:
    """
    With one argument, return the natural logarithm of *x*.

    With two arguments, return the logarithm of *x* to the given *base*.
    """
    ...

@overload
def log(x: SupportsFloat, base: SupportsFloat, /) -> float:
    """
    With one argument, return the natural logarithm of *x*.

    With two arguments, return the logarithm of *x* to the given *base*.
    """
    ...

# inspect: arity=1
def tan(x: SupportsFloat, /) -> float:
    """
    Return the tangent of ``x``.
    """
    ...

# inspect: arity=1
def tanh(x: SupportsFloat, /) -> float:
    """
    Return the hyperbolic tangent of ``x``.
    """
    ...

# inspect: arity=1
def log2(x: SupportsFloat, /) -> float:
    """
    Return the base-2 logarithm of ``x``.
    """
    ...

# inspect: arity=1
def log10(x: SupportsFloat, /) -> float:
    """
    Return the base-10 logarithm of ``x``.
    """
    ...

# inspect: arity=1
def sin(x: SupportsFloat, /) -> float:
    """
    Return the sine of ``x``.
    """
    ...

# inspect: arity=1
def modf(x: SupportsFloat, /) -> tuple[float, float]:
    """
    Return a tuple of two floats, being the fractional and integral parts of
    ``x``.  Both return values have the same sign as ``x``.
    """
    ...

# inspect: arity=1
def radians(x: SupportsFloat, /) -> float:
    """
    Return degrees ``x`` converted to radians.
    """
    ...

# inspect: arity=1
def atanh(x: SupportsFloat, /) -> float:
    """
    Return the inverse hyperbolic tangent of ``x``.
    """
    ...

# inspect: arity=2
def atan2(y: SupportsFloat, x: SupportsFloat, /) -> float:
    """
    Return the principal value of the inverse tangent of ``y/x``.
    """
    ...

# inspect: arity=1
def atan(x: SupportsFloat, /) -> float:
    """
    Return the inverse tangent of ``x``.
    """
    ...

# inspect: arity=1
def ceil(x: SupportsFloat, /) -> int:
    """
    Return an integer, being ``x`` rounded towards positive infinity.
    """
    ...

# inspect: arity=2
def copysign(x: SupportsFloat, y: SupportsFloat, /) -> float:
    """
    Return ``x`` with the sign of ``y``.
    """
    ...

# inspect: arity=1
def frexp(x: SupportsFloat, /) -> tuple[float, int]:
    """
    Decomposes a floating-point number into its mantissa and exponent.
    The returned value is the tuple ``(m, e)`` such that ``x == m * 2**e``
    exactly.  If ``x == 0`` then the function returns ``(0.0, 0)``, otherwise
    the relation ``0.5 <= abs(m) < 1`` holds.
    """
    ...

# inspect: arity=1
def acos(x: SupportsFloat, /) -> float:
    """
    Return the inverse cosine of ``x``.
    """
    ...

# inspect: arity=2
def pow(x: SupportsFloat, y: SupportsFloat, /) -> float:
    """
    Returns ``x`` to the power of ``y``.
    """
    ...

# inspect: arity=1
def asinh(x: SupportsFloat, /) -> float:
    """
    Return the inverse hyperbolic sine of ``x``.
    """
    ...

# inspect: arity=1
def acosh(x: SupportsFloat, /) -> float:
    """
    Return the inverse hyperbolic cosine of ``x``.
    """
    ...

# inspect: arity=1
def asin(x: SupportsFloat, /) -> float:
    """
    Return the inverse sine of ``x``.
    """
    ...

# inspect: arity=1
def factorial(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def fabs(x: SupportsFloat, /) -> float:
    """
    Return the absolute value of ``x``.
    """
    ...

# inspect: arity=1
def expm1(x: SupportsFloat, /) -> float:
    """
    Return ``exp(x) - 1``.
    """
    ...

# inspect: arity=1
def floor(x: SupportsFloat, /) -> int:
    """
    Return an integer, being ``x`` rounded towards negative infinity.
    """
    ...

# inspect: arity=2
def fmod(x: SupportsFloat, y: SupportsFloat, /) -> float:
    """
    Return the remainder of ``x/y``.
    """
    ...

# inspect: arity=1
def cos(x: SupportsFloat, /) -> float:
    """
    Return the cosine of ``x``.
    """
    ...

# inspect: arity=1
def degrees(x: SupportsFloat, /) -> float:
    """
    Return radians ``x`` converted to degrees.
    """
    ...

# inspect: arity=1
def cosh(x: SupportsFloat, /) -> float:
    """
    Return the hyperbolic cosine of ``x``.
    """
    ...

# inspect: arity=1
def exp(x: SupportsFloat, /) -> float:
    """
    Return the exponential of ``x``.
    """
    ...

# inspect: arity=1
def erf(x: SupportsFloat, /) -> float:
    """
    Return the error function of ``x``.
    """
    ...

# inspect: arity=1
def erfc(x: SupportsFloat, /) -> float:
    """
    Return the complementary error function of ``x``.
    """
    ...
