from typing import Optional, Any
from _typeshed import Incomplete as Incomplete

def asm_pio_encode(instr, sideset_count, sideset_opt: bool = ...) -> Incomplete:
    """
    Assemble a single PIO instruction. You usually want to use `asm_pio()`
    instead.

    >>> rp2.asm_pio_encode("set(0, 1)", 0)
    57345
    """

def asm_pio(
    *,
    out_init: Incomplete | None = ...,
    set_init: Incomplete | None = ...,
    sideset_init: Incomplete | None = ...,
    in_shiftdir: int = ...,
    out_shiftdir: int = ...,
    autopush: bool = ...,
    autopull: bool = ...,
    push_thresh: int = ...,
    pull_thresh: int = ...,
    fifo_join=...,
) -> Incomplete:
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
    - *pull_thresh* is the threshold in bits before auto-push or conditional
      re-pushing is triggered.

    The remaining parameters are:

    - *autopush* configures whether auto-push is enabled.
    - *autopull* configures whether auto-pull is enabled.
    - *fifo_join* configures whether the 4-word TX and RX FIFOs should be
      combined into a single 8-word FIFO for one direction only. The options
      are `PIO.JOIN_NONE`, `PIO.JOIN_RX` and `PIO.JOIN_TX`.
    """

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
