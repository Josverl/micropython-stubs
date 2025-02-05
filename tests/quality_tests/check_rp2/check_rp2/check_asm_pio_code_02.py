# TODO: rp2.PIO - The functions defined in the asm_pio decorator are not recognized by pyright.
# ignore for now : other issues to solve first
"""
Sample from micropython discussions

# Generating Sinewaves with PIO block
# ref : https://github.com/orgs/micropython/discussions/16368
"""

# -----------------------------------------------
# add type hints for the rp2.PIO Instructions
try:
    from typing_extensions import TYPE_CHECKING
except ImportError:
    TYPE_CHECKING = False
if TYPE_CHECKING:
    from rp2.asm_pio import *
# -----------------------------------------------


import rp2
from machine import Pin
from utime import sleep



# preset pins as inputs, with pull resitors set up/down
Pin(0, Pin.IN, Pin.PULL_UP)
Pin(1, Pin.IN, Pin.PULL_DOWN)

# fmt: off 
# mypy: ignore-errors
@rp2.asm_pio(sideset_init=[rp2.PIO.IN_HIGH, rp2.PIO.IN_LOW],
         set_init=[rp2.PIO.IN_HIGH, rp2.PIO.IN_LOW])
def pio_sine():							# GPIO1, 		GPIO0
    set(pindirs, 0b11) .side(0b01)		# Low, 			High
    set(pindirs, 0b01) .side(0b01)		# In-pull Low, 	High
    set(pindirs, 0b11) .side(0b11)		# High, 		High
    set(pindirs, 0b01) .side(0b01)		# In-pull Low, 	High
    set(pindirs, 0b11) .side(0b01)		# Low,			High
    set(pindirs, 0b10) .side(0b00)		# Low,			In-Pull High
    set(pindirs, 0b11) .side(0b00)		# Low,			Low
    set(pindirs, 0b10) .side(0b00)		# Low,			In-Pull High


test_sm = rp2.StateMachine(0, pio_sine, freq=5000, sideset_base=Pin(0), set_base=Pin(0))
test_sm.active(1)

while True:
    sleep(10)