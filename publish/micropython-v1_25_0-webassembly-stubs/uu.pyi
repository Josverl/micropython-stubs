from _typeshed import Incomplete

__all__ = ["Error", "encode", "decode"]

class Error(Exception): ...

def encode(in_file, out_file, name: Incomplete | None = None, mode: Incomplete | None = None) -> None:
    """Uuencode file"""

def decode(in_file, out_file: Incomplete | None = None, mode: Incomplete | None = None, quiet: bool = False) -> None:
    """Decode uuencoded file"""
