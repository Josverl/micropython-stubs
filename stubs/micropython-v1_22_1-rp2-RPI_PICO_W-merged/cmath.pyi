"""
Mathematical functions for complex numbers.

MicroPython module: https://docs.micropython.org/en/v1.22.1/library/cmath.html

CPython module: :mod:`python:cmath` https://docs.python.org/3/library/cmath.html .

The ``cmath`` module provides some basic mathematical functions for
working with complex numbers.

Availability: not available on WiPy and ESP8266. Floating point support
required for this module.

---
Module: 'cmath' on micropython-v1.22.1-rp2-RPI_PICO_W
"""
# MCU: {'family': 'micropython', 'version': '1.22.1', 'build': '', 'ver': '1.22.1', 'port': 'rp2', 'board': 'RPI_PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.17.1
from __future__ import annotations
from _typeshed import Incomplete
from typing import Tuple

e: float = 2.718282
pi: float = 3.141593

def polar(z) -> Tuple:
    """
    Returns, as a tuple, the polar form of ``z``.
    """
    ...

def sqrt(z) -> Incomplete:
    """
    Return the square-root of ``z``.
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

def exp(z) -> float:
    """
    Return the exponential of ``z``.
    """
    ...

def cos(z) -> float:
    """
    Return the cosine of ``z``.
    """
    ...

def phase(z) -> float:
    """
    Returns the phase of the number ``z``, in the range (-pi, +pi].
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
