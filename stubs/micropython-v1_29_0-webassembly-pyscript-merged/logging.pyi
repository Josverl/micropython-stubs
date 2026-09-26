"""
Module: 'logging' on micropython-v1.29.0-webassembly-pyscript
"""

# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.29.0
from __future__ import annotations

from typing import Any, AsyncGenerator, Final, Generator

from _typeshed import Incomplete

_loggers: dict = {}
NOTSET: Final[int] = 0
INFO: Final[int] = 20
ERROR: Final[int] = 40
_default_datefmt: str = "%Y-%m-%d %H:%M:%S"
_level_dict: dict = {}
WARNING: Final[int] = 30
_default_fmt: str = "%(levelname)s:%(name)s:%(message)s"
DEBUG: Final[int] = 10
CRITICAL: Final[int] = 50

# inspect: arity=2
def exception(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def getLogger(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def info(*args, **kwargs) -> Incomplete: ...
def shutdown() -> Incomplete: ...

# inspect: arity=1
def critical(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def error(*args, **kwargs) -> Incomplete: ...

# inspect: arity=4
def basicConfig(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def debug(*args, **kwargs) -> Incomplete: ...

# inspect: arity=2
def addLevelName(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def warning(*args, **kwargs) -> Incomplete: ...

# inspect: arity=2
def log(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def const(*args, **kwargs) -> Incomplete: ...

class StreamHandler:
    # inspect: arity=2
    def emit(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=2
    def setFormatter(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=2
    def setLevel(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=2
    def format(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=1
    def close(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

_stream: Incomplete  ## <class 'TextIOWrapper'> = <io.TextIOWrapper 2>

class FileHandler:
    # inspect: arity=2
    def emit(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=2
    def setFormatter(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=2
    def setLevel(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=2
    def format(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=1
    def close(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Logger:
    # inspect: arity=1
    def hasHandlers(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=2
    def warning(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=1
    def getEffectiveLevel(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=2
    def setLevel(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=2
    def info(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=2
    def isEnabledFor(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=2
    def addHandler(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=3
    def exception(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=3
    def log(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=2
    def error(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=2
    def critical(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=2
    def debug(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Formatter:
    # inspect: arity=3
    def formatTime(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=1
    def usesTime(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=2
    def format(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class LogRecord:
    # inspect: arity=4
    def set(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Handler:
    # inspect: arity=2
    def setLevel(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=2
    def setFormatter(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=2
    def format(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=1
    def close(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
