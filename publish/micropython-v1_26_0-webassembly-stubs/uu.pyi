__all__ = ["Error", "encode", "decode"]

class Error(Exception): ...

def encode(in_file, out_file, name=None, mode=None) -> None:
    """Uuencode file"""

def decode(in_file, out_file=None, mode=None, quiet: bool = False) -> None:
    """Decode uuencoded file"""
