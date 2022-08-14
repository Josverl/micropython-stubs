from token import *
from collections.abc import Generator
from typing import Any

COMMENT: Any
NL: Any
ENCODING: Any

class TokenInfo:
    def __str__(self): ...

def get_indent(l): ...
def get_str(l, readline): ...
def tokenize(readline) -> Generator[Any, None, None]: ...
