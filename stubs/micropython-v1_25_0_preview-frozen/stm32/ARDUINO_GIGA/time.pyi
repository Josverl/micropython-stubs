from __future__ import annotations
from utime import *
from _typeshed import Incomplete
from _mpy_shed import _TimeTuple
from typing_extensions import Awaitable, TypeAlias, TypeVar

_TicksMs: TypeAlias = int
_TicksUs: TypeAlias = int
_TicksCPU: TypeAlias = int
_Ticks = TypeVar("_Ticks", _TicksMs, _TicksUs, _TicksCPU, int)

_TS_YEAR: int
_TS_MON: int
_TS_MDAY: int
_TS_HOUR: int
_TS_MIN: int
_TS_SEC: int
_TS_WDAY: int
_TS_YDAY: int
_TS_ISDST: int
_WDAY: Incomplete
_MDAY: Incomplete

def strftime(datefmt, ts): ...
