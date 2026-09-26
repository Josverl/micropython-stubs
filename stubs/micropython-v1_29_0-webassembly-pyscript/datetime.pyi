"""
Module: 'datetime' on micropython-v1.29.0-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.29.0
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete

MAXYEAR: Final[int] = 9999
MINYEAR: Final[int] = 1
# inspect: arity=1
def _iso2t(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def _iso2d(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=4
def _t2iso(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def _leap(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def _o2ymd(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def _d2iso(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=5
def _time(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=2
def _dim(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=3
def _date(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=2
def _dbm(*args, **kwargs) -> Incomplete:
    ...


class datetime():
    # inspect: arity=1
    def isoweekday(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def dst(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def tzname(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def date(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=3
    def isoformat(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def toordinal(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def timestamp(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def timetuple(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def timetz(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def weekday(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def time(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def tuple(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=6
    def replace(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def utcoffset(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def _cmp(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def astimezone(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def _sub(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def _mktime(self, *args, **kwargs) -> Incomplete:
        ...

    year: Incomplete ## <class 'property'> = <property>
    @classmethod
    def now(cls, *args, **kwargs) -> Incomplete:
        ...

    second: Incomplete ## <class 'property'> = <property>
    tzinfo: Incomplete ## <class 'property'> = <property>
    day: Incomplete ## <class 'property'> = <property>
    fold: Incomplete ## <class 'property'> = <property>
    @classmethod
    def fromisoformat(cls, *args, **kwargs) -> Incomplete:
        ...

    @classmethod
    def combine(cls, *args, **kwargs) -> Incomplete:
        ...

    EPOCH: Incomplete ## <class 'datetime'> = datetime.datetime(1970, 1, 1, 0, 0, 0, 0, datetime.timezone(datetime.timedelta(microseconds=0), None), fold=0)
    month: Incomplete ## <class 'property'> = <property>
    microsecond: Incomplete ## <class 'property'> = <property>
    minute: Incomplete ## <class 'property'> = <property>
    @classmethod
    def fromordinal(cls, *args, **kwargs) -> Incomplete:
        ...

    hour: Incomplete ## <class 'property'> = <property>
    @classmethod
    def fromtimestamp(cls, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class timedelta():
    # inspect: arity=2
    def _tuple(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def _fmt(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def isoformat(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def total_seconds(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def tuple(self, *args, **kwargs) -> Incomplete:
        ...

    min: Incomplete ## <class 'timedelta'> = datetime.timedelta(microseconds=-86399999913600000000)
    resolution: Incomplete ## <class 'timedelta'> = datetime.timedelta(microseconds=1)
    seconds: Incomplete ## <class 'property'> = <property>
    max: Incomplete ## <class 'timedelta'> = datetime.timedelta(microseconds=86399999999999999999)
    microseconds: Incomplete ## <class 'property'> = <property>
    days: Incomplete ## <class 'property'> = <property>
    def __init__(self, *argv, **kwargs) -> None:
        ...


class timezone():
    # inspect: arity=2
    def isoformat(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def tzname(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def utcoffset(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def fromutc(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def dst(self, *args, **kwargs) -> Incomplete:
        ...

    utc: Incomplete ## <class 'timezone'> = datetime.timezone(datetime.timedelta(microseconds=0), None)
    def __init__(self, *argv, **kwargs) -> None:
        ...


class tzinfo():
    # inspect: arity=2
    def isoformat(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def tzname(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def utcoffset(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def fromutc(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def dst(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class time():
    # inspect: arity=2
    def _sub(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def dst(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def isoformat(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def tzname(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def utcoffset(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def tuple(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=7
    def replace(self, *args, **kwargs) -> Incomplete:
        ...

    resolution: Incomplete ## <class 'timedelta'> = datetime.timedelta(microseconds=1)
    minute: Incomplete ## <class 'property'> = <property>
    second: Incomplete ## <class 'property'> = <property>
    tzinfo: Incomplete ## <class 'property'> = <property>
    min: Incomplete ## <class 'time'> = datetime.time(microsecond=0, tzinfo=None, fold=0)
    fold: Incomplete ## <class 'property'> = <property>
    max: Incomplete ## <class 'time'> = datetime.time(microsecond=86399999999, tzinfo=None, fold=0)
    microsecond: Incomplete ## <class 'property'> = <property>
    @classmethod
    def fromisoformat(cls, *args, **kwargs) -> Incomplete:
        ...

    hour: Incomplete ## <class 'property'> = <property>
    def __init__(self, *argv, **kwargs) -> None:
        ...


class date():
    # inspect: arity=1
    def timetuple(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def toordinal(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def isoformat(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def isoweekday(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def weekday(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=4
    def replace(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def tuple(self, *args, **kwargs) -> Incomplete:
        ...

    @classmethod
    def today(cls, *args, **kwargs) -> Incomplete:
        ...

    resolution: Incomplete ## <class 'timedelta'> = datetime.timedelta(microseconds=86400000000)
    month: Incomplete ## <class 'property'> = <property>
    year: Incomplete ## <class 'property'> = <property>
    min: Incomplete ## <class 'date'> = datetime.date(0, 0, 1)
    @classmethod
    def fromtimestamp(cls, *args, **kwargs) -> Incomplete:
        ...

    max: Incomplete ## <class 'date'> = datetime.date(0, 0, 3652059)
    @classmethod
    def fromordinal(cls, *args, **kwargs) -> Incomplete:
        ...

    day: Incomplete ## <class 'property'> = <property>
    @classmethod
    def fromisoformat(cls, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

