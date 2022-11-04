"""
mathematical functions for complex numbers. See: https://docs.micropython.org/en/v1.18/library/cmath.html

|see_cpython_module| :mod:`python:cmath` https://docs.python.org/3/library/cmath.html .

The ``cmath`` module provides some basic mathematical functions for
working with complex numbers.

Availability: not available on WiPy and ESP8266. Floating point support
required for this module.
"""
# MCU: {'ver': 'v1.18', 'port': 'stm32', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.18.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.18.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'stm32', 'family': 'micropython'}
# Stubber: 1.5.6
from typing import Tuple, Any


def cos(z) -> float:
    """
    Return the cosine of ``z``.
    """
    ...


e = 2.718281828459045  # type: float


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


pi = 3.141592653589793  # type: float


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
