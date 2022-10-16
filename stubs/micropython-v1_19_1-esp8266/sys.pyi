from typing import Any

path: list
modules: dict
version_info: tuple
platform: str
version: str
byteorder: str
argv: list
maxsize: int
implementation: tuple

def exit(*args, **kwargs) -> Any: ...
def print_exception(*args, **kwargs) -> Any: ...

stderr: Any
stdout: Any
stdin: Any
