from _typeshed import Incomplete as Incomplete

INFO: int
CRITICAL: int
DEBUG: int
NOTSET: int
ERROR: int
WARNING: int

def critical(*args, **kwargs) -> Incomplete: ...
def basicConfig(*args, **kwargs) -> Incomplete: ...
def addLevelName(*args, **kwargs) -> Incomplete: ...
def warning(*args, **kwargs) -> Incomplete: ...
def info(*args, **kwargs) -> Incomplete: ...
def debug(*args, **kwargs) -> Incomplete: ...
def shutdown(*args, **kwargs) -> Incomplete: ...
def error(*args, **kwargs) -> Incomplete: ...
def getLogger(*args, **kwargs) -> Incomplete: ...
def exception(*args, **kwargs) -> Incomplete: ...
def log(*args, **kwargs) -> Incomplete: ...
def const(*args, **kwargs) -> Incomplete: ...

class StreamHandler:
    def emit(self, *args, **kwargs) -> Incomplete: ...
    def setFormatter(self, *args, **kwargs) -> Incomplete: ...
    def setLevel(self, *args, **kwargs) -> Incomplete: ...
    def format(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class LogRecord:
    def set(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Logger:
    def hasHandlers(self, *args, **kwargs) -> Incomplete: ...
    def warning(self, *args, **kwargs) -> Incomplete: ...
    def getEffectiveLevel(self, *args, **kwargs) -> Incomplete: ...
    def setLevel(self, *args, **kwargs) -> Incomplete: ...
    def info(self, *args, **kwargs) -> Incomplete: ...
    def isEnabledFor(self, *args, **kwargs) -> Incomplete: ...
    def addHandler(self, *args, **kwargs) -> Incomplete: ...
    def exception(self, *args, **kwargs) -> Incomplete: ...
    def log(self, *args, **kwargs) -> Incomplete: ...
    def error(self, *args, **kwargs) -> Incomplete: ...
    def critical(self, *args, **kwargs) -> Incomplete: ...
    def debug(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class FileHandler:
    def emit(self, *args, **kwargs) -> Incomplete: ...
    def setFormatter(self, *args, **kwargs) -> Incomplete: ...
    def setLevel(self, *args, **kwargs) -> Incomplete: ...
    def format(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Handler:
    def setLevel(self, *args, **kwargs) -> Incomplete: ...
    def setFormatter(self, *args, **kwargs) -> Incomplete: ...
    def format(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Formatter:
    def formatTime(self, *args, **kwargs) -> Incomplete: ...
    def usesTime(self, *args, **kwargs) -> Incomplete: ...
    def format(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
