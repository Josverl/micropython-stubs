from __future__ import annotations
from ubinascii import *
from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar

def unhexlify(data) -> bytes:
    """
    Convert hexadecimal data to binary representation. Returns bytes string.
    (i.e. inverse of hexlify)
    """
    ...

b2a_hex = hexlify
a2b_hex = unhexlify
PAD: str
table_a2b_base64: Incomplete

def _transform(n): ...
def a2b_base64(ascii) -> bytes:
    """Decode a line of base64 data."""

table_b2a_base64: str

def b2a_base64(bin, newline: bool = True) -> bytes:
    """Base64-code line of data."""
