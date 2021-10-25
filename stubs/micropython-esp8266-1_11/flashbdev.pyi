from typing import Any

class FlashBdev:
    NUM_BLK: int
    RESERVED_SECS: int
    SEC_SIZE: int
    START_SEC: int
    def ioctl() -> None: ...
    def readblocks() -> None: ...
    def writeblocks() -> None: ...

bdev: Any
esp: Any
size: int
