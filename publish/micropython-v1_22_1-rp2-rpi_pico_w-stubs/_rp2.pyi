"""
Functionality specific to the RP2.

MicroPython module: https://docs.micropython.org/en/v1.22.1/library/rp2.html

The ``rp2`` module contains functions and classes specific to the RP2040, as
used in the Raspberry Pi Pico.

See the `RP2040 Python datasheet
<https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf>`_
for more information, and `pico-micropython-examples
<https://github.com/raspberrypi/pico-micropython-examples/tree/master/pio>`_
for example code.

---
Module: '_rp2' on micropython-v1.22.1-rp2-RPI_PICO_W
"""
# MCU: {'family': 'micropython', 'version': '1.22.1', 'build': '', 'ver': '1.22.1', 'port': 'rp2', 'board': 'RPI_PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.17.1
from __future__ import annotations
from _typeshed import Incomplete
from typing import Any, Optional

def country(*args, **kwargs) -> Incomplete: ...
def bootsel_button() -> Incomplete:
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

class Flash:
    """
    Gets the singleton object for accessing the SPI flash memory.
    """

    def readblocks(self, block_num, buf, offset: Optional[int] = 0) -> Incomplete: ...
    def writeblocks(self, block_num, buf, offset: Optional[int] = 0) -> Incomplete: ...
    def ioctl(self, cmd, arg) -> Incomplete:
        """
        These methods implement the simple and extended
        :ref:`block protocol <block-device-interface>` defined by
        :class:`os.AbstractBlockDev`.
        """
        ...
    def __init__(self, *argv, **kwargs) -> None: ...

class DMA:
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def unpack_ctrl(self, *args, **kwargs) -> Incomplete: ...
    def pack_ctrl(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def config(self, *args, **kwargs) -> Incomplete: ...
    def active(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class StateMachine:
    """
    Get the state machine numbered *id*. The RP2040 has two identical PIO
    instances, each with 4 state machines: so there are 8 state machines in
    total, numbered 0 to 7.

    Optionally initialize it with the given program *program*: see
    `StateMachine.init`.
    """

    def irq(self, handler=None, trigger=0 | 1, hard=False) -> Incomplete:
        """
        Returns the IRQ object for the given StateMachine.

        Optionally configure it.
        """
        ...
    def put(self, value, shift=0) -> Incomplete:
        """
        Push words onto the state machine's TX FIFO.

        *value* can be an integer, an array of type ``B``, ``H`` or ``I``, or a
        `bytearray`.

        This method will block until all words have been written to the FIFO.  If
        the FIFO is, or becomes, full, the method will block until the state machine
        pulls enough words to complete the write.

        Each word is first shifted left by *shift* bits, i.e. the state machine
        receives ``word << shift``.
        """
        ...
    def restart(self) -> Incomplete:
        """
        Restarts the state machine and jumps to the beginning of the program.

        This method clears the state machine's internal state using the RP2040's
        ``SM_RESTART`` register. This includes:

         - input and output shift counters
         - the contents of the input shift register
         - the delay counter
         - the waiting-on-IRQ state
         - a stalled instruction run using `StateMachine.exec()`
        """
        ...
    def rx_fifo(self) -> int:
        """
        Returns the number of words in the state machine's RX FIFO. A value of 0
        indicates the FIFO is empty.

        Useful for checking if data is waiting to be read, before calling
        `StateMachine.get()`.
        """
        ...
    def tx_fifo(self) -> int:
        """
        Returns the number of words in the state machine's TX FIFO. A value of 0
        indicates the FIFO is empty.

        Useful for checking if there is space to push another word using
        `StateMachine.put()`.
        """
        ...
    def init(
        self,
        program,
        freq=-1,
        *,
        in_base=None,
        out_base=None,
        set_base=None,
        jmp_pin=None,
        sideset_base=None,
        in_shiftdir=None,
        out_shiftdir=None,
        push_thresh=None,
        pull_thresh=None,
    ) -> None:
        """
        Configure the state machine instance to run the given *program*.

        The program is added to the instruction memory of this PIO instance. If the
        instruction memory already contains this program, then its offset is
        re-used so as to save on instruction memory.

        - *freq* is the frequency in Hz to run the state machine at. Defaults to
          the system clock frequency.

          The clock divider is computed as ``system clock frequency / freq``, so
          there can be slight rounding errors.

          The minimum possible clock divider is one 65536th of the system clock: so
          at the default system clock frequency of 125MHz, the minimum value of
          *freq* is ``1908``. To run state machines at slower frequencies, you'll
          need to reduce the system clock speed with `machine.freq()`.
        - *in_base* is the first pin to use for ``in()`` instructions.
        - *out_base* is the first pin to use for ``out()`` instructions.
        - *set_base* is the first pin to use for ``set()`` instructions.
        - *jmp_pin* is the first pin to use for ``jmp(pin, ...)`` instructions.
        - *sideset_base* is the first pin to use for side-setting.
        - *in_shiftdir* is the direction the ISR will shift, either
          `PIO.SHIFT_LEFT` or `PIO.SHIFT_RIGHT`.
        - *out_shiftdir* is the direction the OSR will shift, either
          `PIO.SHIFT_LEFT` or `PIO.SHIFT_RIGHT`.
        - *push_thresh* is the threshold in bits before auto-push or conditional
          re-pushing is triggered.
        - *pull_thresh* is the threshold in bits before auto-pull or conditional
          re-pulling is triggered.
        """
        ...
    def exec(self, instr) -> Incomplete:
        """
        Execute a single PIO instruction.

        If *instr* is a string then uses `asm_pio_encode` to encode the instruction
        from the given string.

        >>> sm.exec("set(0, 1)")

        If *instr* is an integer then it is treated as an already encoded PIO
        machine code instruction to be executed.

        >>> sm.exec(rp2.asm_pio_encode("out(y, 8)", 0))
        """
        ...
    def get(self, buf=None, shift=0) -> Incomplete:
        """
        Pull a word from the state machine's RX FIFO.

        If the FIFO is empty, it blocks until data arrives (i.e. the state machine
        pushes a word).

        The value is shifted right by *shift* bits before returning, i.e. the
        return value is ``word >> shift``.
        """
        ...
    def active(self, value: Optional[Any] = None) -> Incomplete:
        """
        Gets or sets whether the state machine is currently running.

        >>> sm.active()
        True
        >>> sm.active(0)
        False
        """
        ...
    def __init__(self, *argv, **kwargs) -> None: ...

class PIO:
    """
    Gets the PIO instance numbered *id*. The RP2040 has two PIO instances,
    numbered 0 and 1.

    Raises a ``ValueError`` if any other argument is provided.
    """

    JOIN_TX: int = 1
    JOIN_NONE: int = 0
    JOIN_RX: int = 2
    SHIFT_LEFT: int = 0
    OUT_HIGH: int = 3
    OUT_LOW: int = 2
    SHIFT_RIGHT: int = 1
    IN_LOW: int = 0
    IRQ_SM3: int = 2048
    IN_HIGH: int = 1
    IRQ_SM2: int = 1024
    IRQ_SM0: int = 256
    IRQ_SM1: int = 512
    def state_machine(self, id, program, *args, **kwargs) -> Incomplete:
        """
        Gets the state machine numbered *id*. On the RP2040, each PIO instance has
        four state machines, numbered 0 to 3.

        Optionally initialize it with a *program*: see `StateMachine.init`.

        >>> rp2.PIO(1).state_machine(3)
        StateMachine(7)
        """
        ...
    def remove_program(self, program: Optional[Any] = None) -> None:
        """
        Remove *program* from the instruction memory of this PIO instance.

        If no program is provided, it removes all programs.

        It is not an error to remove a program which has already been removed.
        """
        ...
    def irq(self, handler=None, trigger=IRQ_SM0, hard=False) -> Incomplete:
        """
        Returns the IRQ object for this PIO instance.

        MicroPython only uses IRQ 0 on each PIO instance. IRQ 1 is not available.

        Optionally configure it.
        """
        ...
    def add_program(self, program) -> Incomplete:
        """
        Add the *program* to the instruction memory of this PIO instance.

        The amount of memory available for programs on each PIO instance is
        limited. If there isn't enough space left in the PIO's program memory
        this method will raise ``OSError(ENOMEM)``.
        """
        ...
    def __init__(self, *argv, **kwargs) -> None: ...
