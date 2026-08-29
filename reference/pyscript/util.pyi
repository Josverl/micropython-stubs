"""Utility API documented by PyScript 2026.7.3."""
# Copyright (c) 2020-2025 Jos Verlinde
# MIT Licensed

from typing import NoReturn

def as_bytearray(buffer: object) -> bytearray:
    """
    Given a JavaScript ArrayBuffer, convert it to a Python bytearray in a
    MicroPython friendly manner.
    """
    ...

class NotSupported:
    """
    Small helper that raises exceptions if you try to get/set any attribute on
    it.
    """

    def __init__(self, name: str, error: str) -> None: ...
    def __repr__(self) -> str: ...
    def __getattr__(self, attr: str) -> NoReturn: ...
    def __setattr__(self, attr: str, value: object) -> NoReturn: ...
    def __call__(self, *args: object) -> NoReturn: ...

def is_awaitable(obj: object) -> bool:
    """
    Returns a boolean indication if the passed in obj is an awaitable
    function. (MicroPython treats awaitables as generator functions, and if
    the object is a closure containing an async function we need to work
    carefully.)
    """
    ...
