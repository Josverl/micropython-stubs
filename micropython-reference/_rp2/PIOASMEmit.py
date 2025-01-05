"""
Module: '_rp2.PIOASMEmit'
"""

from __future__ import annotations

from typing import Callable, Dict, List, Union

from _typeshed import Incomplete


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
