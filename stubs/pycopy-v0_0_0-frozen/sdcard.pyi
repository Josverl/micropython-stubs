from typing import Any

_CMD_TIMEOUT: Any
_R1_IDLE_STATE: Any
_R1_ILLEGAL_COMMAND: Any
_TOKEN_CMD25: Any
_TOKEN_STOP_TRAN: Any
_TOKEN_DATA: Any

class SDCard:
    spi: Any
    cs: Any
    cmdbuf: Any
    dummybuf: Any
    tokenbuf: Any
    dummybuf_memoryview: Any
    def __init__(self, spi, cs) -> None: ...
    def init_spi(self, baudrate) -> None: ...
    sectors: Any
    def init_card(self) -> None: ...
    cdv: int
    def init_card_v1(self) -> None: ...
    def init_card_v2(self) -> None: ...
    def cmd(self, cmd, arg, crc, final: int = ..., release: bool = ..., skip1: bool = ...): ...
    def readinto(self, buf) -> None: ...
    def write(self, token, buf) -> None: ...
    def write_token(self, token) -> None: ...
    def readblocks(self, block_num, buf) -> None: ...
    def writeblocks(self, block_num, buf) -> None: ...
    def ioctl(self, op, arg): ...
