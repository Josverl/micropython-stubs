from typing import Any

ACCESS_COPY: int
ACCESS_READ: int
ACCESS_WRITE: int
MAP_PRIVATE: int
MAP_SHARED: int
PROT_EXEC: int
PROT_READ: int
PROT_WRITE: int

class mmap:
    def close(self, *argv) -> Any: ...
    def read(self, *argv) -> Any: ...
    def seek(self, *argv) -> Any: ...
    def write(self, *argv) -> Any: ...
