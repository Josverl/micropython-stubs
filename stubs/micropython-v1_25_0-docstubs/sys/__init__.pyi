"""
System specific functions.

MicroPython module: https://docs.micropython.org/en/v1.25.0/library/sys.html

CPython module: :mod:`python:sys` https://docs.python.org/3/library/sys.html .
"""

# source version: v1.25.0
# origin module:: repos/micropython/docs/library/sys.rst
from __future__ import annotations
from _typeshed import Incomplete
from typing import Callable, NoReturn, overload, Dict, List, Tuple
from typing_extensions import TypeVar, TypeAlias, Awaitable
from _mpy_shed import IOBase_mp, _mp_implementation

argv: List
"""A mutable list of arguments the current program was started with."""
byteorder: Incomplete
"""The byte order of the system (``"little"`` or ``"big"``)."""
implementation: Incomplete
"""\
Object with information about the current Python implementation. For
MicroPython, it has following attributes:

* *name* - string "micropython"
* *version* - tuple (major, minor, micro, releaselevel), e.g. (1, 22, 0, '')
* *_machine* - string describing the underlying machine
* *_mpy* - supported mpy file-format version (optional attribute)
* *_build* - string that can help identify the configuration that
MicroPython was built with

This object is the recommended way to distinguish MicroPython from other
Python implementations (note that it still may not exist in the very
minimal ports).

Starting with version 1.22.0-preview, the fourth node *releaselevel* in
*implementation.version* is either an empty string or ``"preview"``.

The *_build* entry was added in version 1.25.0 and is a hyphen-separated
set of elements.  New elements may be appended in the future so it's best to
access this field using ``sys.implementation._build.split("-")``.  The
elements that are currently used are:

* On the unix, webassembly and windows ports the first element is the variant
name, for example ``'standard'``.
* On microcontroller targets, the first element is the board name and the second
element (if present) is the board variant, for example ``'RPI_PICO2-RISCV'``

Admonition:Difference to CPython
:class: attention

CPython mandates more attributes for this object, but the actual useful
bare minimum is implemented in MicroPython.
"""
maxsize: int
"""\
Maximum value which a native integer type can hold on the current platform,
or maximum value representable by MicroPython integer type, if it's smaller
than platform max value (that is the case for MicroPython ports without
long int support).

This attribute is useful for detecting "bitness" of a platform (32-bit vs
64-bit, etc.). It's recommended to not compare this attribute to some
value directly, but instead count number of bits in it::

bits = 0
v = sys.maxsize
while v:
bits += 1
v >>= 1
if bits > 32:
# 64-bit (or more) platform
"""
modules: Dict
"""\
Dictionary of loaded modules. On some ports, it may not include builtin
modules.
"""
path: List
"""\
A mutable list of directories to search for imported modules.

Admonition:Difference to CPython
:class: attention

On MicroPython, an entry with the value ``".frozen"`` will indicate that import
should search :term:`frozen modules <frozen module>` at that point in the search.
If no frozen module is found then search will *not* look for a directory called
``.frozen``, instead it will continue with the next entry in ``sys.path``.
"""
platform: Incomplete
"""\
The platform that MicroPython is running on. For OS/RTOS ports, this is
usually an identifier of the OS, e.g. ``"linux"``. For baremetal ports it
is an identifier of a board, e.g. ``"pyboard"`` for the original MicroPython
reference board. It thus can be used to distinguish one board from another.
If you need to check whether your program runs on MicroPython (vs other
Python implementation), use `sys.implementation` instead.
"""
ps1: Incomplete
"""\
Mutable attributes holding strings, which are used for the REPL prompt.  The defaults
give the standard Python prompt of ``>>>`` and ``...``.
"""
ps2: Incomplete
"""\
Mutable attributes holding strings, which are used for the REPL prompt.  The defaults
give the standard Python prompt of ``>>>`` and ``...``.
"""
stderr: Incomplete
"""Standard error `stream`."""
stdin: Incomplete
"""Standard input `stream`."""
stdout: Incomplete
"""Standard output `stream`."""
tracebacklimit: int
"""\
A mutable attribute holding an integer value which is the maximum number of traceback
entries to store in an exception.  Set to 0 to disable adding tracebacks.  Defaults
to 1000.

Note: this is not available on all ports.
"""
version: str
"""Python language version that this implementation conforms to, as a string."""
version_info: Tuple
"""\
Python language version that this implementation conforms to, as a tuple of ints.

Admonition:Difference to CPython
:class: attention

Only the first three version numbers (major, minor, micro) are supported and
they can be referenced only by index, not by name.
"""

@overload
def exit(retval: object = 0, /) -> NoReturn:
    """
    Terminate current program with a given exit code. Underlyingly, this
    function raises a `SystemExit` exception. If an argument is given, its
    value given as an argument to `SystemExit`.

    On embedded ports (i.e. all ports but Windows and Unix), an unhandled
    `SystemExit` currently causes a :ref:`soft_reset` of MicroPython.
    """
    ...

@overload
def atexit(func: Callable[[], None] | None, /) -> Callable[[], None] | None:
    """
    Register *func* to be called upon termination.  *func* must be a callable
    that takes no arguments, or ``None`` to disable the call.  The ``atexit``
    function will return the previous value set by this function, which is
    initially ``None``.

    Admonition:Difference to CPython
       :class: attention

       This function is a MicroPython extension intended to provide similar
       functionality to the :mod:`atexit` module in CPython.
    """
    ...

@overload
def print_exception(exc: Exception | BaseException, file: IOBase_mp = stdout, /) -> None:
    """
    Print exception with a traceback to a file-like object *file* (or
    `sys.stdout` by default).

    Admonition:Difference to CPython
       :class: attention

       This is simplified version of a function which appears in the
       ``traceback`` module in CPython. Unlike ``traceback.print_exception()``,
       this function takes just exception value instead of exception type,
       exception value, and traceback object; *file* argument should be
       positional; further arguments are not supported. CPython-compatible
       ``traceback`` module can be found in `micropython-lib`.
    """
    ...

@overload
def settrace(tracefunc) -> None:
    """
    Enable tracing of bytecode execution.  For details see the `CPython
    documentation `<https://docs.python.org/3/library/sys.html#sys.settrace>.

    This function requires a custom MicroPython build as it is typically not
    present in pre-built firmware (due to it affecting performance).  The relevant
    configuration option is *MICROPY_PY_SYS_SETTRACE*.
    """
    ...
