from typing import Any


class _MemoryObject():
    """
    A memory object.  This is a wrapper around a memory region.  It can be used
    to access the memory region as if it were an array of bytes.

    These memory objects can be used in combination with the peripheral register
    constants to read and write registers of the MCU hardware peripherals, as well
    as all other areas of address space.
    """

    def __getitem__(self, key: int) -> Any:
        ...
    def __setitem__(self, key: int, value: Any) -> None:
        ...


__all__ = [
    "_MemoryObject",
]
