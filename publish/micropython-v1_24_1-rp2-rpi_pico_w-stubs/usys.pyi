"""
System specific functions.

MicroPython module: https://docs.micropython.org/en/v1.24.0/library/sys.html

CPython module: :mod:`python:sys` https://docs.python.org/3/library/sys.html .

---
Module: 'usys' on micropython-v1.24.1-rp2-RPI_PICO_W
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'rp2', 'board': 'RPI_PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.3', 'arch': 'armv6m'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Callable, Dict, List, NoReturn, Tuple, overload, Any, Generator
from _typeshed import Incomplete
from _mpy_shed import IOBase_mp
from typing_extensions import Awaitable, TypeAlias, TypeVar

platform: str = "rp2"
version_info: tuple = ()
path: list = []
version: str = "3.4.0; MicroPython v1.24.1 on 2024-11-29"
ps1: str = ">>> "
ps2: str = "... "
byteorder: str = "little"
modules: dict = {}
argv: list = []
implementation: tuple = ()
maxsize: int = 2147483647

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
def exit(retval: object = 0, /) -> NoReturn:
    """
    Terminate current program with a given exit code. Underlyingly, this
    function raise as `SystemExit` exception. If an argument is given, its
    value given as an argument to `SystemExit`.
    """
    ...

@overload
def exit(retval: object = 0, /) -> NoReturn:
    """
    Terminate current program with a given exit code. Underlyingly, this
    function raise as `SystemExit` exception. If an argument is given, its
    value given as an argument to `SystemExit`.
    """
    ...

stderr: Incomplete  ## <class 'TextIOWrapper'> = <io.TextIOWrapper 2>
stdout: Incomplete  ## <class 'TextIOWrapper'> = <io.TextIOWrapper 1>
stdin: Incomplete  ## <class 'TextIOWrapper'> = <io.TextIOWrapper 0>

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
def settrace(tracefunc) -> None:
    """
    Enable tracing of bytecode execution.  For details see the `CPython
    documentation `<https://docs.python.org/3/library/sys.html#sys.settrace>.

    This function requires a custom MicroPython build as it is typically not
    present in pre-built firmware (due to it affecting performance).  The relevant
    configuration option is *MICROPY_PY_SYS_SETTRACE*.
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
