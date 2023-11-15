from _typeshed import Incomplete as Incomplete
from typing import Dict, List, Tuple

argv: List
byteorder: Incomplete
implementation: Incomplete
maxsize: int
modules: Dict
path: List
platform: Incomplete
ps1: Incomplete
ps2: Incomplete
stderr: Incomplete
stdin: Incomplete
stdout: Incomplete
tracebacklimit: int
version: str
version_info: Tuple

def exit(retval: int = ...) -> Incomplete:
    """
    Terminate current program with a given exit code. Underlyingly, this
    function raise as `SystemExit` exception. If an argument is given, its
    value given as an argument to `SystemExit`.
    """

def atexit(func) -> Incomplete:
    """
    Register *func* to be called upon termination.  *func* must be a callable
    that takes no arguments, or ``None`` to disable the call.  The ``atexit``
    function will return the previous value set by this function, which is
    initially ``None``.

    Difference to CPython

       This function is a MicroPython extension intended to provide similar
       functionality to the :mod:`atexit` module in CPython.
    """

def print_exception(exc, file=...) -> None:
    """
    Print exception with a traceback to a file-like object *file* (or
    `sys.stdout` by default).

    Difference to CPython

       This is simplified version of a function which appears in the
       ``traceback`` module in CPython. Unlike ``traceback.print_exception()``,
       this function takes just exception value instead of exception type,
       exception value, and traceback object; *file* argument should be
       positional; further arguments are not supported. CPython-compatible
       ``traceback`` module can be found in `micropython-lib`.
    """

def settrace(tracefunc) -> None:
    """
    Enable tracing of bytecode execution.  For details see the `CPython
    documentaion `<https://docs.python.org/3/library/sys.html#sys.settrace>.

    This function requires a custom MicroPython build as it is typically not
    present in pre-built firmware (due to it affecting performance).  The relevant
    configuration option is *MICROPY_PY_SYS_SETTRACE*.
    """
