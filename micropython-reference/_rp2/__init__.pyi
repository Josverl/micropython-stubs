"""
Functionality specific to the RP2.

MicroPython module: https://docs.micropython.org/en/v1.23.0/library/rp2.html

The ``rp2`` module contains functions and classes specific to the RP2040, as
used in the Raspberry Pi Pico.

See the `RP2040 Python datasheet
<https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf>`_
for more information, and `pico-micropython-examples
<https://github.com/raspberrypi/pico-micropython-examples/tree/master/pio>`_
for example code.

"""

from __future__ import annotations

from rp2.DMA import DMA
from rp2.Flash import Flash
from rp2.PIO import PIO
from rp2.StateMachine import StateMachine
from rp2.PIOASMEmit import PIOASMEmit

from rp2 import bootsel_button
