"""
Module: 'inspect' on micropython-v1.29.0-webassembly-pyscript
"""

# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.29.0
from __future__ import annotations

from typing import Any, AsyncGenerator, Final, Generator

from _typeshed import Incomplete

# inspect: arity=1
def isclass(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def signature(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def iscoroutine(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def getmro(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def getsourcefile(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def getsource(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def ismethod(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def iscoroutinefunction(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def ismodule(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def isfunction(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def isgeneratorfunction(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def isgenerator(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def getargspec(*args, **kwargs) -> Incomplete: ...

# inspect: arity=2
def getmodule(*args, **kwargs) -> Incomplete: ...
def currentframe() -> Incomplete: ...

# inspect: arity=2
def getmembers(*args, **kwargs) -> Incomplete: ...

# inspect: arity=1
def getfile(*args, **kwargs) -> Incomplete: ...

# inspect: arity=2
def getframeinfo(*args, **kwargs) -> Incomplete: ...

class Signature:
    def __init__(self, *argv, **kwargs) -> None: ...

async def _g() -> Incomplete: ...

class _ct:
    def __init__(self, *argv, **kwargs) -> None: ...

class _Class:
    def meth(self) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

_Instance: Incomplete  ## <class '_Class'> = <_Class object at ...>
