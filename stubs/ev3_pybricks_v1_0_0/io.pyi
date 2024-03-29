from typing import Any

class BytesIO:
    def close(self, *argv) -> Any: ...
    def flush(self, *argv) -> Any: ...
    def getvalue(self, *argv) -> Any: ...
    def read(self, *argv) -> Any: ...
    def readinto(self, *argv) -> Any: ...
    def readline(self, *argv) -> Any: ...
    def seek(self, *argv) -> Any: ...
    def write(self, *argv) -> Any: ...

class FileIO:
    def close(self, *argv) -> Any: ...
    def fileno(self, *argv) -> Any: ...
    def flush(self, *argv) -> Any: ...
    def read(self, *argv) -> Any: ...
    def readinto(self, *argv) -> Any: ...
    def readline(self, *argv) -> Any: ...
    def readlines(self, *argv) -> Any: ...
    def seek(self, *argv) -> Any: ...
    def tell(self, *argv) -> Any: ...
    def write(self, *argv) -> Any: ...

class IOBase: ...

SEEK_CUR: int
SEEK_END: int
SEEK_SET: int

class StringIO:
    def close(self, *argv) -> Any: ...
    def flush(self, *argv) -> Any: ...
    def getvalue(self, *argv) -> Any: ...
    def read(self, *argv) -> Any: ...
    def readinto(self, *argv) -> Any: ...
    def readline(self, *argv) -> Any: ...
    def seek(self, *argv) -> Any: ...
    def write(self, *argv) -> Any: ...

class TextIOWrapper:
    def close(self, *argv) -> Any: ...
    def fileno(self, *argv) -> Any: ...
    def flush(self, *argv) -> Any: ...
    def read(self, *argv) -> Any: ...
    def readinto(self, *argv) -> Any: ...
    def readline(self, *argv) -> Any: ...
    def readlines(self, *argv) -> Any: ...
    def seek(self, *argv) -> Any: ...
    def tell(self, *argv) -> Any: ...
    def write(self, *argv) -> Any: ...

def open() -> None: ...
