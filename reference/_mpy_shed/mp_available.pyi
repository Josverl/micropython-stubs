from typing import Callable, Iterable, Tuple, TypeVar, Union

"""
Decorator to annotate objects with the MicroPython ports they are available on.

Usage:
    @mp_available(port="esp32")
    def foo(): ...

    @mp_available(port=["esp32", "rp2"])
    class Bar: ...
"""


__all__ = ["mp_available"]

T = TypeVar("T")  # Works for functions, classes, and other callables

def mp_available(
        *, 
        port: Union[str, Iterable[str]] =["*"], 
        version: Union[str, Iterable[str]] =["*"], 
        macro: Union[str, Iterable[str]] =["*"], 
    ) -> Callable[[T], T]:
    """
    Decorator factory that marks an object as available on the given MicroPython ports.
    The ports list is stored on the decorated object as __mp_available_ports__.
    """
    def decorator(obj: T) -> T:
        return obj
    return decorator

