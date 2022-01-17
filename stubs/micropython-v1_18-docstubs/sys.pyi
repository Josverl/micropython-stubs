from typing import Any, Dict, List, Tuple

argv: List
byteorder: Any
implementation: Any
maxsize: int
modules: Dict
path: List
platform: Any
stderr: Any
stdin: Any
stdout: Any
version: str
version_info: Tuple

def exit(retval: int = ...) -> Any: ...
def atexit(func) -> Any: ...
def print_exception(exc, file=...) -> None: ...
def settrace(tracefunc) -> None: ...
