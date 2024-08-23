""" """

from __future__ import annotations
from typing import Any, Optional
from _typeshed import Incomplete

class DMA:
    """
    Claim one of the DMA controller channels for exclusive use.
    """

    def __init__(self) -> None: ...
    def config(self, read=None, write=None, count=None, ctrl=None, trigger=False) -> None:
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

    def irq(self, handler=None, hard=False) -> Incomplete:
        """
        Returns the IRQ object for this DMA channel and optionally configures it.
        """
        ...

    def close(self) -> Incomplete:
        """
        Release the claim on the underlying DMA channel and free the interrupt
        handler. The :class:`DMA` object can not be used after this operation.
        """
        ...

    def pack_ctrl(self, default=None, *kwargs) -> Incomplete:
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

    def unpack_ctrl(self, value) -> Incomplete:
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

    def active(self, value: Optional[Any] = None) -> Incomplete:
        """
        Gets or sets whether the DMA channel is currently running.

        >>> sm.active()
        0
        >>> sm.active(1)
        >>> while sm.active():
        """
        ...
