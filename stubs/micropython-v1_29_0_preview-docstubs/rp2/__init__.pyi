# MCU: {'mpy': 'v6.3', 'build': '', 'ver': '1.28.0', 'arch': 'armv6m', 'version': '1.28.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'family': 'micropython', 'board_id': 'RPI_PICO_W', 'variant': '', 'cpu': 'RP2040'}
# Stubber: v1.28.0
"""
Functionality specific to the RP2.

MicroPython module: https://docs.micropython.org/en/v1.29.0/library/rp2.html

The ``rp2`` module contains functions and classes specific to the RP2040, as
used in the Raspberry Pi Pico.

See the `RP2040 Python datasheet
<https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf>`_
for more information, and `pico-micropython-examples
<https://github.com/raspberrypi/pico-micropython-examples/tree/master/pio>`_
for example code.
"""

# source version: v1.29.0-preview
# origin module:: repos/micropython/docs/library/rp2.rst
from __future__ import annotations
from _typeshed import ReadableBuffer, WriteableBuffer, Incomplete
from typing_extensions import Protocol, Self, TYPE_CHECKING, TypeVar, TypeAlias, Awaitable
from rp2.DMA import DMA
from rp2.Flash import Flash
from rp2.PIO import PIO
from rp2.StateMachine import StateMachine
from rp2.asm_pio_rp2040 import *
from micropython import const
from rp2 import PIOASMEmit, _PIO_ASM_Program
from typing import Callable, Literal, Union, overload, List
from _mpy_shed import AnyReadableBuf, AnyWritableBuf, _IRQ
from machine import Pin
from vfs import AbstractBlockDev

_IRQ_TRIGGERS: TypeAlias = Literal[256, 512, 1024, 2048]

class PIOASMError(Exception):
    """
        This exception is raised from `asm_pio()` or `asm_pio_encode()` if there is
        an error assembling a PIO program.
    """
def asm_pio(*,
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
class StateMachine:

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
class Flash:
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
    def ioctl(self, op: int, arg: int) -> int | None: ...
    #
    @overload
    def ioctl(self, op: int) -> int | None:
        """
        These methods implement the simple and extended
        :ref:`block protocol <block-device-interface>` defined by
        :class:`vfs.AbstractBlockDev`.
        """
