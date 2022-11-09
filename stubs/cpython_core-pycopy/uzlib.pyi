# CPython core - pycopy
from typing import Any, Union
from zlib import *

class DecompIO:
    stream: Any
    decomp: Any
    pending: bytes

    def __init__(self, stream, dict_bits, dictbuf: Union[Any, None] = ...) -> None: ...
    def read(self, size) -> None: ...
