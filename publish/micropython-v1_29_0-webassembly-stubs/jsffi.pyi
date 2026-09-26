"""
Module: 'jsffi' on micropython-v1.29.0-webassembly-pyscript
"""

# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.29.0
from __future__ import annotations

from typing import Any, AsyncGenerator, Final, Generator

from _typeshed import Incomplete

# inspect: arity=1
def create_proxy(*args, **kwargs) -> Incomplete: ...
def mem_info() -> Incomplete: ...

# inspect: arity=1
def to_js(*args, **kwargs) -> Incomplete: ...

class JsProxy:
    def __init__(self, *argv, **kwargs) -> None: ...

class JsException(Exception): ...
