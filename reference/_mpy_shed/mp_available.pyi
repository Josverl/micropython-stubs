from typing import Callable, Iterable, TypeVar, Union, overload

"""
Decorator to annotate objects with the MicroPython ports they are available on.

Usage:
    @mp_available(port="esp32")
    def foo(): ...

    @mp_available
    def baz(): ...

    @mp_available(port=["esp32", "rp2"])
    class Bar: ...
"""


__all__ = ["mp_available"]

T = TypeVar("T")  # Works for functions, classes, and other callables

@overload
def mp_available(__obj: T) -> T: ...


@overload
def mp_available(
        *,
        port: Union[str, Iterable[str]] = "*",
        version: Union[str, Iterable[str]] = "*",
        macro: Union[str, Iterable[str]] = "*",
    ) -> Callable[[T], T]:
    ...


def mp_available(
        __obj: Union[T, None] = None,
        *,
        port: Union[str, Iterable[str]] = "*",
        version: Union[str, Iterable[str]] = "*",
        macro: Union[str, Iterable[str]] = "*",
    ) -> Union[T, Callable[[T], T]]:
    """Transparent decorator for static type checking.

    Supports both styles:
    - @mp_available
    - @mp_available(...)
    """
    def decorator(obj: T) -> T:
        return obj
    if __obj is None:
        return decorator
    return __obj

