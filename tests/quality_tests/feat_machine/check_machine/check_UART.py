from typing import Union

from machine import UART, Pin
from typing_extensions import assert_type

uart = UART(0, 115200)
uart = UART(0, baudrate=115200, timeout=10, tx=Pin(0), rx=Pin(1))

buffer = bytearray(10)

u = UART(0, 115200)

assert_type(u.readline(), Union[str,None]) # stubs-ignore : skip version < 1.21.0

assert_type(u.readinto(buffer), Union[int,None]) # stubs-ignore : skip version < 1.21.0
assert_type(u.write(buffer), Union[int,None]) # stubs-ignore : skip version < 1.21.0

