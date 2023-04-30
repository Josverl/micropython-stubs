from _typeshed import Incomplete

_PAGE_SIZE: Incomplete
_CMD_WRITE: Incomplete
_CMD_READ: Incomplete
_CMD_RDSR: Incomplete
_CMD_WREN: Incomplete
_CMD_WRITE_32: Incomplete
_CMD_READ_32: Incomplete
_CMD_SEC_ERASE: Incomplete
_CMD_SEC_ERASE_32: Incomplete
_CMD_JEDEC_ID: Incomplete

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
