from typing import Any

bdev: Any

class Partition:
    RUNNING: int
    TYPE_APP: int
    TYPE_DATA: int
    BOOT: int
    def readblocks(self, *args, **kwargs) -> Any: ...
    def ioctl(self, *args, **kwargs) -> Any: ...
    def set_boot(self, *args, **kwargs) -> Any: ...
    def writeblocks(self, *args, **kwargs) -> Any: ...
    def info(self, *args, **kwargs) -> Any: ...
    def find(self, *args, **kwargs) -> Any: ...
    def get_next_update(self, *args, **kwargs) -> Any: ...
    @classmethod
    def mark_app_valid_cancel_rollback(cls, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...