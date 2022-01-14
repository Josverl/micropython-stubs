from typing import Any

class FlashBdev:
    NUM_BLK: int
    RESERVED_SECS: int
    SEC_SIZE: int
    START_SEC: int
    def ioctl(self, *args) -> Any: ...
    def readblocks(self, *args) -> Any: ...
    def writeblocks(self, *args) -> Any: ...

bdev: Any
esp: Any
size: int
