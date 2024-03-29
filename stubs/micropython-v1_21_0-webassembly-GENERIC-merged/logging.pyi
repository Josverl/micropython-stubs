from _typeshed import Incomplete as Incomplete

DEBUG: int
INFO: int
WARNING: int
CRITICAL: int
ERROR: int
NOTSET: int

def getLogger(*args, **kwargs) -> Incomplete: ...
def basicConfig(*args, **kwargs) -> Incomplete: ...
def info(*args, **kwargs) -> Incomplete: ...
def debug(*args, **kwargs) -> Incomplete: ...

class Logger:
    level: int
    def setLevel(self, *args, **kwargs) -> Incomplete: ...
    def exception(self, *args, **kwargs) -> Incomplete: ...
    def isEnabledFor(self, *args, **kwargs) -> Incomplete: ...
    def critical(self, *args, **kwargs) -> Incomplete: ...
    def info(self, *args, **kwargs) -> Incomplete: ...
    def log(self, *args, **kwargs) -> Incomplete: ...
    def warning(self, *args, **kwargs) -> Incomplete: ...
    def debug(self, *args, **kwargs) -> Incomplete: ...
    def error(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
