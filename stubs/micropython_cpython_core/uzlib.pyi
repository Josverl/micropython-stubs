from zlib import *
from typing import Any

class DecompIO:
    stream: Any
    decomp: Any
    pending: bytes
    def __init__(self, stream, dict_bits, dictbuf: Any | None = ...) -> None: ...
    def read(self, size): ...
