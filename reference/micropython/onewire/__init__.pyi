from typing import List
from machine import Pin

from _typeshed import Incomplete

class OneWireError(Exception): ...

class OneWire:
    SEARCH_ROM: int = 0xF0
    MATCH_ROM: int = 0x55
    SKIP_ROM: int = 0xCC
    pin: Pin
    def __init__(self, pin: Pin) -> None:
        """
        The OneWire driver is implemented in software and works on all pins.
        The 1-wire bus is a serial bus that uses just a single wire for communication
        (in addition to wires for ground and power).
        Be sure to put a 4.7k pull-up resistor on the data line.
        """
        ...

    def scan(self) -> List[Incomplete]:
        """Return a list of devices on the bus."""
        ...

    def reset(self, required: bool = False):
        """Reset the bus."""
        ...

    def readbyte(self) -> Incomplete:
        """Read a byte from the bus."""
        ...

    def readbit(self) -> Incomplete:
        """Read a bit from the bus."""
        ...

    def readinto(self, buf: Incomplete) -> None:
        """"""
        ...

    def writebyte(self, value: Incomplete):
        """Write a byte on the bus."""
        ...

    def writebit(self, value: Incomplete):
        """Write a bit on the bus."""
        ...

    def write(self, buf: Incomplete) -> None:
        """Write a buffer on the bus."""
        ...

    def select_rom(self, rom: Incomplete) -> None:
        """ "Select a specific device by its ROM code."""
        ...

    def crc8(self, data: Incomplete) -> Incomplete: ...
    def _search_rom(self, l_rom, diff): ...
