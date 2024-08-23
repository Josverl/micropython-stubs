"""
Access to underlying platform’s identifying data.

MicroPython module: https://docs.micropython.org/en/v1.23.0/library/platform.html

|see_cpython_module| :mod:`python:platform`.

This module tries to retrieve as much platform-identifying data as possible. It
makes this information available via function APIs.
"""

# source version: v1.23.0
# origin module:: repos/micropython/docs/library/platform.rst
from __future__ import annotations
from typing import Tuple
from _typeshed import Incomplete

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

def python_compiler() -> str:
    """
    Returns a string identifying the compiler used for compiling MicroPython.
    """
    ...

def libc_ver() -> Tuple:
    """
    Returns a tuple of strings *(lib, version)*, where *lib* is the name of the
    libc that MicroPython is linked to, and *version* the corresponding version
    of this libc.
    """
    ...
