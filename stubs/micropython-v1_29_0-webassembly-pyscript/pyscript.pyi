"""
Module: 'pyscript' on micropython-v1.29.0-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.28.6
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete

config: dict = {}
RUNNING_IN_WORKER: Final[bool] = False
def when(x0) -> Incomplete:
    ...

def fetch(x0) -> Incomplete:
    ...

def current_target() -> Incomplete:
    ...

def display(x0) -> Incomplete:
    ...


class Storage():
    def popitem(self) -> Incomplete:
        ...

    def pop(self, *args, **kwargs) -> Incomplete:
        ...

    def values(self) -> Incomplete:
        ...

    def setdefault(self, *args, **kwargs) -> Incomplete:
        ...

    def update(self, *args, **kwargs) -> Incomplete:
        ...

    def keys(self) -> Incomplete:
        ...

    def copy(self) -> Incomplete:
        ...

    def get(self, *args, **kwargs) -> Incomplete:
        ...

    def items(self) -> Incomplete:
        ...

    @classmethod
    def fromkeys(cls, *args, **kwargs) -> Incomplete:
        ...

    async def sync(self) -> Incomplete:
        ...

    def clear(self) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class WebSocket():
    OPEN: Final[int] = 1
    CLOSED: Final[int] = 3
    CLOSING: Final[int] = 2
    CONNECTING: Final[int] = 0
    def send(self, x1) -> Incomplete:
        ...

    def close(self) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

workers: Incomplete ## <class '_ReadOnlyProxy'> = <_ReadOnlyProxy object at ...>
async def create_named_worker(x0, x1, x2, x3) -> Incomplete:
    ...

@classmethod
def py_import(*args, **kwargs) -> Incomplete:
    ...

@classmethod
def PyWorker(*args, **kwargs) -> Incomplete:
    ...


class Event():
    def add_listener(self, x1) -> Incomplete:
        ...

    def remove_listener(self) -> Incomplete:
        ...

    def trigger(self, x1) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

sync: Incomplete ## <class 'NotSupported'> = <NotSupported pyscript.sync [pyscript.sync works only when running in a worker]>
async def storage(x0, x1) -> Incomplete:
    ...


class HTML():
    def _repr_html_(self) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

document: Incomplete ## <class 'JsProxy'> = <JsProxy nn>
js_modules: Incomplete ## <class 'JsProxy'> = <JsProxy nn>
@classmethod
def js_import(*args, **kwargs) -> Incomplete:
    ...

