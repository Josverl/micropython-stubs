from typing import Union

from machine import UART, Pin
from typing_extensions import assert_type


uart_1 = UART(0, 115200)
uart_1.write("hello")  # write 5 bytes
uart_1.read(5)  # read up to 5 bytes



# baudrate is positional only
uart_2 = UART(0, 115200, timeout=10, tx=Pin(0), rx=Pin(1))

buffer = bytearray(10)


assert_type(uart_2.readline(), Union[str, None])  # stubs-ignore : skip version < 1.21.0

assert_type(uart_2.readinto(buffer), Union[int, None])  # stubs-ignore : skip version < 1.21.0
assert_type(uart_2.write(buffer), Union[int, None])  # stubs-ignore : skip version < 1.21.0




