"""
access to underlying platform’s identifying data. See: https://docs.micropython.org/en/latest/library/platform.html

|see_cpython_module| :mod:`python:platform` https://docs.python.org/3/library/platform.html .

This module tries to retrieve as much platform-identifying data as possible. It
makes this information available via function APIs.
"""
# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'family': 'micropython', 'build': '449', 'arch': 'xtensawin', 'ver': 'v1.20.0-449', 'cpu': 'SPIRAM'})
# Stubber: v1.13.7
from typing import Tuple, Any


class platform:
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

    def __init__(self) -> None:
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
