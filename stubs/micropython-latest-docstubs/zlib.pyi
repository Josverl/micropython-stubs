import abc
from typing import IO

class DecompIO(IO, metaclass=abc.ABCMeta):
    def __init__(self, stream, wbits: int = ...) -> None: ...

def decompress(data, wbits: int = ..., bufsize: int = ...) -> bytes: ...
