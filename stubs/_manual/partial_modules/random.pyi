from typing import  runtime_checkable, Protocol, TypeVar

_T = TypeVar("_T")
@runtime_checkable
class Subscriptable(Protocol[_T]):
    """A `Protocol` (structurally typed) for an object that is subscriptable and of finite length."""

    __slots__ = ()
    def __len__(self) -> int:
        """Number of elements, normally called via `len(x)` where `x` is an object that implements this protocol."""
    def __getitem__(self, index: int) -> _T:
        """
        Element at the given index, 
        normally called via `x[index]` where `x` is an object that implements this protocol.
        """
