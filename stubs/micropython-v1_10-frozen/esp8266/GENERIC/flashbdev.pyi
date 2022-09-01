from _typeshed import Incomplete

class FlashBdev:
    SEC_SIZE: int
    RESERVED_SECS: int
    START_SEC: Incomplete
    NUM_BLK: Incomplete
    blocks: Incomplete
    def __init__(self, blocks=...) -> None: ...
    def readblocks(self, n, buf) -> None: ...
    def writeblocks(self, n, buf) -> None: ...
    def ioctl(self, op, arg): ...

size: Incomplete
bdev: Incomplete
