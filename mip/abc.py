"""
abc.py - Micropython runtime Abstract Base Classes module
"""

from typing import _any_call  # type: ignore


# must be a real class to allow `class Foo(ABC):`
class ABC:
    pass


def abstractmethod(funcobj):
    return funcobj


def __getattr__(attr):
    return _any_call
