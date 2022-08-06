from typing import Any

_PAGE_SIZE: Any
_CMD_WRITE: Any
_CMD_READ: Any
_CMD_RDSR: Any
_CMD_WREN: Any
_CMD_WRITE_32: Any
_CMD_READ_32: Any
_CMD_SEC_ERASE: Any
_CMD_SEC_ERASE_32: Any
_CMD_JEDEC_ID: Any

class SPIFlash:
    spi: Any
    cs: Any
    id: Any
    _READ: Any
    _WRITE: Any
    _ERASE: Any
    def __init__(self, spi, cs) -> None: ...
    def _get_id(self): ...
    def _wait_wel1(self) -> None: ...
    def _wait_wip0(self) -> None: ...
    def _flash_modify(self, cmd, addr, buf) -> None: ...
    def erase_block(self, addr) -> None: ...
    def readinto(self, addr, buf) -> None: ...
    def write(self, addr, buf) -> None: ...
