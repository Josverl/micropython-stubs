""" """

from __future__ import annotations
from typing import Any, Optional
from _typeshed import Incomplete

class StateMachine:
    """
    Get the state machine numbered *id*. The RP2040 has two identical PIO
    instances, each with 4 state machines: so there are 8 state machines in
    total, numbered 0 to 7.

    Optionally initialize it with the given program *program*: see
    `StateMachine.init`.
    """

    def __init__(self, id, program, *args, **kwargs) -> None: ...
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
        reused so as to save on instruction memory.

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

    def active(self, value: Optional[Any] = None) -> Incomplete:
        """
        Gets or sets whether the state machine is currently running.

        >>> sm.active()
        True
        >>> sm.active(0)
        False
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

    def irq(self, handler=None, trigger=0 | 1, hard=False) -> Incomplete:
        """
        Returns the IRQ object for the given StateMachine.

        Optionally configure it.
        """
        ...
