from token import *
from collections.abc import Generator
from typing import Any

COMMENT: Any
NL: Any
ENCODING: Any

class TokenInfo:
    def __str__(self) -> None: ...

def get_indent(l) -> None: ...
def get_str(l, readline) -> None: ...
def tokenize(readline) -> Generator[Any, None, None]: ...
