"""Example typed Micropython module."""
from typing import TYPE_CHECKING, Tuple


def foo(a: int, b: int) -> Tuple[int, str]:
    return a, str(b)

print("Hello, typed world!")
print(f"{foo(1, 2)=}")
