from typing import Any

def debug(*args, **kwargs) -> Any: ...
def info(*args, **kwargs) -> Any: ...
def getLogger(*args, **kwargs) -> Any: ...
def basicConfig(*args, **kwargs) -> Any: ...

INFO: int
CRITICAL: int
ERROR: int
WARNING: int
DEBUG: int
NOTSET: int

class Logger:
    def __init__(self, *argv, **kwargs) -> None: ...
    def debug(self, *args, **kwargs) -> Any: ...
    def info(self, *args, **kwargs) -> Any: ...
    def log(self, *args, **kwargs) -> Any: ...
    def exception(self, *args, **kwargs) -> Any: ...
    def error(self, *args, **kwargs) -> Any: ...
    def warning(self, *args, **kwargs) -> Any: ...
    level: int
    def setLevel(self, *args, **kwargs) -> Any: ...
    def isEnabledFor(self, *args, **kwargs) -> Any: ...
    def critical(self, *args, **kwargs) -> Any: ...
