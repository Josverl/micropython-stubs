from _typeshed import Incomplete
from micropython import const as const

_NAD_OFFSET: int
_PCB_OFFSET: int
_LEN_OFFSET: int
_INF_OFFSET: int
_I_BLOCK: int
_I_BLOCK_N: int
_I_BLOCK_M: int
_S_BLOCK: int
_S_BLOCK_REQ: int
_R_BLOCK: int
_R_BLOCK_N: int
_R_BLOCK_ERR: int
_RESYNC_REQ: int
_IFS_REQ: int
_ABORT_REQ: int
_WTX_REQ: int
_END_SESSION_REQ: int
_CHIP_RESET_REQ: int
_GET_ATR_REQ: int
_SOFT_RESET_REQ: int
_CLA_ISO7816: int
_INS_GP_SELECT: int
_STATE_IBLK: int
_STATE_SBLK: int
_STATE_SEND: int
_STATE_RECV: int
_STATE_WAIT: int
_STATE_WWTX: int
_STATE_DONE: int

def log_enabled(level): ...

class SmartCard:
    seq: int
    bus: Incomplete
    sad: Incomplete
    dad: Incomplete
    aid: Incomplete
    atr: Incomplete
    w_buf: Incomplete
    r_buf: Incomplete
    s_buf: Incomplete
    apdu_buf: Incomplete
    block_name: Incomplete
    state_name: Incomplete
    apdu_status: Incomplete
    def __init__(self, bus, nad, aid) -> None: ...
    def _block_type(self, pcb): ...
    def _block_size(self, buf): ...
    def _block_crc16(self, prologue, data, poly: int = 33800, crc: int = 65535): ...
    def _block_write(self, buf, delay: int = 0) -> None: ...
    def _block_print(self, txrx, *args) -> None: ...
    def _block_new(self, buf, btype, **kwargs): ...
    def _send_block(self, btype, arg, retry: int = 25, backoff: float = 1.2): ...
    def send_apdu(self, cla, ins, p1, p2, data: Incomplete | None = None, le: int = 0): ...
    def reset(self) -> None: ...
    def resync(self) -> None: ...
    def _parse_atrs(self, atr_bytes): ...
    def _dump_atrs(self, atr) -> None: ...
