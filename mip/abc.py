"""
abc.py - Micropython runtime Abstract Base Classes module
"""

from typing import _any_call  # type: ignore


def abstractmethod(funcobj):
    return funcobj


def __getattr__(attr):
    return _any_call
