from _typeshed import Incomplete

class FlashBdev:
    SEC_SIZE: int
    start_sec: Incomplete
    blocks: Incomplete
    def __init__(self, start_sec, blocks) -> None: ...
    def readblocks(self, n, buf, off: int = ...) -> None: ...
    def writeblocks(self, n, buf, off: Incomplete | None = ...) -> None: ...
    def ioctl(self, op, arg): ...

size: Incomplete
bdev: Incomplete
start_sec: Incomplete
