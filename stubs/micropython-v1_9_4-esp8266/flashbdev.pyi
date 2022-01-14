from typing import Any

class FlashBdev:
    NUM_BLK: int
    RESERVED_SECS: int
    SEC_SIZE: int
    START_SEC: int
    def ioctl(self, *argv) -> Any: ...
    def readblocks(self, *argv) -> Any: ...
    def writeblocks(self, *argv) -> Any: ...

bdev: Any
esp: Any
size: int
