# Add MicroPython specific overloads to the core typing module
# No need to import from typing , as these will be inserted into the typing module itself
# type: ignore

class IO(Generic[AnyStr]):
    @abstractmethod
    @overload # write(bytes)
    def write(self, s: bytes, /) -> int: ...
