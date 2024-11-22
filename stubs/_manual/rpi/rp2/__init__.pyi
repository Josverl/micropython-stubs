"""
Functionality specific to the RP2.

MicroPython module: https://docs.micropython.org/en/v1.21.0/library/rp2.html

The ``rp2`` module contains functions and classes specific to the RP2040, as
used in the Raspberry Pi Pico.

See the `RP2040 Python datasheet
<https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf>`_
for more information, and `pico-micropython-examples
<https://github.com/raspberrypi/pico-micropython-examples/tree/master/pio>`_
for example code.
"""

from typing import Any, Callable, Dict, Final, List, Union

from _rp2 import PIO
from _typeshed import Incomplete
from machine import Pin  # type: ignore
from typing import List

_PROG_DATA: Final[int] = 0
_PROG_OFFSET_PIO0: Final[int] = 1
_PROG_OFFSET_PIO1: Final[int] = 2
_PROG_EXECCTRL: Final[int] = 3
_PROG_SHIFTCTRL: Final[int] = 4
_PROG_OUT_PINS: Final[int] = 5
_PROG_SET_PINS: Final[int] = 6
_PROG_SIDESET_PINS: Final[int] = 7
_PROG_MAX_FIELDS: Final[int] = 8

class PIOASMError(Exception): ...

class PIOASMEmit:
    """
    The PIOASMEmit class provides a comprehensive interface for constructing PIO programs,
    handling the intricacies of instruction encoding, label management, and program state.
    This allows users to build complex PIO programs in pythone, leveraging the flexibility
    and power of the PIO state machine.

    The class should not be instantiated directly, but used via the `@asm_pio` decorator.
    """

    labels: Dict
    prog: List
    wrap_used: bool
    sideset_count: int
    delay_max: int
    sideset_opt: bool
    pass_: int
    num_instr: int
    num_sideset: int
    def __init__(
        self,
        *,
        out_init: int | List | None = ...,
        set_init: int | List | None = ...,
        sideset_init: int | List | None = ...,
        in_shiftdir: int = ...,
        out_shiftdir: int = ...,
        autopush: bool = ...,
        autopull: bool = ...,
        push_thresh: int = ...,
        pull_thresh: int = ...,
        fifo_join: int = ...,
    ) -> None: ...
    def __getitem__(self, key): ...
    def start_pass(self, pass_) -> None:
        """The start_pass method is used to start a pass over the instructions,
        setting up the necessary state for the pass. It handles wrapping instructions
        if needed and adjusts the delay maximum based on the number of side-set bits.
        """

        ...

    def delay(self, delay: int):
        """
        The delay method allows setting a delay for the current instruction,
        ensuring it does not exceed the maximum allowed delay.
        """

    def side(self, value: int):
        """\
        This is a modifier which can be applied to any instruction, and is used to control side-set pin values.
        value: the value (bits) to output on the side-set pins

        When an instruction has side 0 next to it, the corresponding output is set LOW, 
        and when it has side 1 next to it, the corresponding output is set HIGH. 
        There can be up to 5 side-set pins, in which case side N is interpreted as a binary number.

        `side(0b00011)` sets the first and the second side-set pin HIGH, and the others LOW.
        """
        ...

    def wrap_target(self) -> None: ...
    def wrap(self) -> None:
        """
        The wrap method sets the wrap point for the program, ensuring the program loops correctly.
        """
        ...

    def label(self, label: str) -> None: ...
    def word(self, instr, label: str | None = ...): ...
    def nop(self): ...
    def jmp(self, cond, label: str | None = ...): ...
    def wait(self, polarity, src, index): ...
    def in_(self, src, data): ...
    def out(self, dest, data): ...
    def push(self, value: int = ..., value2: int = ...): ...
    def pull(self, value: int = ..., value2: int = ...): ...
    def mov(self, dest, src): ...
    def irq(self, mod, index: Incomplete | None = ...): ...
    def set(self, dest, data): ...

_pio_funcs: Dict[str, Any]

def asm_pio(
    *,
    out_init: Union[Pin, List[Pin], int, None] = None,
    set_init: Union[Pin, List[Pin], int, None] = None,
    sideset_init: Union[Pin, List[Pin], int, None] = None,
    in_shiftdir=0,
    out_shiftdir=0,
    autopush=False,
    autopull=False,
    push_thresh=32,
    pull_thresh=32,
    fifo_join=PIO.JOIN_NONE,
) -> Callable[..., PIOASMEmit]:
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

def asm_pio_encode(instr, sideset_count, sideset_opt=False) -> int:
    """
    Assemble a single PIO instruction. You usually want to use `asm_pio()`
    instead.

    >>> rp2.asm_pio_encode("set(0, 1)", 0)
    57345
    """
    ...
