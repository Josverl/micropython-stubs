"""
Mathematical functions for complex numbers.

MicroPython module: https://docs.micropython.org/en/v1.23.0/library/cmath.html

CPython module: :mod:`python:cmath` https://docs.python.org/3/library/cmath.html .

The ``cmath`` module provides some basic mathematical functions for
working with complex numbers.

Availability: not available on WiPy and ESP8266. Floating point support
required for this module.

---
Module: 'cmath' on micropython-v1.23.0-esp32-ESP32_GENERIC
"""

# MCU: {'version': '1.23.0', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': '1.23.0', 'cpu': 'ESP32'}
# Stubber: v1.23.0
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
