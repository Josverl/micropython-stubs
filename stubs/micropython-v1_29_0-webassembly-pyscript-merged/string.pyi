"""
Module: 'string' on micropython-v1.29.0-webassembly-pyscript
"""

# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.28.6
from __future__ import annotations

from typing import Any, AsyncGenerator, Final, Generator

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

def translate(x0, x1) -> Incomplete: ...
