from _typeshed import Incomplete
from micropython import const as const

VFS_FAT: int
VFS_LFS1: int
VFS_LFS2: int
VFS_RAW: int
_ELEM_TYPE_END: int
_ELEM_TYPE_MOUNT: int
_ELEM_TYPE_FSLOAD: int
_ELEM_TYPE_STATUS: int

def check_mem_contains(addr, buf): ...
def dfu_read(filename): ...

class Flash:
    _FLASH_KEY1: int
    _FLASH_KEY2: int
    addressof: Incomplete
    _keyr: Incomplete
    _sr: Incomplete
    _sr_busy: Incomplete
    _cr: Incomplete
    _cr_lock: Incomplete
    _cr_init_erase: Incomplete
    _cr_start_erase: Incomplete
    _cr_init_write: Incomplete
    _cr_flush: Incomplete
    _write_multiple: int
    sector0_size: Incomplete
    def __init__(self) -> None: ...
    def wait_not_busy(self) -> None: ...
    def unlock(self) -> None: ...
    def lock(self) -> None: ...
    def erase_sector(self, sector) -> None: ...
    def write(self, addr, buf) -> None: ...

def update_mboot(filename) -> None: ...
def _create_element(kind, body): ...
def update_app_elements(
    filename,
    fs_base,
    fs_len,
    fs_type=...,
    fs_blocksize: int = 0,
    status_addr: Incomplete | None = None,
    addr_64bit: bool = False,
    *,
    fs_base2: int = 0,
    fs_len2: int = 0,
): ...
def update_mpy(*args, **kwargs) -> None: ...
def get_mboot_version(
    mboot_base: int = 134217728, mboot_len: int = 32768, mboot_ver_len: int = 64, valid_prefix: str = "mboot-", include_opts: bool = True
): ...
