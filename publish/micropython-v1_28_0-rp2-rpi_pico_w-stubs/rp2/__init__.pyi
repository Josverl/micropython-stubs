# MCU: {'mpy': 'v6.3', 'build': '', 'ver': '1.28.0', 'arch': 'armv6m', 'version': '1.28.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'family': 'micropython', 'board_id': 'RPI_PICO_W', 'variant': '', 'cpu': 'RP2040'}
# Stubber: v1.28.0
"""
Functionality specific to the RP2.

MicroPython module: https://docs.micropython.org/en/v1.28.0/library/rp2.html

The ``rp2`` module contains functions and classes specific to the RP2040, as
used in the Raspberry Pi Pico.

See the `RP2040 Python datasheet
<https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf>`_
for more information, and `pico-micropython-examples
<https://github.com/raspberrypi/pico-micropython-examples/tree/master/pio>`_
for example code.

---
Module: 'rp2.PIOASMEmit'

---
Type hints for the ``rp2.asm_pio`` DSL **as exposed on RP2350** (PIO version 1).

This stub is a thin **overlay** on top of :mod:`rp2.asm_pio_rp2040` (the
RP2040-compatible PIO version 0 baseline). Importing it inside a
``TYPE_CHECKING`` block enables the additional instructions, sources,
modifiers and constants that exist on RP2350's PIO v1 hardware:

* ``irq(prev, …)`` / ``irq(next, …)`` — target a neighbouring PIO instance.
* ``wait(1, jmppin, n)`` — stall on the JMP-pin GPIO.
* ``wait(1, irq_prev, n)`` / ``wait(1, irq_next, n)`` — cross-PIO IRQ wait.
* ``in_(pindirs, n)`` and ``mov(pindirs, src)`` — read/write the PINDIRS register.
* Wider side-set / set / out pin counts (driven by ``@asm_pio`` configuration).

Reference: https://github.com/micropython/micropython/pull/18975

Usage in a PIO program file
---------------------------

The PIO target **must be specified explicitly** at the top of the file. Pick
*one* of the three imports below — they cannot be combined:

.. code-block:: python

    try:
        from typing_extensions import TYPE_CHECKING  # type: ignore
    except ImportError:
        TYPE_CHECKING = False

    if TYPE_CHECKING:
        # Default (RP2040 / PIO v0):
        from rp2.asm_pio import *

        # Explicit RP2040 / PIO v0:
        # from rp2.asm_pio_rp2040 import *

        # RP2350 / PIO v1 (uncomment instead of one of the lines above):
        # from rp2.asm_pio_rp2350 import *

This module re-exports every symbol from :mod:`rp2.asm_pio_rp2040`, so a
single ``from rp2.asm_pio_rp2350 import *`` is sufficient — there is no
need to also import the baseline.

---
Type hints for the ``rp2.asm_pio`` DSL **as exposed on RP2040** (PIO version 0).

This is the canonical, full declaration of the PIO assembler DSL. Two sibling
modules exist:

* :mod:`rp2.asm_pio_rp2040` — *this module* — RP2040 / PIO v0 (the baseline).
* :mod:`rp2.asm_pio_rp2350` — RP2350 / PIO v1 overlay (re-exports this module
  and adds ``prev``, ``next``, ``jmppin``, ``irq_prev``, ``irq_next``).
* :mod:`rp2.asm_pio` — thin default that simply re-exports this module
  (``from rp2.asm_pio_rp2040 import *``), kept for backward compatibility
  with the historical ``from rp2.asm_pio import *`` idiom.

In a PIO program file, pick *one* of the three imports below — they cannot
be combined:

```py
# -----------------------------------------------
# add type hints for the rp2.PIO Instructions
try:
    from typing_extensions import TYPE_CHECKING  # type: ignore
except ImportError:
    TYPE_CHECKING = False
if TYPE_CHECKING:
    # Default (RP2040 / PIO v0) — same as importing rp2.asm_pio_rp2040:
    from rp2.asm_pio import *

    # Explicit RP2040 / PIO v0:
    # from rp2.asm_pio_rp2040 import *

    # RP2350 / PIO v1:
    # from rp2.asm_pio_rp2350 import *
# -----------------------------------------------
```

For more information on PIO assembly programming and the Raspberry Pi Pico
Python SDK, refer to:

- raspberry-pi-pico-python-sdk.pdf: https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-python-sdk.pdf
- raspberry-pi-pico-c-sdk.pdf: https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-c-sdk.pdf
- Beginner-friendly reference: https://dernulleffekt.de/doku.php?id=raspberrypipico:pico_pio

---
Default PIO assembler typing surface — re-exports :mod:`rp2.asm_pio_rp2040`.

This module exists for backward compatibility with the historical idiom

.. code-block:: python

    if TYPE_CHECKING:
        from rp2.asm_pio import *

…which has always meant *"give me the RP2040 / PIO v0 DSL"*. The actual
declarations now live in :mod:`rp2.asm_pio_rp2040`; this stub simply
re-exports them so existing PIO programs keep type-checking unchanged.

PIO target selection
--------------------

Pick *one* of the three imports below in your PIO program file — they
cannot be combined:

.. code-block:: python

    if TYPE_CHECKING:
        # Default (RP2040 / PIO v0) — equivalent to importing rp2.asm_pio_rp2040:
        from rp2.asm_pio import *

        # Explicit RP2040 / PIO v0:
        # from rp2.asm_pio_rp2040 import *

        # RP2350 / PIO v1 (adds prev, next, jmppin, irq_prev, irq_next):
        # from rp2.asm_pio_rp2350 import *

See https://github.com/micropython/micropython/pull/18975 for the RP2350
PIO v1 additions.

---
Module: 'rp2' on micropython-v1.28.0-rp2-RPI_PICO_W
"""

# MCU: {'mpy': 'v6.3', 'build': '', 'ver': '1.28.0', 'arch': 'armv6m', 'version': '1.28.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'family': 'micropython', 'board_id': 'RPI_PICO_W', 'variant': '', 'cpu': 'RP2040'}
# Stubber: v1.28.0
from __future__ import annotations
from typing import Union, List, Literal, overload, Any, Callable, Optional, Final
from _typeshed import ReadableBuffer, WriteableBuffer, Incomplete
from rp2.asm_pio_rp2040 import *
from micropython import const
from typing_extensions import Awaitable, TypeAlias, TypeVar, Protocol, Self, TYPE_CHECKING
from _mpy_shed import AnyReadableBuf, AnyWritableBuf, _IRQ
from vfs import AbstractBlockDev
from machine import Pin
_IRQ_TRIGGERS: TypeAlias = Literal[256, 512, 1024, 2048]

_pio_funcs: dict = {}
_pio_directives: tuple = ()
_pio_instructions: tuple = ()

def bootsel_button() -> int:
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

@overload
def country() -> str:
    """
    Get the two-letter country code.

    Deprecated alias to ``network.country``.
    Only available when CYW43 networking support is enabled.
    """
    ...

@overload
def country(code: str, /) -> None:
    """
    Set the two-letter country code.

    Deprecated alias to ``network.country``.
    Only available when CYW43 networking support is enabled.
    """
    ...

@overload
def country() -> str:
    """
    Get the two-letter country code.

    Deprecated alias to ``network.country``.
    Only available when CYW43 networking support is enabled.
    """
    ...

@overload
def country(code: str, /) -> None:
    """
    Set the two-letter country code.

    Deprecated alias to ``network.country``.
    Only available when CYW43 networking support is enabled.
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

def const(*args, **kwargs) -> Incomplete: ...

class DMA:
    """
    Claim one of the DMA controller channels for exclusive use.
    """
    def irq(self, handler: Optional[Callable] = None, hard: bool = False) -> _IRQ:
        """
        Returns the IRQ object for this DMA channel and optionally configures it.
        """
        ...
    @staticmethod
    def unpack_ctrl(value: int) -> dict[str, int]:
        """
        Unpack a value for a DMA channel control register into a dictionary with key/value pairs
        for each of the fields in the control register.  *value* is the ``ctrl`` register value
        to unpack.

        This method will return values for all the keys that can be passed to ``DMA.pack_ctrl``.
        In addition, it will also return the read-only flags in the control register: ``busy``,
        which goes high when a transfer starts and low when it ends, and ``ahb_err``, which is
        the logical OR of the ``read_err`` and ``write_err`` flags. These values will be ignored
        when packing, so that the dictionary created by unpacking a control register can be used
        directly as the keyword arguments for packing.
        """
        ...
    def pack_ctrl(
        self,
        *,
        default: int | None = None,
        enable: bool = True,
        high_pri: bool = False,
        size: int = 2,
        inc_read: bool = True,
        inc_write: bool = True,
        # RP2350-only fields:
        inc_read_rev: Optional[bool] = None,  # RP2350 only
        inc_write_rev: Optional[bool] = None,  # RP2350 only
        **kwargs,
    ) -> int:
        """
        Pack the values provided in the keyword arguments into the named fields of a new control
        register value. Any field that is not provided will be set to a default value. The
        default will either be taken from the provided ``default`` value, or if that is not
        given, a default suitable for the current channel; setting this to the current value
        of the `DMA.ctrl` attribute provides an easy way to override a subset of the fields.

        The keys for the keyword arguments can be any key returned by the :meth:`DMA.unpack_ctrl()`
        method. The writable values are:

        - *enable*: ``bool`` Set to enable the channel (default: ``True``).

        - *high_pri*: ``bool`` Make this channel's bus traffic high priority (default: ``False``).

        - *size*: ``int`` Transfer size: 0=byte, 1=half word, 2=word (default: 2).

        - *inc_read*: ``bool`` Increment the read address after each transfer (default: ``True``).

        - *inc_write*: ``bool`` Increment the write address after each transfer (default: ``True``).

        - *ring_size*: ``int`` If non-zero, only the bottom ``ring_size`` bits of one
          address register will change when an address is incremented, causing the
          address to wrap at the next ``1 << ring_size`` byte boundary. Which
          address is wrapped is controlled by the ``ring_sel`` flag. A zero value
          disables address wrapping.

        - *ring_sel*: ``bool`` Set to ``False`` to have the ``ring_size`` apply to the read address
          or ``True`` to apply to the write address.

        - *chain_to*: ``int`` The channel number for a channel to trigger after this transfer
          completes. Setting this value to this DMA object's own channel number
          disables chaining (this is the default).

        - *treq_sel*: ``int`` Select a Transfer Request signal. See section 2.5.3 in the RP2040
          datasheet for details.

        - *irq_quiet*: ``bool`` Do not generate interrupt at the end of each transfer. Interrupts
          will instead be generated when a zero value is written to the trigger
          register, which will halt a sequence of chained transfers (default:
          ``True``).

        - *bswap*: ``bool`` If set to true, bytes in words or half-words will be reversed before
          writing (default: ``True``).

        - *sniff_en*: ``bool`` Set to ``True`` to allow data to be accessed by the chips sniff
          hardware (default: ``False``).

        - *write_err*: ``bool`` Setting this to ``True`` will clear a previously reported write
          error.

        - *read_err*: ``bool`` Setting this to ``True`` will clear a previously reported read
          error.

        See the description of the ``CH0_CTRL_TRIG`` register in section 2.5.7 of the RP2040
        datasheet for details of all of these fields.
        """
        ...
    def close(self) -> None:
        """
        Release the claim on the underlying DMA channel and free the interrupt
        handler. The :class:`DMA` object can not be used after this operation.
        """
        ...
    def config(
        self,
        *,
        read: int | AnyReadableBuf | None = None,
        write: int | AnyWritableBuf | None = None,
        count: int | None = None,
        ctrl: int | None = None,
        trigger: bool = False,
    ) -> None:
        """
        Configure the DMA registers for the channel and optionally start the transfer.
        Parameters are:

        - *read*: The address from which the DMA controller will start reading data or
          an object that will provide data to be read. It can be an integer or any
          object that supports the buffer protocol.
        - *write*: The address to which the DMA controller will start writing or an
          object into which data will be written. It can be an integer or any object
          that supports the buffer protocol.
        - *count*: The number of bus transfers that will execute before this channel
          stops. Note that this is the number of transfers, not the number of bytes.
          If the transfers are 2 or 4 bytes wide then the total amount of data moved
          (and thus the size of required buffer) needs to be multiplied accordingly.
        - *ctrl*: The value for the DMA control register. This is an integer value
          that is typically packed using the :meth:`DMA.pack_ctrl()`.
        - *trigger*: Optionally commence the transfer immediately.
        """
        ...
    def active(self, value: Any | None = None) -> bool:
        """
        Gets or sets whether the DMA channel is currently running.

        >>> sm.active()
        0
        >>> sm.active(1)
        >>> while sm.active():
        """
        ...
    def __init__(self) -> None: ...

class PIO:
    """
    Gets the PIO instance numbered *id*. The RP2040 has two PIO instances,
    numbered 0 and 1.

    Raises a ``ValueError`` if any other argument is provided.
    """

    JOIN_TX: Final[int] = 1
    """These constants are used for the *fifo_join* argument to `asm_pio`."""
    JOIN_NONE: Final[int] = 0
    """These constants are used for the *fifo_join* argument to `asm_pio`."""
    JOIN_RX: Final[int] = 2
    """These constants are used for the *fifo_join* argument to `asm_pio`."""
    SHIFT_LEFT: Final[int] = 0
    """\
    These constants are used for the *in_shiftdir* and *out_shiftdir* arguments
    to `asm_pio` or `StateMachine.init`.
    """
    OUT_HIGH: Final[int] = 3
    """\
    These constants are used for the *out_init*, *set_init*, and *sideset_init*
    arguments to `asm_pio`.
    """
    OUT_LOW: Final[int] = 2
    """\
    These constants are used for the *out_init*, *set_init*, and *sideset_init*
    arguments to `asm_pio`.
    """
    SHIFT_RIGHT: Final[int] = 1
    """\
    These constants are used for the *in_shiftdir* and *out_shiftdir* arguments
    to `asm_pio` or `StateMachine.init`.
    """
    IN_LOW: Final[int] = 0
    """\
    These constants are used for the *out_init*, *set_init*, and *sideset_init*
    arguments to `asm_pio`.
    """
    IRQ_SM3: Final[int] = 2048
    """These constants are used for the *trigger* argument to `PIO.irq`."""
    IN_HIGH: Final[int] = 1
    """\
    These constants are used for the *out_init*, *set_init*, and *sideset_init*
    arguments to `asm_pio`.
    """
    IRQ_SM2: Final[int] = 1024
    """These constants are used for the *trigger* argument to `PIO.irq`."""
    IRQ_SM0: Final[int] = 256
    """These constants are used for the *trigger* argument to `PIO.irq`."""
    IRQ_SM1: Final[int] = 512
    """These constants are used for the *trigger* argument to `PIO.irq`."""
    def state_machine(self, id: int, program: _PIO_ASM_Program | None = None, **kwargs) -> StateMachine:
        """
        Gets the state machine numbered *id*. On the RP2040, each PIO instance has
        four state machines, numbered 0 to 3.

        Optionally initialize it with a *program*: see `StateMachine.init`.

        >>> rp2.PIO(1).state_machine(3)
        StateMachine(7)
        """
        ...
    def remove_program(self, program: Optional[_PIO_ASM_Program] = None) -> None:
        """
        Remove *program* from the instruction memory of this PIO instance.

        If no program is provided, it removes all programs.

        It is not an error to remove a program which has already been removed.
        """
        ...
    def irq(
        self,
        handler: Optional[Callable[[PIO], None]] = None,
        trigger: _IRQ_TRIGGERS = 0xF00,
        hard: bool = False,
    ) -> _IRQ:
        """
        Returns the IRQ object for this PIO instance.

        MicroPython only uses IRQ 0 on each PIO instance. IRQ 1 is not available.

        Optionally configure it.
        """
        ...
    def add_program(self, program: _PIO_ASM_Program) -> None:
        """
        Add the *program* to the instruction memory of this PIO instance.

        The amount of memory available for programs on each PIO instance is
        limited. If there isn't enough space left in the PIO's program memory
        this method will raise ``OSError(ENOMEM)``.
        """
        ...
    def __init__(self, id: int) -> None: ...

class StateMachine:
    """
    Get the state machine numbered *id*. The RP2040 has two identical PIO
    instances, each with 4 state machines: so there are 8 state machines in
    total, numbered 0 to 7.

    Optionally initialize it with the given program *program*: see
    `StateMachine.init`.
    """
    def irq(self, handler: Optional[Callable] = None, trigger: int = 1, hard: bool = False) -> _IRQ:
        """
        Returns the IRQ object for the given StateMachine.

        Optionally configure it.
        """
        ...
    def put(self, value: int | ReadableBuffer, shift: int = 0) -> None:
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
    def restart(self) -> None:
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
        program: _PIO_ASM_Program,
        *,
        freq: int = -1,
        in_base: Pin | None = None,
        out_base: Pin | None = None,
        set_base: Pin | None = None,
        jmp_pin: Pin | None = None,
        sideset_base: Pin | None = None,
        in_shiftdir: int | None = None,
        out_shiftdir: int | None = None,
        push_thresh: int | None = None,
        pull_thresh: int | None = None,
        **kwargs,
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

        Note: pins used for *in_base* need to be configured manually for input (or
        otherwise) so that the PIO can see the desired signal (they could be input
        pins, output pins, or connected to a different peripheral).  The *jmp_pin*
        can also be configured manually, but by default will be an input pin.
        """
        ...
    def exec(self, instr: Union[int, str]) -> None:
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

    @overload
    def get(self, buf: None = None, shift: int = 0) -> int: ...
    @overload
    def get(self, buf: WriteableBuffer, shift: int = 0) -> WriteableBuffer: ...
    @overload
    def get(self, buf: None = None, shift: int = 0) -> int: ...
    @overload
    def get(self, buf: WriteableBuffer, shift: int = 0) -> WriteableBuffer: ...
    @overload
    def active(self) -> bool: ...
    @overload
    def active(self, value: Union[bool, int]) -> bool:
        """
        Gets or sets whether the state machine is currently running.

        >>> sm.active()
        True
        >>> sm.active(0)
        False
        """
        ...
    @overload
    def active(self) -> bool: ...
    @overload
    def active(self, value: Union[bool, int]) -> bool:
        """
        Gets or sets whether the state machine is currently running.

        >>> sm.active()
        True
        >>> sm.active(0)
        False
        """
        ...
    def __init__(
        self,
        id: int,
        program: _PIO_ASM_Program | None = None,
        *,
        freq: int = -1,
        in_base: Pin | None = None,
        out_base: Pin | None = None,
        set_base: Pin | None = None,
        jmp_pin: Pin | None = None,
        sideset_base: Pin | None = None,
        in_shiftdir: int | None = None,
        out_shiftdir: int | None = None,
        push_thresh: int | None = None,
        pull_thresh: int | None = None,
        **kwargs,
    ) -> None: ...
class PIOASMEmit:
    """
    Internal emitter used by the ``@asm_pio`` decorator. Not intended for
    direct use.

    PIO instructions, directives, and modifiers are exposed via
    :mod:`rp2.asm_pio` (which re-exports :mod:`rp2.asm_pio_rp2040`), and
    that module is the single source of truth for their typing surface.
    """
    def __init__(
        self,
        *,
        out_init: int | List | None = ...,
        set_init: int | List | None = ...,
        sideset_init: int | List | None = ...,
        side_pindir: bool = ...,
        in_shiftdir: int = ...,
        out_shiftdir: int = ...,
        autopush: bool = ...,
        autopull: bool = ...,
        push_thresh: int = ...,
        pull_thresh: int = ...,
        fifo_join: int = ...,
    ) -> None: ...
    def __getattr__(self, name: str) -> Incomplete: ...

class Flash:
    """
    Gets the singleton object for accessing the SPI flash memory.
    """
    @overload
    def readblocks(self, block_num: int, buf: AnyWritableBuf) -> None:
        """
        The first form reads aligned, multiples of blocks.
        Starting at the block given by the index *block_num*, read blocks from
        the device into *buf* (an array of bytes).
        The number of blocks to read is given by the length of *buf*,
        which will be a multiple of the block size.
        """

    @overload
    def readblocks(self, block_num: int, buf: AnyWritableBuf, offset: int) -> None:
        """
        The second form allows reading at arbitrary locations within a block,
        and arbitrary lengths.
        Starting at block index *block_num*, and byte offset within that block
        of *offset*, read bytes from the device into *buf* (an array of bytes).
        The number of bytes to read is given by the length of *buf*.
        """
    @overload
    def readblocks(self, block_num: int, buf: AnyWritableBuf) -> None:
        """
        The first form reads aligned, multiples of blocks.
        Starting at the block given by the index *block_num*, read blocks from
        the device into *buf* (an array of bytes).
        The number of blocks to read is given by the length of *buf*,
        which will be a multiple of the block size.
        """

    @overload
    def readblocks(self, block_num: int, buf: AnyWritableBuf, offset: int) -> None:
        """
        The second form allows reading at arbitrary locations within a block,
        and arbitrary lengths.
        Starting at block index *block_num*, and byte offset within that block
        of *offset*, read bytes from the device into *buf* (an array of bytes).
        The number of bytes to read is given by the length of *buf*.
        """

    @overload
    def writeblocks(self, block_num: int, buf: AnyReadableBuf) -> None:
        """
        The first form writes aligned, multiples of blocks, and requires that the
        blocks that are written to be first erased (if necessary) by this method.
        Starting at the block given by the index *block_num*, write blocks from
        *buf* (an array of bytes) to the device.
        The number of blocks to write is given by the length of *buf*,
        which will be a multiple of the block size.
        """

    @overload
    def writeblocks(self, block_num: int, buf: AnyReadableBuf, offset: int) -> None:
        """
        The second form allows writing at arbitrary locations within a block,
        and arbitrary lengths.  Only the bytes being written should be changed,
        and the caller of this method must ensure that the relevant blocks are
        erased via a prior ``ioctl`` call.
        Starting at block index *block_num*, and byte offset within that block
        of *offset*, write bytes from *buf* (an array of bytes) to the device.
        The number of bytes to write is given by the length of *buf*.

        Note that implementations must never implicitly erase blocks if the offset
        argument is specified, even if it is zero.
        """

    @overload
    def writeblocks(self, block_num: int, buf: AnyReadableBuf) -> None:
        """
        The first form writes aligned, multiples of blocks, and requires that the
        blocks that are written to be first erased (if necessary) by this method.
        Starting at the block given by the index *block_num*, write blocks from
        *buf* (an array of bytes) to the device.
        The number of blocks to write is given by the length of *buf*,
        which will be a multiple of the block size.
        """

    @overload
    def writeblocks(self, block_num: int, buf: AnyReadableBuf, offset: int) -> None:
        """
        The second form allows writing at arbitrary locations within a block,
        and arbitrary lengths.  Only the bytes being written should be changed,
        and the caller of this method must ensure that the relevant blocks are
        erased via a prior ``ioctl`` call.
        Starting at block index *block_num*, and byte offset within that block
        of *offset*, write bytes from *buf* (an array of bytes) to the device.
        The number of bytes to write is given by the length of *buf*.

        Note that implementations must never implicitly erase blocks if the offset
        argument is specified, even if it is zero.
        """

    @overload
    def ioctl(self, op: int, arg: int) -> int | None: ...
    #
    @overload
    def ioctl(self, op: int) -> int | None:
        """
        These methods implement the simple and extended
        :ref:`block protocol <block-device-interface>` defined by
        :class:`vfs.AbstractBlockDev`.
        """

    @overload
    def ioctl(self, op: int, arg: int) -> int | None: ...
    #
    @overload
    def ioctl(self, op: int) -> int | None:
        """
        These methods implement the simple and extended
        :ref:`block protocol <block-device-interface>` defined by
        :class:`vfs.AbstractBlockDev`.
        """
    def __init__(self, *, start: int = -1, len: int = -1) -> None: ...

class PIOASMError(Exception): ...
class _PIO_ASM_Program:
    """Opaque handle representing an assembled PIO program.

    Returned by ``@asm_pio`` and consumed by ``StateMachine``/``PIO``.
    Users should not introspect or index this object. The chainable
    per-instruction expression that lives inside the decorator body is
    a different type (``rp2.asm_pio._PIOInstr``).
    """
