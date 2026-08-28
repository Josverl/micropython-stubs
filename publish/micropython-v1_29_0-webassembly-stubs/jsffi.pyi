"""
Module: 'jsffi' on micropython-v1.29.0-webassembly-pyscript
"""

# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.28.6
from __future__ import annotations

from typing import Any, AsyncGenerator, Final, Generator

from _typeshed import Incomplete

def create_proxy(x0) -> Incomplete: ...
def mem_info() -> Incomplete: ...
def to_js(x0) -> Incomplete: ...

class JsProxy:
    def __init__(self, *argv, **kwargs) -> None: ...

class JsException(Exception): ...
