"""
Functionality specific to the RP2.

MicroPython module: https://docs.micropython.org/en/v1.24.0/library/rp2.html

The ``rp2`` module contains functions and classes specific to the RP2040, as
used in the Raspberry Pi Pico.

See the `RP2040 Python datasheet
<https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf>`_
for more information, and `pico-micropython-examples
<https://github.com/raspberrypi/pico-micropython-examples/tree/master/pio>`_
for example code.
"""

# source version: v1.24.0
# origin module:: repos/micropython/docs/library/rp2.rst
# 2024 - Jos Verlinde - PIO additions

from __future__ import annotations

from typing import Callable, Dict, List, Union, overload
from _typeshed import Incomplete
from typing_extensions import TypeAlias

from rp2.PIO import PIO
from rp2.PIOASMEmit import PIOASMEmit
from machine import Pin

_PIO_ASM_Program: TypeAlias = PIOASMEmit

class PIOASMError(Exception):
    """
    This exception is raised from `asm_pio()` or `asm_pio_encode()` if there is
    an error assembling a PIO program.
    """

def asm_pio(
    *,
    out_init: Union[Pin, List[Pin], int, List[int], None] = None,
    set_init: Union[Pin, List[Pin], int, List[int], None] = None,
    sideset_init: Union[Pin, List[Pin], int, List[int], None] = None,
    side_pindir: bool = False,
    in_shiftdir=0,
    out_shiftdir=0,
    autopush=False,
    autopull=False,
    push_thresh=32,
    pull_thresh=32,
    fifo_join=PIO.JOIN_NONE,
) -> Callable[..., _PIO_ASM_Program]:
    """
    Assemble a PIO program.

    The following parameters control the initial state of the GPIO pins, as one
    of `PIO.IN_LOW`, `PIO.IN_HIGH`, `PIO.OUT_LOW` or `PIO.OUT_HIGH`. If the
    program uses more than one pin, provide a tuple, e.g.
    ``out_init=(PIO.OUT_LOW, PIO.OUT_LOW)``.

    - *out_init* configures the pins used for ``out()`` instructions.
    - *set_init* configures the pins used for ``set()`` instructions. There can
      be at most 5.
    - *sideset_init* configures the pins used for ``.side()`` modifiers. There
      can be at most 5.
    - *side_pindir* when set to ``True`` configures ``.side()`` modifiers to be
      used for pin directions, instead of pin values (the default, when ``False``).

    The following parameters are used by default, but can be overridden in
    `StateMachine.init()`:

    - *in_shiftdir* is the default direction the ISR will shift, either
      `PIO.SHIFT_LEFT` or `PIO.SHIFT_RIGHT`.
    - *out_shiftdir* is the default direction the OSR will shift, either
      `PIO.SHIFT_LEFT` or `PIO.SHIFT_RIGHT`.
    - *push_thresh* is the threshold in bits before auto-push or conditional
      re-pushing is triggered.
    - *pull_thresh* is the threshold in bits before auto-pull or conditional
      re-pulling is triggered.

    The remaining parameters are:

    - *autopush* configures whether auto-push is enabled.
    - *autopull* configures whether auto-pull is enabled.
    - *fifo_join* configures whether the 4-word TX and RX FIFOs should be
      combined into a single 8-word FIFO for one direction only. The options
      are `PIO.JOIN_NONE`, `PIO.JOIN_RX` and `PIO.JOIN_TX`.
    """
    ...

def asm_pio_encode(instr, sideset_count, sideset_opt=False) -> int:
    """
    Assemble a single PIO instruction. You usually want to use `asm_pio()`
    instead.

    >>> rp2.asm_pio_encode("set(0, 1)", 0)
    57345
    """
    ...

def bootsel_button() -> int:
    # actually defined in _rp2
    """
    Temporarily turns the QSPI_SS pin into an input and reads its value,
    returning 1 for low and 0 for high.
    On a typical RP2040 board with a BOOTSEL button, a return value of 1
    indicates that the button is pressed.

    Since this function temporarily disables access to the external flash
    memory, it also temporarily disables interrupts and the other core to
    prevent them from trying to execute code from flash.
    """
    ...
