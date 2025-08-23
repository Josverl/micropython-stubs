from typing import Callable, Iterable, Tuple, TypeVar, Union

"""
Decorator to annotate objects with the MicroPython ports they are available on.

Usage:
    @mp_available("esp32")
    def foo(): ...

    @mp_available(["esp32", "rp2"])
    class Bar: ...
"""


__all__ = ["mp_available"]

T = TypeVar("T")  # Works for functions, classes, and other callables


# def _normalize_ports(ports: Union[str, Iterable[str]]) -> Tuple[str, ...]:
#     if isinstance(ports, str):
#         return (ports,)
#     try:
#         normalized = tuple(ports)  # type: ignore[arg-type]
#     except TypeError as e:
#         raise TypeError("ports must be a string or an iterable of strings") from e
#     if not all(isinstance(p, str) for p in normalized):
#         raise TypeError("all items in ports must be strings")
#     return normalized


def mp_available(ports: Union[str, Iterable[str]]  ) -> Callable[[T], T]:
    """
    Decorator factory that marks an object as available on the given MicroPython ports.
    The ports list is stored on the decorated object as __mp_available_ports__.
    """
    # allowed = _normalize_ports(ports)
    allowed = ports

    def decorator(obj: T) -> T:
        setattr(obj, "__mp_available_ports__", allowed)
        return obj

    return decorator