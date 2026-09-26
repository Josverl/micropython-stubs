"""
Module: 'base64' on micropython-v1.29.0-webassembly-pyscript
"""

# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.29.0
from __future__ import annotations

from typing import Any, AsyncGenerator, Final, Generator

from _typeshed import Incomplete

MAXBINSIZE: Final[int] = 57
_b32tab: list = []
_b32rev: dict = {}
MAXLINESIZE: Final[int] = 76
_b32alphabet: dict = {}
bytes_types: tuple = ()

# inspect: arity=1
def decodestring(*args, **kwargs) -> Incomplete: ...

# inspect: arity=3
def b64decode(*args, **kwargs) -> Incomplete: ...

# inspect: arity=2
def b64encode(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def decodebytes(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def b32encode(*args, **kwargs) -> Incomplete: ...
def test() -> Incomplete: ...

# inspect: arity=1
def encodebytes(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def urlsafe_b64decode(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def encodestring(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def standard_b64encode(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def standard_b64decode(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def urlsafe_b64encode(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def _bytes_from_decode_data(*args, **kwargs) -> Incomplete: ...

# inspect: arity=2
def encode(*args, **kwargs) -> Incomplete: ...

# inspect: arity=2
def decode(*args, **kwargs) -> Incomplete: ...
def main() -> Incomplete: ...

# inspect: arity=3
def b32decode(*args, **kwargs) -> Incomplete: ...

# inspect: arity=2
def b16decode(*args, **kwargs) -> Incomplete: ...

# inspect: arity=2
def _maketrans(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def b16encode(*args, **kwargs) -> Incomplete: ...

# inspect: arity=2
def _translate(*args, **kwargs) -> Incomplete: ...
