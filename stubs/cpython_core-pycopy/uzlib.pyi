from zlib import *
from typing import Any, Union

class DecompIO:
    stream: Any
    decomp: Any
    pending: bytes
    def __init__(self, stream, dict_bits, dictbuf: Union[Any, None] = ...) -> None: ...
    def read(self, size) -> None: ...
