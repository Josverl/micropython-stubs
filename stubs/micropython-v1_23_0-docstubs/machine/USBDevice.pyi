""" """

from __future__ import annotations
from typing import Any, Optional
from _typeshed import Incomplete

class USBDevice:
    """
    Construct a USBDevice object.

    ``Note:`` This object is a singleton, each call to this constructor
              returns the same object reference.
    """

    BUILTIN_NONE: Incomplete
    BUILTIN_DEFAULT: Incomplete
    BUILTIN_CDC: Incomplete
    BUILTIN_MSC: Incomplete
    BUILTIN_CDC_MSC: int
    """\
    These constant objects hold the built-in descriptor data which is
    compiled into the MicroPython firmware. ``USBDevice.BUILTIN_NONE`` and
    ``USBDevice.BUILTIN_DEFAULT`` are always present. Additional objects may be present
    depending on the firmware build configuration and the actual built-in drivers.
    
    ``Note:`` Currently at most one of ``USBDevice.BUILTIN_CDC``,
    ``USBDevice.BUILTIN_MSC`` and ``USBDevice.BUILTIN_CDC_MSC`` is defined
    and will be the same object as ``USBDevice.BUILTIN_DEFAULT``.
    These constants are defined to allow run-time detection of
    the built-in driver (if any). Support for selecting one of
    multiple built-in driver configurations may be added in the
    future.
    
    These values are assigned to :data:`USBDevice.builtin_driver` to get/set the
    built-in configuration.
    
    Each object contains the following read-only fields:
    
    - ``itf_max`` - One more than the highest bInterfaceNumber value used
    in the built-in configuration descriptor.
    - ``ep_max`` - One more than the highest bEndpointAddress value used
    in the built-in configuration descriptor. Does not include any
    ``IN`` flag bit (0x80).
    - ``str_max`` - One more than the highest string descriptor index
    value used by any built-in descriptor.
    - ``desc_dev`` - ``bytes`` object containing the built-in USB device
    descriptor.
    - ``desc_cfg`` - ``bytes`` object containing the complete built-in USB
    configuration descriptor.
    """
    def __init__(self) -> None: ...
    def config(self, desc_dev, desc_cfg, desc_strs=None, open_itf_cb=None, reset_cb=None, control_xfer_cb=None, xfer_cb=None) -> None:
        """
        Configures the ``USBDevice`` singleton object with the USB runtime device
        state and callback functions:

        - ``desc_dev`` - A bytes-like object containing
          the new USB device descriptor.

        - ``desc_cfg`` - A bytes-like object containing the
          new USB configuration descriptor.

        - ``desc_strs`` - Optional object holding strings or bytes objects
           containing USB string descriptor values. Can be a list, a dict, or any
           object which supports subscript indexing with integer keys (USB string
           descriptor index).

           Strings are an optional USB feature, and this parameter can be unset
           (default) if no strings are referenced in the device and configuration
           descriptors, or if only built-in strings should be used.

           Apart from index 0, all the string values should be plain ASCII. Index 0
           is the special "languages" USB descriptor, represented as a bytes object
           with a custom format defined in the USB standard. ``None`` can be
           returned at index 0 in order to use a default "English" language
           descriptor.

           To fall back to providing a built-in string value for a given index, a
           subscript lookup can return ``None``, raise ``KeyError``, or raise
           ``IndexError``.

        - ``open_itf_cb`` - This callback is called once for each interface
          or Interface Association Descriptor in response to a Set
          Configuration request from the USB Host (the final stage before
          the USB device is available to the host).

          The callback takes a single argument, which is a memoryview of the
          interface or IAD descriptor that the host is accepting (including
          all associated descriptors). It is a view into the same
          ``desc_cfg`` object that was provided as a separate
          argument to this function. The memoryview is only valid until the
          callback function returns.

        - ``reset_cb`` - This callback is called when the USB host performs
          a bus reset. The callback takes no arguments. Any in-progress
          transfers will never complete. The USB host will most likely
          proceed to re-enumerate the USB device by calling the descriptor
          callbacks and then ``open_itf_cb()``.

        - ``control_xfer_cb`` - This callback is called one or more times
          for each USB control transfer (device Endpoint 0). It takes two
          arguments.

          The first argument is the control transfer stage. It is one of:

          - ``1`` for SETUP stage.
          - ``2`` for DATA stage.
          - ``3`` for ACK stage.

          Second argument is a memoryview to read the USB control request
          data for this stage. The memoryview is only valid until the
          callback function returns. Data in this memoryview will be the same
          across each of the three stages of a single transfer.

          A successful transfer consists of this callback being called in sequence
          for the three stages. Generally speaking, if a device wants to do
          something in response to a control request then it's best to wait until
          the ACK stage to confirm the host controller completed the transfer as
          expected.

          The callback should return one of the following values:

          - ``False`` to stall the endpoint and reject the transfer. It won't
            proceed to any remaining stages.
          - ``True`` to continue the transfer to the next stage.
          - A buffer object can be returned at the SETUP stage when the transfer
            will send or receive additional data. Typically this is the case when
            the ``wLength`` field in the request has a non-zero value. This should
            be a writable buffer for an ``OUT`` direction transfer, or a readable
            buffer with data for an ``IN`` direction transfer.

        - ``xfer_cb`` - This callback is called whenever a non-control
          transfer submitted by calling :func:`USBDevice.submit_xfer` completes.

          The callback has three arguments:

          1. The Endpoint number for the completed transfer.
          2. Result value: ``True`` if the transfer succeeded, ``False``
             otherwise.
          3. Number of bytes successfully transferred. In the case of a
             "short" transfer, The result is ``True`` and ``xferred_bytes``
             will be smaller than the length of the buffer submitted for the
             transfer.

          ``Note:`` If a bus reset occurs (see :func:`USBDevice.reset`),
                    ``xfer_cb`` is not called for any transfers that have not
                    already completed.
        """
        ...

    def active(self, value: Optional[Any] = None) -> bool:
        """
        Returns the current active state of this runtime USB device as a
        boolean. The runtime USB device is "active" when it is available to
        interact with the host, it doesn't mean that a USB Host is actually
        present.

        If the optional ``value`` argument is set to a truthy value, then
        the USB device will be activated.

        If the optional ``value`` argument is set to a falsey value, then
        the USB device is deactivated. While the USB device is deactivated,
        it will not be detected by the USB Host.

        To simulate a disconnect and a reconnect of the USB device, call
        ``active(False)`` followed by ``active(True)``. This may be
        necessary if the runtime device configuration has changed, so that
        the host sees the new device.
        """
        ...

    def submit_xfer(self, ep, buffer) -> bool:
        """
        Submit a USB transfer on endpoint number ``ep``. ``buffer`` must be
        an object implementing the buffer interface, with read access for
        ``IN`` endpoints and write access for ``OUT`` endpoints.

        ``Note:`` ``ep`` cannot be the control Endpoint number 0. Control
           transfers are built up through successive executions of
           ``control_xfer_cb``, see above.

        Returns ``True`` if successful, ``False`` if the transfer could not
        be queued (as USB device is not configured by host, or because
        another transfer is queued on this endpoint.)

        When the USB host completes the transfer, the ``xfer_cb`` callback
        is called (see above).

        Raises ``OSError`` with reason ``MP_EINVAL`` If the USB device is not
        active.
        """
        ...

    def stall(self, ep, stall: Optional[Any] = None) -> Incomplete:
        """
        Calling this function gets or sets the STALL state of a device endpoint.

        ``ep`` is the number of the endpoint.

        If the optional ``stall`` parameter is set, this is a boolean flag
        for the STALL state.

        The return value is the current stall state of the endpoint (before
        any change made by this function).

        An endpoint that is set to STALL may remain stalled until this
        function is called again, or STALL may be cleared automatically by
        the USB host.

        Raises ``OSError`` with reason ``MP_EINVAL`` If the USB device is not
        active.
        """
        ...
