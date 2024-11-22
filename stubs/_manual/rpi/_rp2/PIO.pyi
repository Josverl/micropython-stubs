"""
Module: '_rp2' on micropython-v1.23.0-rp2-RPI_PICO
"""

# MCU: {'build': '', 'ver': '1.23.0', 'version': '1.23.0', 'port': 'rp2', 'board': 'RPI_PICO', 'mpy': 'v6.3', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.23.0
from __future__ import annotations

from typing import Callable, Final, Literal, Optional

from _mpy_shed import _IRQ
from _typeshed import Incomplete
from typing_extensions import TypeAlias

from .StateMachine import StateMachine

_PIO_ASM_Program: TypeAlias = Incomplete  # ? Callable
_IRQ_TRIGGERS = Literal[256, 512, 1024, 2048]

class PIO:
    """
    Gets the PIO instance numbered *id*. The RP2040 has two PIO instances,
    numbered 0 and 1.

    Raises a ``ValueError`` if any other argument is provided.
    """

    #
    JOIN_TX: int = 1
    JOIN_NONE: int = 0
    JOIN_RX: int = 2
    #
    IN_LOW: Final[int] = 0
    IN_HIGH: Final[int] = 1
    #
    OUT_LOW: Final[int] = 2
    OUT_HIGH: Final[int] = 3
    #
    SHIFT_LEFT: Final[int] = 0
    SHIFT_RIGHT: Final[int] = 1
    #
    IRQ_SM0: Final[int] = 256
    IRQ_SM1: Final[int] = 512
    IRQ_SM2: Final[int] = 1024
    IRQ_SM3: Final[int] = 2048

    def __init__(self, id) -> None: ...
    def add_program(self, program: _PIO_ASM_Program) -> None:
        """
        Add the *program* to the instruction memory of this PIO instance.

        The amount of memory available for programs on each PIO instance is
        limited. If there isn't enough space left in the PIO's program memory
        this method will raise ``OSError(ENOMEM)``.
        """
        ...

    def remove_program(self, program: Optional[_PIO_ASM_Program] = None) -> None:
        """
        Remove *program* from the instruction memory of this PIO instance.

        If no program is provided, it removes all programs.

        It is not an error to remove a program which has already been removed.
        """
        ...

    def state_machine(self, id: int, program: _PIO_ASM_Program, *args, **kwargs) -> StateMachine:
        """
        Gets the state machine numbered *id*. On the RP2040, each PIO instance has
        four state machines, numbered 0 to 3.

        Optionally initialize it with a *program*: see `StateMachine.init`.

        >>> rp2.PIO(1).state_machine(3)
        StateMachine(7)
        """
        ...

    def irq(
        self,
        handler: Optional[Callable[[PIO], None]] = None,
        trigger: _IRQ_TRIGGERS | None = None,
        hard: bool = False,
    ) -> _IRQ:
        """
        Returns the IRQ object for this PIO instance.

        MicroPython only uses IRQ 0 on each PIO instance. IRQ 1 is not available.

        Optionally configure it.
        """
        ...
