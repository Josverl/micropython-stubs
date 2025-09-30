""" """

from __future__ import annotations
from _typeshed import Incomplete
from typing_extensions import TypeVar, TypeAlias, Awaitable

class I2CTarget:
    """
    Construct and return a new I2CTarget object using the following parameters:

       - *id* identifies a particular I2C peripheral.  Allowed values depend on the
         particular port/board.  Some ports have a default in which case this parameter
         can be omitted.
       - *addr* is the I2C address of the target.
       - *addrsize* is the number of bits in the I2C target address.  Valid values
         are 7 and 10.
       - *mem* is an object with the buffer protocol that is writable.  If not
         specified then there is no backing memory and data must be read/written
         using the :meth:`I2CTarget.readinto` and :meth:`I2CTarget.write` methods.
       - *mem_addrsize* is the number of bits in the memory address.  Valid values
         are 0, 8, 16, 24 and 32.
       - *scl* is a pin object specifying the pin to use for SCL.
       - *sda* is a pin object specifying the pin to use for SDA.

    Note that some ports/boards will have default values of *scl* and *sda*
    that can be changed in this constructor.  Others will have fixed values
    of *scl* and *sda* that cannot be changed.
    """

    IRQ_ADDR_MATCH_READ: Incomplete
    """IRQ trigger sources."""
    IRQ_ADDR_MATCH_WRITE: Incomplete
    """IRQ trigger sources."""
    IRQ_READ_REQ: Incomplete
    """IRQ trigger sources."""
    IRQ_WRITE_REQ: Incomplete
    """IRQ trigger sources."""
    IRQ_END_READ: Incomplete
    """IRQ trigger sources."""
    IRQ_END_WRITE: Incomplete
    """IRQ trigger sources."""
    def __init__(self, id, addr, *, addrsize=7, mem=None, mem_addrsize=8, scl=None, sda=None) -> None: ...
    def deinit(self) -> Incomplete:
        """
        Deinitialise the I2C target.  After this method is called the hardware will no
        longer respond to requests on the I2C bus, and no other methods can be called.
        """
        ...
    def readinto(self, buf) -> int:
        """
        Read into the given buffer any pending bytes written by the I2C controller.
        Returns the number of bytes read.
        """
        ...
    def write(self, buf) -> int:
        """
        Write out the bytes from the given buffer, to be passed to the I2C controller
        after it sends a read request.  Returns the number of bytes written.  Most ports
        only accept one byte at a time to this method.
        """
        ...
    def irq(self, handler=None, trigger=IRQ_END_READ | IRQ_END_WRITE, hard=False) -> Incomplete:
        """
        Configure an IRQ *handler* to be called when an event occurs.  The possible events are
        given by the following constants, which can be or'd together and passed to the *trigger*
        argument:

           - ``IRQ_ADDR_MATCH_READ`` indicates that the target was addressed by a
             controller for a read transaction.
           - ``IRQ_ADDR_MATCH_READ`` indicates that the target was addressed by a
             controller for a write transaction.
           - ``IRQ_READ_REQ`` indicates that the controller is requesting data, and this
             request must be satisfied by calling `I2CTarget.write` with the data to be
             passed back to the controller.
           - ``IRQ_WRITE_REQ`` indicates that the controller has written data, and the
             data must be read by calling `I2CTarget.readinto`.
           - ``IRQ_END_READ`` indicates that the controller has finished a read transaction.
           - ``IRQ_END_WRITE`` indicates that the controller has finished a write transaction.

        Not all triggers are available on all ports.  If a port has the constant then that
        event is available.

        Note the following restrictions:

           - ``IRQ_ADDR_MATCH_READ``, ``IRQ_ADDR_MATCH_READ``, ``IRQ_READ_REQ`` and
             ``IRQ_WRITE_REQ`` must be handled by a hard IRQ callback (with the *hard* argument
             set to ``True``).  This is because these events have very strict timing requirements
             and must usually be satisfied synchronously with the hardware event.

           - ``IRQ_END_READ`` and ``IRQ_END_WRITE`` may be handled by either a soft or hard
             IRQ callback (although note that all events must be registered with the same handler,
             so if any events need a hard callback then all events must be hard).

           - If a memory buffer has been supplied in the constructor then ``IRQ_END_WRITE``
             is not emitted for the transaction that writes the memory address.  This is to
             allow ``IRQ_END_READ`` and ``IRQ_END_WRITE`` to function correctly as soft IRQ
             callbacks, where the IRQ handler may be called quite some time after the actual
             hardware event.
        """
        ...
