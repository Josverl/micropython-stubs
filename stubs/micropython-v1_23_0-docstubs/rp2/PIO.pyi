""" """

from __future__ import annotations
from typing import Any, Optional
from _typeshed import Incomplete

class PIO:
    """
    Gets the PIO instance numbered *id*. The RP2040 has two PIO instances,
    numbered 0 and 1.

    Raises a ``ValueError`` if any other argument is provided.
    """

    IN_LOW: Incomplete
    """\
    These constants are used for the *out_init*, *set_init*, and *sideset_init*
    arguments to `asm_pio`.
    """
    IN_HIGH: Incomplete
    """\
    These constants are used for the *out_init*, *set_init*, and *sideset_init*
    arguments to `asm_pio`.
    """
    OUT_LOW: Incomplete
    """\
    These constants are used for the *out_init*, *set_init*, and *sideset_init*
    arguments to `asm_pio`.
    """
    OUT_HIGH: Incomplete
    """\
    These constants are used for the *out_init*, *set_init*, and *sideset_init*
    arguments to `asm_pio`.
    """
    SHIFT_LEFT: Incomplete
    """\
    These constants are used for the *in_shiftdir* and *out_shiftdir* arguments
    to `asm_pio` or `StateMachine.init`.
    """
    SHIFT_RIGHT: Incomplete
    """\
    These constants are used for the *in_shiftdir* and *out_shiftdir* arguments
    to `asm_pio` or `StateMachine.init`.
    """
    JOIN_NONE: Incomplete
    """These constants are used for the *fifo_join* argument to `asm_pio`."""
    JOIN_TX: Incomplete
    """These constants are used for the *fifo_join* argument to `asm_pio`."""
    JOIN_RX: Incomplete
    """These constants are used for the *fifo_join* argument to `asm_pio`."""
    IRQ_SM0: Incomplete
    """These constants are used for the *trigger* argument to `PIO.irq`."""
    IRQ_SM1: Incomplete
    """These constants are used for the *trigger* argument to `PIO.irq`."""
    IRQ_SM2: Incomplete
    """These constants are used for the *trigger* argument to `PIO.irq`."""
    IRQ_SM3: Incomplete
    """These constants are used for the *trigger* argument to `PIO.irq`."""
    def __init__(self, id) -> None: ...
    def add_program(self, program) -> Incomplete:
        """
        Add the *program* to the instruction memory of this PIO instance.

        The amount of memory available for programs on each PIO instance is
        limited. If there isn't enough space left in the PIO's program memory
        this method will raise ``OSError(ENOMEM)``.
        """
        ...

    def remove_program(self, program: Optional[Any] = None) -> None:
        """
        Remove *program* from the instruction memory of this PIO instance.

        If no program is provided, it removes all programs.

        It is not an error to remove a program which has already been removed.
        """
        ...

    def state_machine(self, id, program, *args, **kwargs) -> Incomplete:
        """
        Gets the state machine numbered *id*. On the RP2040, each PIO instance has
        four state machines, numbered 0 to 3.

        Optionally initialize it with a *program*: see `StateMachine.init`.

        >>> rp2.PIO(1).state_machine(3)
        StateMachine(7)
        """
        ...

    def irq(self, handler=None, trigger=IRQ_SM0, hard=False) -> Incomplete:
        """
        Returns the IRQ object for this PIO instance.

        MicroPython only uses IRQ 0 on each PIO instance. IRQ 1 is not available.

        Optionally configure it.
        """
        ...
