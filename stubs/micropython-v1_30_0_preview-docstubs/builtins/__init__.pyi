"""
All builtin functions and exceptions are described here. They are also.

MicroPython module: https://docs.micropython.org/en/v1.30.0/library/builtins.html
available via ``builtins`` module.

MicroPython builds are configurable, so some builtins and capabilities
described below are not available on all builds. See the code or the `MicroPython
configuration macros <https://github.com/micropython/micropython/wiki/macros_micropy#micropy_py_builtins>`_
page on the Wiki for details.
"""

# source version: v1.30.0-preview
# origin module:: repos/micropython/docs/library/builtins.rst
from __future__ import annotations
from _typeshed import Incomplete
from typing import Any, Callable, Iterator, List, Optional, Tuple
from typing_extensions import TypeVar, TypeAlias, Awaitable
from _mpy_shed import AnyReadableBuf, AnyWritableBuf
import sys
from typing import TypeIs

class bool:
    """
    |see_cpython| `python:bool`.

    A Boolean value, either True or False.
    """
    def __init__(self, x=False, /) -> None: ...

class bytearray:
    """
    |see_cpython| `python:bytearray`.

    Slice deletion or assignment with a step other than 1 is not implemented,
    and slice-assignment only accepts a value supporting the same operations
    as a list (not an arbitrary iterable).

    - :ref:`cpydiff_types_bytearray_sliceassign`
    """
    def __init__(self, source=b"", encoding=None, errors=None, /) -> None: ...

class bytes:
    """
    |see_cpython| `python:bytes`.

    ``bytes(string, encoding)`` does not accept ``encoding`` as a keyword
    argument -- pass it positionally. ``bytes`` objects also support
    ``.format()`` (in addition to ``%``-formatting), and subscripting with a
    step other than 1 is not implemented.

    - :ref:`cpydiff_types_bytes_keywords`
    - :ref:`cpydiff_types_bytes_format`
    - :ref:`cpydiff_types_bytes_subscrstep`
    """
    def __init__(self, source=b"", encoding=None, errors=None, /) -> None: ...
    def decode(self, encoding="utf-8", errors="strict") -> Incomplete:
        """
        Decode the bytes object to a string using the specified *encoding*.

        MicroPython supports the following encodings:

        - ``'utf-8'`` or ``'utf8'`` - UTF-8 encoding (default)
        - ``'ascii'`` - ASCII encoding (subset of UTF-8)

        The *errors* parameter controls how decoding errors are handled:

        - ``'strict'`` - Raise a ``UnicodeError`` on invalid UTF-8 (default)
        - ``'ignore'`` - Skip invalid bytes
        - ``'replace'`` - Replace invalid bytes with U+FFFD '�'

        .. note::
            The ``'ignore'`` and ``'replace'`` error handlers are not available
            on all builds.

        Example::

            >>> b'\xc2\xa9 2024'.decode('utf-8')  # © symbol
            '© 2024'
            >>> b'hello\xffworld'.decode('utf-8', 'ignore')  # Skip invalid bytes
            'helloworld'

        Raises ``LookupError`` if the encoding is not supported, or
        ``UnicodeError`` if the data contains invalid UTF-8 and ``errors='strict'``.
        """
        ...

class complex:
    """
    |see_cpython| `python:complex`.

    Unlike CPython, the string parser also accepts a space (instead of a
    ``+``) between the real and imaginary parts, e.g. ``complex("1 1j")``.

    - :ref:`cpydiff_types_complex_parser`
    """
    def __init__(self, real=0, imag=0, /) -> None: ...

class dict:
    """
    |see_cpython| `python:dict`.

    The object returned by ``dict.keys()`` does not behave as a set view --
    set operations such as ``&`` or ``|`` against it are not supported.

    - :ref:`cpydiff_types_dict_keys_set`
    """
    def __init__(self, mapping_or_iterable=(), /, **kwarg) -> None: ...

class float:
    """
    |see_cpython| `python:float`.

    Unlike CPython, MicroPython implicitly converts an object that implements
    ``__float__()`` when it appears alongside a ``float`` in a math operation,
    instead of requiring an explicit ``float(obj)`` conversion.

    - :ref:`cpydiff_types_float_implicit_conversion`
    """
    def __init__(self, x=0.0, /) -> None: ...

class frozenset:
    """
    |see_cpython| `python:frozenset`.

    An immutable set.
    """
    def __init__(self, iterable=(), /) -> None: ...

class int:
    """
    |see_cpython| `python:int`.
    """
    def __init__(self, x=0, base=10, /) -> None: ...
    @classmethod
    def from_bytes(cls, bytes, byteorder, /) -> Incomplete:
        """
        In MicroPython, `byteorder` parameter must be positional (this is
        compatible with CPython).
        """
        ...
    def to_bytes(self, length=1, byteorder="big", *, signed=False) -> List[int]:
        """
            Return an array of bytes representing an integer.

        Unlike CPython, ``int`` does not implement the ``bit_length()`` method.
        Arithmetic on ``int`` subclasses does not convert the result back to that
        subclass.

        - :ref:`cpydiff_types_int_bit_length`
        - :ref:`cpydiff_types_int_subclassconv`
        """
        ...

class list:
    """
    |see_cpython| `python:list`.

    Loading, storing or deleting a slice with a step other than 1 is not
    implemented, and slice-assignment only accepts a ``tuple`` or ``list`` on
    the right-hand side rather than an arbitrary iterable.

    - :ref:`cpydiff_types_list_store_subscrstep`
    - :ref:`cpydiff_types_list_delete_subscrstep`
    - :ref:`cpydiff_types_list_store_noniter`
    """
    def __init__(self, iterable=(), /) -> None: ...

class memoryview:
    """
    |see_cpython| `python:memoryview`.

    Unlike CPython, MicroPython does not prevent a ``bytearray`` or
    ``io.BytesIO`` object from being resized while a ``memoryview`` still
    references it; doing so can leave the ``memoryview`` referencing invalid,
    freed memory.

    - :ref:`cpydiff_types_memoryview_invalid`
    """
    def __init__(self, obj, /) -> None: ...

class object:
    """
    |see_cpython| `python:object`.

    User-defined classes do not support the ``__del__`` special method.
    When subclassing a native type, methods inherited from that native base
    should not be used before ``super().__init__()`` has been called.

    - :ref:`cpydiff_core_class_delnotimpl`
    - :ref:`cpydiff_core_class_super_init`
    """
    def __init__(self) -> None: ...

class property:
    """
    |see_cpython| `python:property`.

    In a subclass that overrides a property, accessing the property through
    ``super()`` returns the ``property`` object itself rather than invoking
    the getter and returning its value.

    - :ref:`cpydiff_core_class_superproperty`
    """
    def __init__(self, fget=None, fset=None, fdel=None, /, doc=None) -> None: ...

class set:
    """
    |see_cpython| `python:set`.

    Return a new set object, optionally with elements taken from ``iterable``.
    """
    def __init__(self, iterable=(), /) -> None: ...

class slice:
    """
    |see_cpython| `python:slice`.

    The *slice* builtin is the type that slice objects have, and cannot be instantiated directly.
    """
    def __init__(self) -> None: ...

class str:
    """
    |see_cpython| `python:str`.

    A number of `str` methods and behaviours available in CPython are not
    implemented: ``str(bytes, encoding)`` does not accept ``encoding`` as a
    keyword argument, ``ljust()``/``rjust()`` do not exist, ``rsplit(None,
    n)`` is not supported, and subscripting with a step other than 1 is not
    implemented. ``str.format()`` does not support attribute/index access in
    replacement fields (e.g. ``"{a[0]}"``), and does not reject the ``,``
    grouping option for non-decimal presentation types like CPython does
    """
    def __init__(self, object="", encoding=None, errors=None, /) -> None: ...
    def encode(self, encoding="utf-8") -> Incomplete:
        """
        Encode the string to bytes using the specified *encoding*.

        MicroPython supports the following encodings:

        - ``'utf-8'`` or ``'utf8'`` - UTF-8 encoding (default)
        - ``'ascii'`` - ASCII encoding (subset of UTF-8)

        Example::

            >>> '© 2024'.encode('utf-8')  # Copyright symbol
            b'\xc2\xa9 2024'

        Raises ``LookupError`` if the encoding is not supported.
        """
        ...
    def center(self, width) -> int:
        """
            Return a centered string of length *width*. Padding is done using spaces.

            When full Unicode support is available, this method counts Unicode
            characters rather than bytes, ensuring proper alignment for multi-byte
            UTF-8 characters.

            Example::

                >>> 'café'.center(10)  # é is 2 bytes in UTF-8
                '   café   '

        - :ref:`cpydiff_types_str_keywords`
        - :ref:`cpydiff_types_str_ljust_rjust`
        - :ref:`cpydiff_types_str_rsplitnone`
        - :ref:`cpydiff_types_str_subscrstep`
        - :ref:`cpydiff_types_str_formatsubscr`
        - :ref:`cpydiff_types_str_formatsep`
        """
        ...

class tuple:
    """
    |see_cpython| `python:tuple`.

    Subscripting with a step other than 1 is not implemented.

    - :ref:`cpydiff_types_tuple_subscrstep`
    """
    def __init__(self, iterable=(), /) -> None: ...

class AssertionError(Exception): ...
class AttributeError(Exception): ...
class ImportError(Exception): ...
class IndexError(Exception): ...
class KeyboardInterrupt(Exception): ...
class KeyError(Exception): ...
class MemoryError(Exception): ...
class NameError(Exception): ...
class NotImplementedError(Exception): ...
class OSError(Exception): ...
class RuntimeError(Exception): ...
class StopIteration(Exception): ...
class SyntaxError(Exception): ...
class SystemExit(Exception): ...
class TypeError(Exception): ...
class ValueError(Exception): ...
class ZeroDivisionError(Exception): ...

def abs(x, /) -> int:
    """
    |see_cpython| `python:abs`.

    Return the absolute value of a number.
    """
    ...

def all(iterable, /) -> bool:
    """
    |see_cpython| `python:all`.

    Return ``True`` if all elements of the iterable are true.
    """
    ...

def any(iterable, /) -> bool:
    """
    |see_cpython| `python:any`.

    Return ``True`` if any element of the iterable is true.
    """
    ...

def bin(number, /) -> Incomplete:
    """
    |see_cpython| `python:bin`.

    Convert an integer to a binary string prefixed with ``0b``.
    """
    ...

def callable(obj) -> TypeIs[Callable[..., object]]:
    """
    |see_cpython| `python:callable`.

    Return whether the object appears to be callable.
    """
    ...

def chr(i, /) -> str:
    """
    |see_cpython| `python:chr`.

    Return the string of one character whose code point is the given integer.
    On builds without full Unicode support, only code points 0-255 are
    accepted.
    """
    ...

def compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1, /) -> Incomplete:
    """
    |see_cpython| `python:compile`.

    Compile source into a code object that can later be executed by `exec` or
    `eval`. The ``flags``, ``dont_inherit`` and ``optimize`` arguments are
    accepted for CPython compatibility but are ignored.
    """
    ...

def delattr(obj, name, /) -> Incomplete:
    """
    |see_cpython| `python:delattr`.

    The argument *name* should be a string, and this function deletes the named
    attribute from the object given by *obj*.
    """
    ...

def dir(object, /) -> List[str]:
    """
    |see_cpython| `python:dir`.

    Without an argument, return the names in the current local scope; with an
    argument, return the names available on that object. Unlike CPython, the
    returned list is not sorted.
    """
    ...

def divmod(x, y, /) -> Incomplete:
    """
    |see_cpython| `python:divmod`.

    Return the pair ``(x // y, x % y)``.
    """
    ...

def enumerate(iterable, start=0) -> Iterator:
    """
    |see_cpython| `python:enumerate`.

    Return an iterator yielding pairs of index and value.
    """
    ...

def eval(expression, globals=None, locals=None, /) -> Incomplete:
    """
    |see_cpython| `python:eval`.

    Evaluate the given expression and return its value. At module scope this
    behaves as in CPython, but because MicroPython does not keep a symbolic
    namespace for a function's local variables, code run by ``eval()`` inside
    a function cannot see that function's locals: it effectively only has
    access to the module's globals.

    - :ref:`cpydiff_core_locals_eval`
    """
    ...

def exec(source, globals=None, locals=None, /) -> Incomplete:
    """
    |see_cpython| `python:exec`.

    Execute the given source.
    Subject to the same local-scope limitation as :func:`eval`.
    """
    ...

def filter(function, iterable, /) -> Incomplete:
    """
    |see_cpython| `python:filter`.

    Construct an iterator of the elements for which a function returns true.
    """
    ...

def getattr(object, name, default: Optional[Any] = None, /) -> Incomplete:
    """
    |see_cpython| `python:getattr`.

    Return the value of a named attribute of an object, with an optional
    default.
    """
    ...

def globals() -> Incomplete:
    """
    |see_cpython| `python:globals`.

    Return the dictionary representing the current module's global namespace.
    """
    ...

def hasattr(object, name, /) -> bool:
    """
    |see_cpython| `python:hasattr`.

    Return whether the object has the given attribute.
    """
    ...

def hash(object, /) -> Incomplete:
    """
    |see_cpython| `python:hash`.

    Return the hash value of an object. Unlike CPython, the result is always
    truncated to a small, machine-word-sized integer, so hash values will
    generally not match CPython's for the same object.
    """
    ...

def hex(number, /) -> Incomplete:
    """
    |see_cpython| `python:hex`.

    Convert an integer to a hexadecimal string prefixed with ``0x``.
    """
    ...

def id(object, /) -> Incomplete:
    """
    |see_cpython| `python:id`.

    Return an integer that is guaranteed to be constant and unique for the
    object during its lifetime.
    """
    ...

def input(prompt="", /) -> Incomplete:
    """
    |see_cpython| `python:input`.

    Read a line from input, optionally after printing a prompt.
    """
    ...

def isinstance(object, classinfo, /) -> Incomplete:
    """
    |see_cpython| `python:isinstance`.

    Return whether an object is an instance of a class (or one of a tuple of
    classes).
    """
    ...

def issubclass(class_, classinfo, /) -> Tuple:
    """
    |see_cpython| `python:issubclass`.

    Return whether a class is a subclass of another class (or one of a tuple
    of classes).
    """
    ...

def iter(object, /) -> Iterator:
    """
    |see_cpython| `python:iter`.

    Return an iterator for an object. Unlike CPython, the two-argument form
    ``iter(callable, sentinel)`` is not implemented.
    """
    ...

def len(s, /) -> int:
    """
    |see_cpython| `python:len`.

    Return the length of a container.
    """
    ...

def locals() -> Incomplete:
    """
    |see_cpython| `python:locals`.

    At module scope, behaves as in CPython. Inside a function, MicroPython
    compiles local variables to array slots rather than a symbolic namespace,
    so the dictionary returned by ``locals()`` does not include that
    function's local variables.

    - :ref:`cpydiff_core_locals`
    """
    ...

def map(function, *iterables) -> Iterator:
    """
    |see_cpython| `python:map`.

    Apply a function to every item of an iterable, returning an iterator of
    the results.
    """
    ...

def max(arg1, arg2, /, *args, key=None) -> Incomplete:
    """
    |see_cpython| `python:max`.

    Return the largest item in an iterable, or the largest of two or more
    arguments.
    """
    ...

def min(arg1, arg2, /, *args, key=None) -> Incomplete:
    """
    |see_cpython| `python:min`.

    Return the smallest item in an iterable, or the smallest of two or more
    arguments.
    """
    ...

def next(iterator, default: Optional[Any] = None, /) -> Incomplete:
    """
    |see_cpython| `python:next`.

    Retrieve the next item from an iterator.

    .. note::
        The two-argument form ``next(iterator, default)`` is not available on all builds.
    """
    ...

def oct(number, /) -> Incomplete:
    """
    |see_cpython| `python:oct`.

    Convert an integer to an octal string prefixed with ``0o``.
    """
    ...

def open(name, mode="r", **kwargs) -> Incomplete:
    """
    |see_cpython| `python:open`.

    Open a file.
    See also :func:`io.open`.
    """
    ...

def ord(c, /) -> str:
    """
    |see_cpython| `python:ord`.

    Return the code point of a one-character string.
    """
    ...

def pow(base, exp, mod=None, /) -> Incomplete:
    """
    |see_cpython| `python:pow`.

    Return ``base`` raised to the power ``exp``, optionally modulo ``mod``.

    .. note::
        The three-argument form is not available on all builds; where it is not
        available it raises `NotImplementedError`.
    """
    ...

def print(*objects, sep=" ", end="\n", file=sys.stdout) -> Incomplete:
    """
    |see_cpython| `python:print`.

    Print objects to a text stream, separated by ``sep`` and followed by
    ``end``. Unlike CPython, the ``flush`` keyword argument is not supported.
    """
    ...

def range(start, stop, step=1, /) -> Incomplete:
    """
    |see_cpython| `python:range`.

    ``start``/``stop``/``step`` values large enough to overflow the
    interpreter's native integer type may raise `OverflowError`, or produce an
    incorrect ``len()``.

    - :ref:`cpydiff_types_range_limits`
    """
    ...

def repr(object, /) -> Incomplete:
    """
    |see_cpython| `python:repr`.

    Return a printable representation of an object.
    """
    ...

def reversed(sequence, /) -> Iterator:
    """
    |see_cpython| `python:reversed`.

    Return a reverse iterator.
    """
    ...

def round(number, ndigits: Optional[Any] = None, /) -> int:
    """
    |see_cpython| `python:round`.

    Return ``number`` rounded to ``ndigits`` precision after the decimal point.
    If ``ndigits`` is omitted or is None, it returns the nearest integer to its input.
    """
    ...

def setattr(object, name, value, /) -> Incomplete:
    """
    |see_cpython| `python:setattr`.

    Set a named attribute on an object to a given value.
    """
    ...

def sorted(iterable, /, *, key=None, reverse=False) -> Incomplete:
    """
    |see_cpython| `python:sorted`.

    Return a new sorted list from the items in an iterable.
    """
    ...

def sum(iterable, start=0, /) -> Incomplete:
    """
    |see_cpython| `python:sum`.

    Sum the items of an iterable, with an optional start value.
    """
    ...

def super(type, obj) -> Incomplete:
    """
    |see_cpython| `python:super`.

    Only the zero-argument form (which may only be used inside a method body)
    and the two-argument form ``super(type, obj)`` are implemented; the
    single-argument "unbound" form ``super(type)`` is not supported.
    The method resolution order used to look up attributes through ``super()`` is
    a simplified, depth-first search rather than CPython's C3 linearization.
    Therefore results can differ in non-trivial multiple-inheritance hierarchies, and
    calling ``super()`` from a class with multiple base classes only reaches
    one of them rather than cooperatively chaining through all of them.

    - :ref:`cpydiff_core_class_mro`
    - :ref:`cpydiff_core_class_supermultiple`
    """
    ...

def type(name, bases, dict, /) -> Incomplete:
    """
    |see_cpython| `python:type`.

    Class creation follows the same simplified
    method resolution order described under :func:`super`.
    """
    ...

def zip(*iterables) -> Incomplete:
    """
    |see_cpython| `python:zip`.

    Iterate over several iterables in parallel.
    """
    ...
