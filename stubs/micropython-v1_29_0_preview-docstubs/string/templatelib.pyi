"""
PEP 750 template string support.

MicroPython module: https://docs.micropython.org/en/v1.29.0/library/string.templatelib.html

This module provides support for template strings (t-strings) as defined in
`PEP 750 <https://peps.python.org/pep-0750/>`_. Template strings are created
using the ``t`` prefix and provide access to both the literal string parts and
interpolated values before they are combined.

**Availability:** template strings require ``MICROPY_PY_TSTRINGS`` to be enabled
at compile time. They are enabled by default at the full feature level, which
includes the alif, mimxrt and samd (SAMD51 only) ports, the unix coverage variant
and the webassembly pyscript variant.
"""

# source version: v1.29.0-preview
# origin module:: repos/micropython/docs/library/string.templatelib.rst
from __future__ import annotations
from _typeshed import Incomplete
from typing_extensions import TypeVar, TypeAlias, Awaitable

class Template:
    """
    Represents a template string. Template objects are typically created by
    t-string syntax (``t"..."``) but can also be constructed directly using
    the constructor.
    """
    def __init__(self, *args) -> None: ...
    def __iter__(self) -> Incomplete:
        """
        Iterate over the template contents, yielding string parts and
        :class:`Interpolation` objects in the order they appear. Empty strings
        are omitted.
        """
        ...
    def __add__(self, other) -> Incomplete:
        """
        Concatenate two templates. Returns a new :class:`Template` combining
        the strings and interpolations from both templates.

        :raises TypeError: if *other* is not a :class:`Template`

        Template concatenation with ``str`` is prohibited to avoid ambiguity
        about whether the string should be treated as a literal or interpolation::

           t1 = t"Hello "
           t2 = t"World"
           result = t1 + t2  # Valid

           # TypeError: cannot concatenate str to Template
           result = t1 + "World"
        """
        ...

class Interpolation:
    """
    Represents an interpolated expression within a template string. All
    arguments can be passed as keyword arguments.
    """
    def __init__(self, value, expression="", conversion=None, format_spec="") -> None: ...
