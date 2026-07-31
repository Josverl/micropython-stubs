# Add MicroPython specific overloads to the core typing module
# No need to import from typing , as these will be inserted into the typing module itself
# type: ignore

from _typeshed import ReadableBuffer, WriteableBuffer

class IO(Generic[AnyStr]):
    @abstractmethod
    @overload  # write(bytes)
    def write(self, s: bytes, /) -> int: ...
    @abstractmethod
    @overload
    def write(self: IO[bytes], buffer: ReadableBuffer, max_len: int, /) -> int | None: ...
    @abstractmethod
    @overload
    def write(self: IO[bytes], buffer: ReadableBuffer, offset: int, max_len: int, /) -> int | None: ...
    @abstractmethod
    def readinto(self: IO[bytes], buffer: WriteableBuffer, max_len: int = ..., /) -> int | None: ...
