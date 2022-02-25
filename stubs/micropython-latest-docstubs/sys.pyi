"""
system specific functions. See: https://docs.micropython.org/en/latest/library/sys.html

|see_cpython_module| :mod:`python:sys` https://docs.python.org/3/library/sys.html .
"""

# source version: latest
# origin module:: micropython/docs/library/sys.rst
from typing import IO, Any, Callable, Coroutine, Dict, Generator, Iterator, List, NoReturn, Optional, Tuple, Union

#    A mutable list of arguments the current program was started with.
argv: List
#    The byte order of the system (``"little"`` or ``"big"``).
byteorder: Any = ...
#    Object with information about the current Python implementation. For
#    MicroPython, it has following attributes:
#
#    * *name* - string "micropython"
#    * *version* - tuple (major, minor, micro), e.g. (1, 7, 0)
#
#    This object is the recommended way to distinguish MicroPython from other
#    Python implementations (note that it still may not exist in the very
#    minimal ports).
implementation: Any = ...
#    Maximum value which a native integer type can hold on the current platform,
#    or maximum value representable by MicroPython integer type, if it's smaller
#    than platform max value (that is the case for MicroPython ports without
#    long int support).
#
#    This attribute is useful for detecting "bitness" of a platform (32-bit vs
#    64-bit, etc.). It's recommended to not compare this attribute to some
#    value directly, but instead count number of bits in it::
#
#     bits = 0
#     v = sys.maxsize
#     while v:
#         bits += 1
#         v >>= 1
#     if bits > 32:
#         # 64-bit (or more) platform
maxsize: int = 1
#    Dictionary of loaded modules. On some ports, it may not include builtin
#    modules.
modules: Dict
#    A mutable list of directories to search for imported modules.
path: List
#    The platform that MicroPython is running on. For OS/RTOS ports, this is
#    usually an identifier of the OS, e.g. ``"linux"``. For baremetal ports it
#    is an identifier of a board, e.g. ``"pyboard"`` for the original MicroPython
#    reference board. It thus can be used to distinguish one board from another.
#    If you need to check whether your program runs on MicroPython (vs other
#    Python implementation), use `sys.implementation` instead.
platform: Any = ...
#    Standard error `stream`.
stderr: Any = ...
#    Standard input `stream`.
stdin: Any = ...
#    Standard output `stream`.
stdout: Any = ...
#    Python language version that this implementation conforms to, as a string.
version: str = ""
#    Python language version that this implementation conforms to, as a tuple of ints.
version_info: Tuple

def exit(retval=0, /) -> Any:
    """
    Terminate current program with a given exit code. Underlyingly, this
    function raise as `SystemExit` exception. If an argument is given, its
    value given as an argument to `SystemExit`.
    """
    ...

def atexit(func) -> Any:
    """
    Register *func* to be called upon termination.  *func* must be a callable
    that takes no arguments, or ``None`` to disable the call.  The ``atexit``
    function will return the previous value set by this function, which is
    initially ``None``.
    """
    ...

def print_exception(exc, file=stdout, /) -> None:
    """
    Print exception with a traceback to a file-like object *file* (or
    `sys.stdout` by default).
    """
    ...

def settrace(tracefunc) -> None:
    """
    Enable tracing of bytecode execution.  For details see the `CPython
    documentaion `<https://docs.python.org/3/library/sys.html#sys.settrace>.

    This function requires a custom MicroPython build as it is typically not
    present in pre-built firmware (due to it affecting performance).  The relevant
    configuration option is *MICROPY_PY_SYS_SETTRACE*.
    """
    ...
