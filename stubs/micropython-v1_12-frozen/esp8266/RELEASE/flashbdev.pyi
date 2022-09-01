from _typeshed import Incomplete

class FlashBdev:
    SEC_SIZE: int
    RESERVED_SECS: int
    START_SEC: Incomplete
    NUM_BLK: Incomplete
    blocks: Incomplete
    def __init__(self, blocks=...) -> None: ...
    def readblocks(self, n, buf, off: int = ...) -> None: ...
    def writeblocks(self, n, buf, off: Incomplete | None = ...) -> None: ...
    def ioctl(self, op, arg): ...

size: Incomplete
bdev: Incomplete
