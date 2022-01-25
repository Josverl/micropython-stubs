from typing import Any, Optional

class DiskAccess:
    def __init__(self, disk_name) -> None: ...
    def readblocks(self, block_num, buf, offset: Optional[int]) -> Any: ...
    def writeblocks(self, block_num, buf, offset: Optional[int]) -> Any: ...
    def ioctl(self, cmd, arg) -> Any: ...

class FlashArea:
    def __init__(self, id, block_size) -> None: ...
    def readblocks(self, block_num, buf, offset: Optional[int]) -> Any: ...
    def writeblocks(self, block_num, buf, offset: Optional[int]) -> Any: ...
    def ioctl(self, cmd, arg) -> Any: ...

def is_preempt_thread() -> Any: ...
def current_tid() -> Any: ...
def thread_analyze() -> Any: ...
def shell_exec(cmd_in) -> Any: ...