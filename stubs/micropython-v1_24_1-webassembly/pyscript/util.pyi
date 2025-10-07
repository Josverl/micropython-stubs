"""
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/
"""

def as_bytearray(buffer) -> bytearray:
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

    def __init__(self, name, error) -> None: ...
    def __repr__(self) -> str: ...
    def __getattr__(self, attr): ...
    def __setattr__(self, attr, value): ...
    def __call__(self, *args): ...

def is_awaitable(obj) -> bool:
    """
    Returns a boolean indication if the passed in obj is an awaitable
    function. (MicroPython treats awaitables as generator functions, and if
    the object is a closure containing an async function we need to work
    carefully.)
    """
    ...
