# Use UART 3 on a ItsyBitsy M4 board
from machine import UART, Pin

uart3 = UART(3,baudrate=115200)
uart3.write('hello')  # write 5 bytes
uart3.read(5)         # read up to 5 bytes

# uart = UART()         # Use the default values for id, rx and tx.
# uart = UART(baudrate=9600) # Use the default UART and set the baudrate

