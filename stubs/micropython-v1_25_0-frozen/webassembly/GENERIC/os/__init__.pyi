"""
Basic "operating system" services.

MicroPython module: https://docs.micropython.org/en/v1.25.0/library/os.html

CPython module: :mod:`python:os` https://docs.python.org/3/library/os.html .

The ``os`` module contains functions for filesystem access and mounting,
terminal redirection and duplication, and the ``uname`` and ``urandom``
functions.
"""

from __future__ import annotations
from uos import *
from . import path as path
from _mpy_shed import uname_result
from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar
