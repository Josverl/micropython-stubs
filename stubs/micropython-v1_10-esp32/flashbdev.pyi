from typing import Any

bdev: Any
size: int

class FlashBdev:
    def __init__(self, *argv, **kwargs) -> None: ...
    def ioctl(self, *args, **kwargs) -> Any: ...
    def readblocks(self, *args, **kwargs) -> Any: ...
    def writeblocks(self, *args, **kwargs) -> Any: ...
    SEC_SIZE: int
    START_SEC: int
