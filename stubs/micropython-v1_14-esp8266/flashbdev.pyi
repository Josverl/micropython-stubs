from typing import Any

bdev: Any

class FlashBdev:
    def __init__(self, *argv, **kwargs) -> None: ...
    def ioctl(self, *args, **kwargs) -> Any: ...
    def readblocks(self, *args, **kwargs) -> Any: ...
    def writeblocks(self, *args, **kwargs) -> Any: ...
    SEC_SIZE: int

size: int
start_sec: int
