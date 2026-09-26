"""
Module: 'pyscript.__init__' on micropython-v1.29.0-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.29.0
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete

config: dict = {}
RUNNING_IN_WORKER: Final[bool] = False
# inspect: arity=1
def display(*args, **kwargs) -> Incomplete:
    ...

def current_target() -> Incomplete:
    ...

# inspect: arity=1
def fetch(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def when(*args, **kwargs) -> Incomplete:
    ...

workers: Incomplete ## <class '_ReadOnlyProxy'> = <_ReadOnlyProxy object at ...>

class HTML():
    # inspect: arity=1
    def _repr_html_(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Storage():
    # inspect: arity=1
    def popitem(self, *args, **kwargs) -> Incomplete:
        ...

    def pop(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def values(self, *args, **kwargs) -> Incomplete:
        ...

    def setdefault(self, *args, **kwargs) -> Incomplete:
        ...

    def update(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def keys(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def copy(self, *args, **kwargs) -> Incomplete:
        ...

    def get(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def items(self, *args, **kwargs) -> Incomplete:
        ...

    @classmethod
    def fromkeys(cls, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    async def sync(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def clear(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

# inspect: arity=2
async def storage(*args, **kwargs) -> Incomplete:
    ...


class WebSocket():
    OPEN: Final[int] = 1
    CLOSED: Final[int] = 3
    CLOSING: Final[int] = 2
    CONNECTING: Final[int] = 0
    # inspect: arity=2
    def send(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

# inspect: arity=4
async def create_named_worker(*args, **kwargs) -> Incomplete:
    ...

@classmethod
def py_import(*args, **kwargs) -> Incomplete:
    ...


class Event():
    # inspect: arity=2
    def add_listener(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def remove_listener(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def trigger(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

sync: Incomplete ## <class 'NotSupported'> = <NotSupported pyscript.sync [pyscript.sync works only when running in a worker]>
@classmethod
def PyWorker(*args, **kwargs) -> Incomplete:
    ...

js_modules: Incomplete ## <class 'JsProxy'> = <JsProxy nn>
@classmethod
def js_import(*args, **kwargs) -> Incomplete:
    ...

document: Incomplete ## <class 'JsProxy'> = <JsProxy nn>
