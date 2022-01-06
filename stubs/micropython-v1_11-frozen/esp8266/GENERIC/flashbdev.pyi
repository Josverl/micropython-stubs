from typing import Any

class FlashBdev:
    SEC_SIZE: int
    RESERVED_SECS: int
    START_SEC: Any
    NUM_BLK: Any
    blocks: Any
    def __init__(self, blocks=...) -> None: ...
    def readblocks(self, n, buf) -> None: ...
    def writeblocks(self, n, buf) -> None: ...
    def ioctl(self, op, arg): ...

size: Any
bdev: Any
