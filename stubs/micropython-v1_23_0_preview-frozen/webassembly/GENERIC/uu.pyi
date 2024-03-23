from _typeshed import Incomplete

class Error(Exception): ...

def encode(in_file, out_file, name: Incomplete | None = ..., mode: Incomplete | None = ...) -> None:
    """Uuencode file"""

def decode(in_file, out_file: Incomplete | None = ..., mode: Incomplete | None = ..., quiet: bool = ...) -> None:
    """Decode uuencoded file"""
