from _typeshed import Incomplete
from micropython import const as const

_PAGE_SIZE: int
_CMD_WRITE: int
_CMD_READ: int
_CMD_RDSR: int
_CMD_WREN: int
_CMD_WRITE_32: int
_CMD_READ_32: int
_CMD_SEC_ERASE: int
_CMD_SEC_ERASE_32: int
_CMD_JEDEC_ID: int

class SPIFlash:
    spi: Incomplete
    cs: Incomplete
    id: Incomplete
    _READ: Incomplete
    _WRITE: Incomplete
    _ERASE: Incomplete
    def __init__(self, spi, cs) -> None: ...
    def _get_id(self): ...
    def _wait_wel1(self) -> None: ...
    def _wait_wip0(self) -> None: ...
    def _flash_modify(self, cmd, addr, buf) -> None: ...
    def erase_block(self, addr) -> None: ...
    def readinto(self, addr, buf) -> None: ...
    def write(self, addr, buf) -> None: ...
