"""
Module: 'string' on micropython-v1.24.1-webassembly
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'webassembly', 'board': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

hexdigits: str = "0123456789abcdefABCDEF"
octdigits: str = "01234567"
printable: str = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c"
punctuation: str = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
whitespace: str = " \t\n\r\x0b\x0c"
digits: str = "0123456789"
ascii_letters: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ascii_lowercase: str = "abcdefghijklmnopqrstuvwxyz"
ascii_uppercase: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def translate(*args, **kwargs) -> Incomplete: ...
