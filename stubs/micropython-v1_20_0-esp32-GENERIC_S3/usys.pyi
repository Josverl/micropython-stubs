from typing import Any

platform: str
version_info: tuple
path: list
version: str
ps1: str
ps2: str
byteorder: str
modules: dict
argv: list
implementation: tuple
maxsize: int

def print_exception(*args, **kwargs) -> Any: ...
def exit(*args, **kwargs) -> Any: ...

stderr: Any
stdout: Any
stdin: Any
