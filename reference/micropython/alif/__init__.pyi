""""MicroPython module for ALIF SoCs."""

from _mpy_shed import _BlockDeviceProtocol

usb_msc: int

def info() -> None: ...

class Flash(_BlockDeviceProtocol):
    def __init__(self, *, start: int = -1, len: int = -1) -> None: ...
    def ioctl(self, cmd: int, arg: int) -> int:
        ...
    def readblocks(self, block_num: int, buf: bytearray, offset: int) -> int:
        ...
    def writeblocks(self, block_num: int, buf: bytes, offset: int) -> int:
        ...

