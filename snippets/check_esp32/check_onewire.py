from typing_extensions import assert_type
# OneWire driver
from machine import Pin
import onewire

ow = onewire.OneWire(Pin(12))  # create a OneWire bus on GPIO12
ow.scan()  # return a list of devices on the bus

ow.reset()  # reset the bus
ow.readbyte()  # read a byte
ow.writebyte(0x12)  # write a byte on the bus
ow.write(b"123")  # write bytes on the bus
ow.select_rom(b"12345678")  # select a specific device by its ROM code

assert_type(ow, onewire.OneWire)

# there was no onewire documatation before 1.19.1
# assert_type(ow.write(b"123"), None)
# assert_type(ow.select_rom(b"12345678"), None)

# assert_type(ow.scan(), list)
# assert_type(ow.reset(), None)
# assert_type(ow.readbyte(), int)
# assert_type(ow.writebyte(0x12), None)
