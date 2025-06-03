from _typeshed import Incomplete
from micropython import const as const

_IOCTL_BLOCK_COUNT: int
_IOCTL_BLOCK_SIZE: int
_MBOOT_SPIFLASH_BASE_ADDR: int
_RAW_FILESYSTEM_ADDR: Incomplete
_RAW_FILESYSTEM_LEN: Incomplete

def _copy_file_to_raw_filesystem(filename, flash, block) -> None: ...
def update_app(filename) -> None: ...
