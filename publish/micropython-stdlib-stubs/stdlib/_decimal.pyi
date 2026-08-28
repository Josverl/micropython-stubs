import sys
from decimal import (
    Clamped as Clamped,
)
from decimal import (
    Context as Context,
)
from decimal import (
    ConversionSyntax as ConversionSyntax,
)
from decimal import (
    Decimal as Decimal,
)
from decimal import (
    DecimalException as DecimalException,
)
from decimal import (
    DecimalTuple as DecimalTuple,
)
from decimal import (
    DivisionByZero as DivisionByZero,
)
from decimal import (
    DivisionImpossible as DivisionImpossible,
)
from decimal import (
    DivisionUndefined as DivisionUndefined,
)
from decimal import (
    FloatOperation as FloatOperation,
)
from decimal import (
    Inexact as Inexact,
)
from decimal import (
    InvalidContext as InvalidContext,
)
from decimal import (
    InvalidOperation as InvalidOperation,
)
from decimal import (
    Overflow as Overflow,
)
from decimal import (
    Rounded as Rounded,
)
from decimal import (
    Subnormal as Subnormal,
)
from decimal import (
    Underflow as Underflow,
)
from types import TracebackType
from typing import Final

from typing_extensions import TypeAlias

_TrapType: TypeAlias = type[DecimalException]

class _ContextManager:
    new_context: Context
    saved_context: Context
    def __init__(self, new_context: Context) -> None: ...
    def __enter__(self) -> Context: ...
    def __exit__(self, t: type[BaseException] | None, v: BaseException | None, tb: TracebackType | None) -> None: ...

__version__: Final[str]
__libmpdec_version__: Final[str]

ROUND_DOWN: Final[str]
ROUND_HALF_UP: Final[str]
ROUND_HALF_EVEN: Final[str]
ROUND_CEILING: Final[str]
ROUND_FLOOR: Final[str]
ROUND_UP: Final[str]
ROUND_HALF_DOWN: Final[str]
ROUND_05UP: Final[str]
HAVE_CONTEXTVAR: Final[bool]
HAVE_THREADS: Final[bool]
MAX_EMAX: Final[int]
MAX_PREC: Final[int]
MIN_EMIN: Final[int]
MIN_ETINY: Final[int]

def setcontext(context: Context, /) -> None: ...
def getcontext() -> Context: ...

if sys.version_info >= (3, 11):
    def localcontext(
        ctx: Context | None = None,
        *,
        prec: int | None = ...,
        rounding: str | None = ...,
        Emin: int | None = ...,
        Emax: int | None = ...,
        capitals: int | None = ...,
        clamp: int | None = ...,
        traps: dict[_TrapType, bool] | None = ...,
        flags: dict[_TrapType, bool] | None = ...,
    ) -> _ContextManager: ...

else:
    def localcontext(ctx: Context | None = None) -> _ContextManager: ...

DefaultContext: Context
BasicContext: Context
ExtendedContext: Context
