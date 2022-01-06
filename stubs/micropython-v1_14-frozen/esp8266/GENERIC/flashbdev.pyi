from typing import Any

class FlashBdev:
    SEC_SIZE: int
    start_sec: Any
    blocks: Any
    def __init__(self, start_sec, blocks) -> None: ...
    def readblocks(self, n, buf, off: int = ...) -> None: ...
    def writeblocks(self, n, buf, off: Any | None = ...) -> None: ...
    def ioctl(self, op, arg): ...

size: Any
bdev: Any
start_sec: Any
