"""
Access to underlying platform’s identifying data.

MicroPython module: https://docs.micropython.org/en/v1.27.0/library/platform.html

CPython module: :mod:`python:platform` https://docs.python.org/3/library/platform.html .

This module tries to retrieve as much platform-identifying data as possible. It
makes this information available via function APIs.

---
Module: 'platform' on micropython-v1.27.0-esp32-ESP32_GENERIC_C6
"""

# MCU: {'variant': '', 'build': '', 'arch': 'rv32imc', 'port': 'esp32', 'board': 'ESP32_GENERIC_C6', 'board_id': 'ESP32_GENERIC_C6', 'mpy': 'v6.3', 'ver': '1.27.0', 'family': 'micropython', 'cpu': 'ESP32C6', 'version': '1.27.0'}
# Stubber: v1.26.4
from __future__ import annotations
from _typeshed import Incomplete
from typing import Tuple
from typing_extensions import Awaitable, TypeAlias, TypeVar

def python_compiler() -> str:
    """
    Returns a string identifying the compiler used for compiling MicroPython.
    """
    ...

def processor() -> str:
    """
    Returns a string with a detailed name of the processor, if one is available.
    If no name for the processor is known, it will return an empty string
    instead.

    This is currently available only on RISC-V targets (both 32 and 64 bits).
    """
    ...

def platform() -> str:
    """
    Returns a string identifying the underlying platform. This string is composed
    of several substrings in the following order, delimited by dashes (``-``):

    - the name of the platform system (e.g. Unix, Windows or MicroPython)
    - the MicroPython version
    - the architecture of the platform
    - the version of the underlying platform
    - the concatenation of the name of the libc that MicroPython is linked to
      and its corresponding version.

    For example, this could be
    ``"MicroPython-1.20.0-xtensa-IDFv4.2.4-with-newlib3.0.0"``.
    """
    ...

def libc_ver() -> Tuple:
    """
    Returns a tuple of strings *(lib, version)*, where *lib* is the name of the
    libc that MicroPython is linked to, and *version* the corresponding version
    of this libc.
    """
    ...
