"""
Functionality specific to STM32 MCUs.

MicroPython module: https://docs.micropython.org/en/v1.23.0/library/stm.html

This module provides functionality specific to STM32 microcontrollers, including
direct access to peripheral registers.
"""

# source version: v1.23.0
# origin module:: repos/micropython/docs/library/stm.rst
from __future__ import annotations
from typing import Tuple
from _typeshed import Incomplete

mem8: bytearray
"""Read/write 8 bits of memory."""
mem16: bytearray
"""Read/write 16 bits of memory."""
mem32: bytearray
"""\
Read/write 32 bits of memory.

Use subscript notation ``[...]`` to index these objects with the address of
interest.

These memory objects can be used in combination with the peripheral register
constants to read and write registers of the MCU hardware peripherals, as well
as all other areas of address space.
"""
GPIOA: int
"""Base address of the GPIOA peripheral."""
GPIOB: int
"""Base address of the GPIOB peripheral."""
GPIO_BSRR: Incomplete
"""Offset of the GPIO bit set/reset register."""
GPIO_IDR: Incomplete
"""Offset of the GPIO input data register."""
GPIO_ODR: int
"""\
Offset of the GPIO output data register.

Constants that are named after a peripheral, like ``GPIOA``, are the absolute
address of that peripheral.  Constants that have a prefix which is the name of a
peripheral, like ``GPIO_BSRR``, are relative offsets of the register.  Accessing
peripheral registers requires adding the absolute base address of the peripheral
and the relative register offset.  For example ``GPIOA + GPIO_BSRR`` is the
full, absolute address of the ``GPIOA->BSRR`` register.

Example use:
"""

def rfcore_status() -> int:
    """
    Returns the status of the second CPU as an integer (the first word of device
    info table).
    """
    ...

def rfcore_fw_version(id) -> Tuple:
    """
    Get the version of the firmware running on the second CPU.  Pass in 0 for
    *id* to get the FUS version, and 1 to get the WS version.

    Returns a 5-tuple with the full version number.
    """
    ...

def rfcore_sys_hci(ogf, ocf, data, timeout_ms=0) -> bytes:
    """
    Execute a HCI command on the SYS channel.  The execution is synchronous.

    Returns a bytes object with the result of the SYS command.
    """
    ...

def subghz_cs(level) -> None:
    """
    Sets the internal SPI CS pin attached to the radio peripheral. The ``level``
    argument is active-low: a truthy value means "CS pin high" and de-asserts the
    signal, a falsey value means "CS pin low" and asserts the signal.

    The internal-only SPI bus corresponding to this CS signal can be instantiated
    using :ref:`machine.SPI()<machine.SPI>` ``id`` value ``"SUBGHZ"``.
    """
    ...

def subghz_irq(handler) -> None:
    """
    Sets the internal SUBGHZ radio interrupt handler to the provided
    function. The handler function is called as a "hard" interrupt in response to
    radio peripheral interrupts. See :ref:`isr_rules` for more information about
    interrupt handlers in MicroPython.

    Calling this function with the handler argument set to None disables the IRQ.

    Due to a hardware limitation, each time this IRQ fires MicroPython disables
    it before calling the handler. In order to receive another interrupt, Python
    code should call ``subghz_irq()`` to set the handler again. This has the side
    effect of re-enabling the IRQ.
    """
    ...

def subghz_is_busy() -> bool:
    """
    Return a ``bool`` corresponding to the internal "RFBUSYS" signal from the
    radio peripheral. Before sending a new command to the radio over SPI then
    this function should be polled until it returns ``False``, to confirm the
    busy signal is de-asserted.
    """
    ...
