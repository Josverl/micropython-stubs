
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class FlashBdev:
    def __init__(self, blocks: Any=NUM_BLK) -> None: ...
    def readblocks(self, n: int, buf: Any, off: Any=) -> None: ...
    def writeblocks(self, n: int, buf: Any, off: Any=) -> None: ...
    def ioctl(self, op: Any, arg: Any) -> Optional[Any]: ...
        #   0: return self.blocks
        # ? 0: return self.blocks
        #   1: return self.SEC_SIZE
        # ? 1: return self.SEC_SIZE
        #   2: return
        #   2: return
