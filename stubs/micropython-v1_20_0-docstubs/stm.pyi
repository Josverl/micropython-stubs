from _typeshed import Incomplete as Incomplete
from typing import Tuple

mem8: bytearray
mem16: bytearray
mem32: bytearray
GPIOA: int
GPIOB: int
GPIO_BSRR: Incomplete
GPIO_IDR: Incomplete
GPIO_ODR: int

def rfcore_status() -> int:
    """
    Returns the status of the second CPU as an integer (the first word of device
    info table).
    """

def rfcore_fw_version(id) -> Tuple:
    """
    Get the version of the firmware running on the second CPU.  Pass in 0 for
    *id* to get the FUS version, and 1 to get the WS version.

    Returns a 5-tuple with the full version number.
    """

def rfcore_sys_hci(ogf, ocf, data, timeout_ms: int = ...) -> bytes:
    """
    Execute a HCI command on the SYS channel.  The execution is synchronous.

    Returns a bytes object with the result of the SYS command.
    """
