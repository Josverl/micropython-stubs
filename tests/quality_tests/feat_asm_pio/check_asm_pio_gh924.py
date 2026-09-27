# pyright: reportUntypedFunctionDecorator=error
"""
Sample from https://github.com/Josverl/micropython-stubs/issues/924

`@rp2.asm_pio(...)` must not obscure the type of the decorated function,
otherwise pyright reports reportUntypedFunctionDecorator.
"""

# mypy: ignore-errors

import rp2

# -----------------------------------------------
# add type hints for the rp2.PIO Instructions
try:
    from typing_extensions import TYPE_CHECKING
except ImportError:
    TYPE_CHECKING = False
if TYPE_CHECKING:
    from rp2.asm_pio import *
# -----------------------------------------------


@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)  # stubs-ignore: version<1.29.0
def blink_1hz():
    # fmt: off
    # Cycles: 1 + 1 + 6 + 32 * (30 + 1) = 1000
    irq(rel(0))
    set(pins, 1)
    set(x, 31)                [5]
    label("delay_high")
    nop()                     [29]
    jmp(x_dec, "delay_high")
    # Cycles: 1 + 1 + 6 + 32 * (30 + 1) = 1000
    nop()
    set(pins, 0)
    set(x, 31)                [5]
    label("delay_low")
    nop()                     [29]
    jmp(x_dec, "delay_low")
    # fmt: on
