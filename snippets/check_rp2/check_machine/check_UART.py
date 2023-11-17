# UART
from machine import UART, Pin

uart1 = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
uart1.write("hello")  # write 5 bytes
uart1.read(5)  # read up to 5 bytes
