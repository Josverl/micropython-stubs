"""MicroPython compiler-provided builtins for static type checkers."""

from _typeshed import ReadableBuffer
from typing import Any, Mapping, TypeVar
from typing_extensions import Self, TypeAlias

# BEGIN: BUILTINS
Const_T = TypeVar("Const_T", int, float, str, bytes, tuple)  # noqa: PYI001

#: Unsigned machine-word integer used by the Viper emitter. This type is
#: primarily useful as a Viper function return annotation. It makes MicroPython
#: interpret ``0xffffffff`` as ``2**32 - 1`` rather than ``-1``.
uint: TypeAlias = int  # noqa: PYI042

class ptr(int):
    """Viper pointer to an object or memory address.

    Create a pointer from an integer address or an object supporting the buffer
    protocol. Plain ``ptr`` values are not subscriptable; use a sized pointer
    type for direct memory access.

    Pointer operations are only valid in native/Viper code and do not perform
    bounds checks. Invalid addresses or indexes can corrupt memory or crash the
    device.
    """

    def __new__(cls, value: int | ReadableBuffer, /) -> Self: ...

class ptr8(ptr):
    """Viper pointer providing indexed access to unsigned 8-bit bytes.

    Indexes address individual bytes. Slices and bounds checks are not supported.
    """

    def __getitem__(self, index: int, /) -> int: ...
    def __setitem__(self, index: int, value: int, /) -> None: ...

class ptr16(ptr):
    """Viper pointer providing indexed access to unsigned 16-bit half-words.

    Indexes are scaled by two bytes. Slices and bounds checks are not supported.
    """

    def __getitem__(self, index: int, /) -> int: ...
    def __setitem__(self, index: int, value: int, /) -> None: ...

class ptr32(ptr):
    """Viper pointer providing indexed access to unsigned 32-bit machine words.

    Indexes are scaled by four bytes. Slices and bounds checks are not supported.
    """

    def __getitem__(self, index: int, /) -> int: ...
    def __setitem__(self, index: int, value: int, /) -> None: ...

def const(expr: Const_T, /) -> Const_T:
    """Declare an expression as a compile-time constant.

    MicroPython may substitute the value during compilation. A name beginning
    with an underscore is hidden from module globals and consumes no runtime
    storage.
    """
    ...

def execfile(filename: str, globals: dict[str, Any] | None = None, locals: Mapping[str, object] | None = None, /) -> None:
    """Execute the file *filename* with semantics equivalent to Python 2's ``execfile``.

    Only available on ports/builds with ``MICROPY_PY_BUILTINS_EXECFILE`` enabled
    (disabled by default on most embedded ports). Unlike `exec`, *filename* must
    be a `str`; passing anything else (including `bytes`) raises `TypeError`.
    """
    ...

# END: BUILTINS
