"""
functionality specific to the RP2. See: https://docs.micropython.org/en/latest/library/rp2.html

The ``rp2`` module contains functions and classes specific to the RP2040, as
used in the Raspberry Pi Pico.

See the `RP2040 Python datasheet
<https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf>`_
for more information, and `pico-micropython-examples
<https://github.com/raspberrypi/pico-micropython-examples/tree/master/pio>`_
for example code.

"""
from typing import Optional, Any

def asm_pio_encode(instr, sideset_count, sideset_opt=False) -> Any:
    """
    Assemble a single PIO instruction. You usually want to use `asm_pio()`
    instead.

    >>> rp2.asm_pio_encode("set(0, 1)", 0)
    57345
    """
    ...

def asm_pio(
    *,
    out_init=None,
    set_init=None,
    sideset_init=None,
    in_shiftdir=0,
    out_shiftdir=0,
    autopush=False,
    autopull=False,
    push_thresh=32,
    pull_thresh=32,
    fifo_join=PIO.JOIN_NONE,
) -> Any:
    """
    Assemble a PIO program.

    The following parameters control the initial state of the GPIO pins, as one
    of `PIO.IN_LOW`, `PIO.IN_HIGH`, `PIO.OUT_LOW` or `PIO.OUT_HIGH`. If the
    program uses more than one pin, provide a tuple, e.g.
    ``out_init=(PIO.OUT_LOW, PIO.OUT_LOW)``.

    - *out_init* configures the pins used for ``out()`` instructions.
    - *set_init* configures the pins used for ``set()`` instructions. There can
      be at most 5.
    - *sideset_init* configures the pins used side-setting. There can be at
      most 5.

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

def dht_readinto(*args, **kwargs) -> Any: ...
def const(*args, **kwargs) -> Any: ...

class PIOASMEmit:
    def wrap(self, *args, **kwargs) -> Any: ...
    def wait(self, *args, **kwargs) -> Any: ...
    def jmp(self, *args, **kwargs) -> Any: ...
    def word(self, *args, **kwargs) -> Any: ...
    def in_(self, *args, **kwargs) -> Any: ...
    def delay(self, *args, **kwargs) -> Any: ...
    def start_pass(self, *args, **kwargs) -> Any: ...
    def out(self, *args, **kwargs) -> Any: ...
    def side(self, *args, **kwargs) -> Any: ...
    def wrap_target(self, *args, **kwargs) -> Any: ...
    def label(self, *args, **kwargs) -> Any: ...
    def irq(self, *args, **kwargs) -> Any: ...
    def set(self, *args, **kwargs) -> Any: ...
    def mov(self, *args, **kwargs) -> Any: ...
    def push(self, *args, **kwargs) -> Any: ...
    def pull(self, *args, **kwargs) -> Any: ...
    def nop(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class PIOASMError(Exception): ...
