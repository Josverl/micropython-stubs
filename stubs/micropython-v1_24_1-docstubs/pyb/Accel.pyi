""" """

from __future__ import annotations
from _typeshed import Incomplete
from typing import NoReturn, overload, Tuple
from typing_extensions import TypeVar, TypeAlias, Awaitable
from _mpy_shed import HID_Tuple, _OldAbstractBlockDev, _OldAbstractReadOnlyBlockDev
from array import array
from collections.abc import Sequence
from pyb.ADC import ADC
from pyb.CAN import CAN
from pyb.DAC import DAC
from pyb.ExtInt import ExtInt
from pyb.Flash import Flash
from pyb.I2C import I2C
from pyb.LCD import LCD
from pyb.LED import LED
from pyb.Pin import Pin
from pyb.RTC import RTC
from pyb.SPI import SPI
from pyb.Servo import Servo
from pyb.Switch import Switch
from pyb.Timer import Timer
from pyb.UART import UART
from pyb.USB_HID import USB_HID
from pyb.USB_VCP import USB_VCP
from vfs import AbstractBlockDev

class Accel:
    """
    Accel is an object that controls the accelerometer.  Example usage::

        accel = pyb.Accel()
        for i in range(10):
            print(accel.x(), accel.y(), accel.z())

    Raw values are between -32 and 31.
    """

    def __init__(self) -> None:
        """
        Create and return an accelerometer object.
        """

    def filtered_xyz(self) -> Tuple:
        """
        Get a 3-tuple of filtered x, y and z values.

        Implementation note: this method is currently implemented as taking the
        sum of 4 samples, sampled from the 3 previous calls to this function along
        with the sample from the current call.  Returned values are therefore 4
        times the size of what they would be from the raw x(), y() and z() calls.
        """
        ...

    def tilt(self) -> int:
        """
        Get the tilt register.
        """
        ...

    def x(self) -> int:
        """
        Get the x-axis value.
        """
        ...

    def y(self) -> int:
        """
        Get the y-axis value.
        """
        ...

    def z(self) -> int:
        """
        Get the z-axis value.
        """
        ...

@overload
def freq() -> tuple[int, int, int, int]:
    """
    If given no arguments, returns a tuple of clock frequencies:
    (sysclk, hclk, pclk1, pclk2).
    These correspond to:

     - sysclk: frequency of the CPU
     - hclk: frequency of the AHB bus, core memory and DMA
     - pclk1: frequency of the APB1 bus
     - pclk2: frequency of the APB2 bus

    If given any arguments then the function sets the frequency of the CPU,
    and the buses if additional arguments are given.  Frequencies are given in
    Hz.  Eg freq(120000000) sets sysclk (the CPU frequency) to 120MHz.  Note that
    not all values are supported and the largest supported frequency not greater
    than the given value will be selected.

    Supported sysclk frequencies are (in MHz): 8, 16, 24, 30, 32, 36, 40, 42, 48,
    54, 56, 60, 64, 72, 84, 96, 108, 120, 144, 168.

    The maximum frequency of hclk is 168MHz, of pclk1 is 42MHz, and of pclk2 is
    84MHz.  Be sure not to set frequencies above these values.

    The hclk, pclk1 and pclk2 frequencies are derived from the sysclk frequency
    using a prescaler (divider).  Supported prescalers for hclk are: 1, 2, 4, 8,
    16, 64, 128, 256, 512.  Supported prescalers for pclk1 and pclk2 are: 1, 2,
    4, 8.  A prescaler will be chosen to best match the requested frequency.

    A sysclk frequency of
    8MHz uses the HSE (external crystal) directly and 16MHz uses the HSI
    (internal oscillator) directly.  The higher frequencies use the HSE to
    drive the PLL (phase locked loop), and then use the output of the PLL.

    Note that if you change the frequency while the USB is enabled then
    the USB may become unreliable.  It is best to change the frequency
    in boot.py, before the USB peripheral is started.  Also note that sysclk
    frequencies below 36MHz do not allow the USB to function correctly.
    """

@overload
def freq(sysclk: int, /) -> None:
    """
    If given no arguments, returns a tuple of clock frequencies:
    (sysclk, hclk, pclk1, pclk2).
    These correspond to:

     - sysclk: frequency of the CPU
     - hclk: frequency of the AHB bus, core memory and DMA
     - pclk1: frequency of the APB1 bus
     - pclk2: frequency of the APB2 bus

    If given any arguments then the function sets the frequency of the CPU,
    and the buses if additional arguments are given.  Frequencies are given in
    Hz.  Eg freq(120000000) sets sysclk (the CPU frequency) to 120MHz.  Note that
    not all values are supported and the largest supported frequency not greater
    than the given value will be selected.

    Supported sysclk frequencies are (in MHz): 8, 16, 24, 30, 32, 36, 40, 42, 48,
    54, 56, 60, 64, 72, 84, 96, 108, 120, 144, 168.

    The maximum frequency of hclk is 168MHz, of pclk1 is 42MHz, and of pclk2 is
    84MHz.  Be sure not to set frequencies above these values.

    The hclk, pclk1 and pclk2 frequencies are derived from the sysclk frequency
    using a prescaler (divider).  Supported prescalers for hclk are: 1, 2, 4, 8,
    16, 64, 128, 256, 512.  Supported prescalers for pclk1 and pclk2 are: 1, 2,
    4, 8.  A prescaler will be chosen to best match the requested frequency.

    A sysclk frequency of
    8MHz uses the HSE (external crystal) directly and 16MHz uses the HSI
    (internal oscillator) directly.  The higher frequencies use the HSE to
    drive the PLL (phase locked loop), and then use the output of the PLL.

    Note that if you change the frequency while the USB is enabled then
    the USB may become unreliable.  It is best to change the frequency
    in boot.py, before the USB peripheral is started.  Also note that sysclk
    frequencies below 36MHz do not allow the USB to function correctly.
    """

@overload
def freq(sysclk: int, hclk: int, /) -> None:
    """
    If given no arguments, returns a tuple of clock frequencies:
    (sysclk, hclk, pclk1, pclk2).
    These correspond to:

     - sysclk: frequency of the CPU
     - hclk: frequency of the AHB bus, core memory and DMA
     - pclk1: frequency of the APB1 bus
     - pclk2: frequency of the APB2 bus

    If given any arguments then the function sets the frequency of the CPU,
    and the buses if additional arguments are given.  Frequencies are given in
    Hz.  Eg freq(120000000) sets sysclk (the CPU frequency) to 120MHz.  Note that
    not all values are supported and the largest supported frequency not greater
    than the given value will be selected.

    Supported sysclk frequencies are (in MHz): 8, 16, 24, 30, 32, 36, 40, 42, 48,
    54, 56, 60, 64, 72, 84, 96, 108, 120, 144, 168.

    The maximum frequency of hclk is 168MHz, of pclk1 is 42MHz, and of pclk2 is
    84MHz.  Be sure not to set frequencies above these values.

    The hclk, pclk1 and pclk2 frequencies are derived from the sysclk frequency
    using a prescaler (divider).  Supported prescalers for hclk are: 1, 2, 4, 8,
    16, 64, 128, 256, 512.  Supported prescalers for pclk1 and pclk2 are: 1, 2,
    4, 8.  A prescaler will be chosen to best match the requested frequency.

    A sysclk frequency of
    8MHz uses the HSE (external crystal) directly and 16MHz uses the HSI
    (internal oscillator) directly.  The higher frequencies use the HSE to
    drive the PLL (phase locked loop), and then use the output of the PLL.

    Note that if you change the frequency while the USB is enabled then
    the USB may become unreliable.  It is best to change the frequency
    in boot.py, before the USB peripheral is started.  Also note that sysclk
    frequencies below 36MHz do not allow the USB to function correctly.
    """

@overload
def freq(sysclk: int, hclk: int, pclk1: int, /) -> None:
    """
    If given no arguments, returns a tuple of clock frequencies:
    (sysclk, hclk, pclk1, pclk2).
    These correspond to:

     - sysclk: frequency of the CPU
     - hclk: frequency of the AHB bus, core memory and DMA
     - pclk1: frequency of the APB1 bus
     - pclk2: frequency of the APB2 bus

    If given any arguments then the function sets the frequency of the CPU,
    and the buses if additional arguments are given.  Frequencies are given in
    Hz.  Eg freq(120000000) sets sysclk (the CPU frequency) to 120MHz.  Note that
    not all values are supported and the largest supported frequency not greater
    than the given value will be selected.

    Supported sysclk frequencies are (in MHz): 8, 16, 24, 30, 32, 36, 40, 42, 48,
    54, 56, 60, 64, 72, 84, 96, 108, 120, 144, 168.

    The maximum frequency of hclk is 168MHz, of pclk1 is 42MHz, and of pclk2 is
    84MHz.  Be sure not to set frequencies above these values.

    The hclk, pclk1 and pclk2 frequencies are derived from the sysclk frequency
    using a prescaler (divider).  Supported prescalers for hclk are: 1, 2, 4, 8,
    16, 64, 128, 256, 512.  Supported prescalers for pclk1 and pclk2 are: 1, 2,
    4, 8.  A prescaler will be chosen to best match the requested frequency.

    A sysclk frequency of
    8MHz uses the HSE (external crystal) directly and 16MHz uses the HSI
    (internal oscillator) directly.  The higher frequencies use the HSE to
    drive the PLL (phase locked loop), and then use the output of the PLL.

    Note that if you change the frequency while the USB is enabled then
    the USB may become unreliable.  It is best to change the frequency
    in boot.py, before the USB peripheral is started.  Also note that sysclk
    frequencies below 36MHz do not allow the USB to function correctly.
    """

@overload
def freq(sysclk: int, hclk: int, pclk1: int, pclk2: int, /) -> None:
    """
    If given no arguments, returns a tuple of clock frequencies:
    (sysclk, hclk, pclk1, pclk2).
    These correspond to:

     - sysclk: frequency of the CPU
     - hclk: frequency of the AHB bus, core memory and DMA
     - pclk1: frequency of the APB1 bus
     - pclk2: frequency of the APB2 bus

    If given any arguments then the function sets the frequency of the CPU,
    and the buses if additional arguments are given.  Frequencies are given in
    Hz.  Eg freq(120000000) sets sysclk (the CPU frequency) to 120MHz.  Note that
    not all values are supported and the largest supported frequency not greater
    than the given value will be selected.

    Supported sysclk frequencies are (in MHz): 8, 16, 24, 30, 32, 36, 40, 42, 48,
    54, 56, 60, 64, 72, 84, 96, 108, 120, 144, 168.

    The maximum frequency of hclk is 168MHz, of pclk1 is 42MHz, and of pclk2 is
    84MHz.  Be sure not to set frequencies above these values.

    The hclk, pclk1 and pclk2 frequencies are derived from the sysclk frequency
    using a prescaler (divider).  Supported prescalers for hclk are: 1, 2, 4, 8,
    16, 64, 128, 256, 512.  Supported prescalers for pclk1 and pclk2 are: 1, 2,
    4, 8.  A prescaler will be chosen to best match the requested frequency.

    A sysclk frequency of
    8MHz uses the HSE (external crystal) directly and 16MHz uses the HSI
    (internal oscillator) directly.  The higher frequencies use the HSE to
    drive the PLL (phase locked loop), and then use the output of the PLL.

    Note that if you change the frequency while the USB is enabled then
    the USB may become unreliable.  It is best to change the frequency
    in boot.py, before the USB peripheral is started.  Also note that sysclk
    frequencies below 36MHz do not allow the USB to function correctly.
    """

@overload
def freq(self) -> int:
    """
    Get or set the frequency for the timer (changes prescaler and period if set).
    """

@overload
def freq(self, value: int, /) -> None:
    """
    Get or set the frequency for the timer (changes prescaler and period if set).
    """

@overload
def hid(data: tuple[int, int, int, int], /) -> None:
    """
    Takes a 4-tuple (or list) and sends it to the USB host (the PC) to
    signal a HID mouse-motion event.

    ``Note:`` This function is deprecated.  Use :meth:`pyb.USB_HID.send()` instead.
    """

@overload
def hid(data: Sequence[int], /) -> None:
    """
    Takes a 4-tuple (or list) and sends it to the USB host (the PC) to
    signal a HID mouse-motion event.

    ``Note:`` This function is deprecated.  Use :meth:`pyb.USB_HID.send()` instead.
    """

@overload
def info() -> None:
    """
    Print out lots of information about the board.
    """

@overload
def info(dump_alloc_table: bytes, /) -> None:
    """
    Print out lots of information about the board.
    """

@overload
def info(self) -> list[int]:
    """
    Get information about the controller's error states and TX and RX buffers.
    If *list* is provided then it should be a list object with at least 8 entries,
    which will be filled in with the information.  Otherwise a new list will be
    created and filled in.  In both cases the return value of the method is the
    populated list.

    The values in the list are:

    - TEC value
    - REC value
    - number of times the controller enterted the Error Warning state (wrapped
      around to 0 after 65535)
    - number of times the controller enterted the Error Passive state (wrapped
      around to 0 after 65535)
    - number of times the controller enterted the Bus Off state (wrapped
      around to 0 after 65535)
    - number of pending TX messages
    - number of pending RX messages on fifo 0
    - number of pending RX messages on fifo 1
    """

@overload
def info(self, list: list[int], /) -> list[int]:
    """
    Get information about the controller's error states and TX and RX buffers.
    If *list* is provided then it should be a list object with at least 8 entries,
    which will be filled in with the information.  Otherwise a new list will be
    created and filled in.  In both cases the return value of the method is the
    populated list.

    The values in the list are:

    - TEC value
    - REC value
    - number of times the controller enterted the Error Warning state (wrapped
      around to 0 after 65535)
    - number of times the controller enterted the Error Passive state (wrapped
      around to 0 after 65535)
    - number of times the controller enterted the Bus Off state (wrapped
      around to 0 after 65535)
    - number of pending TX messages
    - number of pending RX messages on fifo 0
    - number of pending RX messages on fifo 1
    """

@overload
def mount(
    device: _OldAbstractReadOnlyBlockDev,
    mountpoint: str,
    /,
    *,
    readonly: bool = False,
    mkfs: bool = False,
) -> None:
    """
    ``Note:`` This function is deprecated. Mounting and unmounting devices should
       be performed by :meth:`vfs.mount` and :meth:`vfs.umount` instead.

    Mount a block device and make it available as part of the filesystem.
    ``device`` must be an object that provides the block protocol. (The
    following is also deprecated. See :class:`vfs.AbstractBlockDev` for the
    correct way to create a block device.)

     - ``readblocks(self, blocknum, buf)``
     - ``writeblocks(self, blocknum, buf)`` (optional)
     - ``count(self)``
     - ``sync(self)`` (optional)

    ``readblocks`` and ``writeblocks`` should copy data between ``buf`` and
    the block device, starting from block number ``blocknum`` on the device.
    ``buf`` will be a bytearray with length a multiple of 512.  If
    ``writeblocks`` is not defined then the device is mounted read-only.
    The return value of these two functions is ignored.

    ``count`` should return the number of blocks available on the device.
    ``sync``, if implemented, should sync the data on the device.

    The parameter ``mountpoint`` is the location in the root of the filesystem
    to mount the device.  It must begin with a forward-slash.

    If ``readonly`` is ``True``, then the device is mounted read-only,
    otherwise it is mounted read-write.

    If ``mkfs`` is ``True``, then a new filesystem is created if one does not
    already exist.
    """

@overload
def mount(
    device: _OldAbstractBlockDev,
    mountpoint: str,
    /,
    *,
    readonly: bool = False,
    mkfs: bool = False,
) -> None:
    """
    ``Note:`` This function is deprecated. Mounting and unmounting devices should
       be performed by :meth:`vfs.mount` and :meth:`vfs.umount` instead.

    Mount a block device and make it available as part of the filesystem.
    ``device`` must be an object that provides the block protocol. (The
    following is also deprecated. See :class:`vfs.AbstractBlockDev` for the
    correct way to create a block device.)

     - ``readblocks(self, blocknum, buf)``
     - ``writeblocks(self, blocknum, buf)`` (optional)
     - ``count(self)``
     - ``sync(self)`` (optional)

    ``readblocks`` and ``writeblocks`` should copy data between ``buf`` and
    the block device, starting from block number ``blocknum`` on the device.
    ``buf`` will be a bytearray with length a multiple of 512.  If
    ``writeblocks`` is not defined then the device is mounted read-only.
    The return value of these two functions is ignored.

    ``count`` should return the number of blocks available on the device.
    ``sync``, if implemented, should sync the data on the device.

    The parameter ``mountpoint`` is the location in the root of the filesystem
    to mount the device.  It must begin with a forward-slash.

    If ``readonly`` is ``True``, then the device is mounted read-only,
    otherwise it is mounted read-write.

    If ``mkfs`` is ``True``, then a new filesystem is created if one does not
    already exist.
    """

@overload
def repl_uart() -> UART | None:
    """
    Get or set the UART object where the REPL is repeated on.
    """

@overload
def repl_uart(uart: UART, /) -> None:
    """
    Get or set the UART object where the REPL is repeated on.
    """

# noinspection PyShadowingNames
@overload
def usb_mode() -> str:
    """
    If called with no arguments, return the current USB mode as a string.

    If called with *modestr* provided, attempts to configure the USB mode.
    The following values of *modestr* are understood:

    - ``None``: disables USB
    - ``'VCP'``: enable with VCP (Virtual COM Port) interface
    - ``'MSC'``: enable with MSC (mass storage device class) interface
    - ``'VCP+MSC'``: enable with VCP and MSC
    - ``'VCP+HID'``: enable with VCP and HID (human interface device)
    - ``'VCP+MSC+HID'``: enabled with VCP, MSC and HID (only available on PYBD boards)

    For backwards compatibility, ``'CDC'`` is understood to mean
    ``'VCP'`` (and similarly for ``'CDC+MSC'`` and ``'CDC+HID'``).

    The *port* parameter should be an integer (0, 1, ...) and selects which
    USB port to use if the board supports multiple ports.  A value of -1 uses
    the default or automatically selected port.

    The *vid* and *pid* parameters allow you to specify the VID (vendor id)
    and PID (product id).  A *pid* value of -1 will select a PID based on the
    value of *modestr*.

    If enabling MSC mode, the *msc* parameter can be used to specify a list
    of SCSI LUNs to expose on the mass storage interface.  For example
    ``msc=(pyb.Flash(), pyb.SDCard())``.

    If enabling HID mode, you may also specify the HID details by
    passing the *hid* keyword parameter.  It takes a tuple of
    (subclass, protocol, max packet length, polling interval, report
    descriptor).  By default it will set appropriate values for a USB
    mouse.  There is also a ``pyb.hid_keyboard`` constant, which is an
    appropriate tuple for a USB keyboard.

    The *high_speed* parameter, when set to ``True``, enables USB HS mode if
    it is supported by the hardware.
    """

# noinspection PyShadowingNames
@overload
def usb_mode(
    modestr: str,
    /,
    *,
    port: int = -1,
    vid: int = 0xF055,
    pid: int = -1,
    msc: Sequence[AbstractBlockDev] = (),
    hid: tuple[int, int, int, int, bytes] = hid_mouse,
    high_speed: bool = False,
) -> None:
    """
    If called with no arguments, return the current USB mode as a string.

    If called with *modestr* provided, attempts to configure the USB mode.
    The following values of *modestr* are understood:

    - ``None``: disables USB
    - ``'VCP'``: enable with VCP (Virtual COM Port) interface
    - ``'MSC'``: enable with MSC (mass storage device class) interface
    - ``'VCP+MSC'``: enable with VCP and MSC
    - ``'VCP+HID'``: enable with VCP and HID (human interface device)
    - ``'VCP+MSC+HID'``: enabled with VCP, MSC and HID (only available on PYBD boards)

    For backwards compatibility, ``'CDC'`` is understood to mean
    ``'VCP'`` (and similarly for ``'CDC+MSC'`` and ``'CDC+HID'``).

    The *port* parameter should be an integer (0, 1, ...) and selects which
    USB port to use if the board supports multiple ports.  A value of -1 uses
    the default or automatically selected port.

    The *vid* and *pid* parameters allow you to specify the VID (vendor id)
    and PID (product id).  A *pid* value of -1 will select a PID based on the
    value of *modestr*.

    If enabling MSC mode, the *msc* parameter can be used to specify a list
    of SCSI LUNs to expose on the mass storage interface.  For example
    ``msc=(pyb.Flash(), pyb.SDCard())``.

    If enabling HID mode, you may also specify the HID details by
    passing the *hid* keyword parameter.  It takes a tuple of
    (subclass, protocol, max packet length, polling interval, report
    descriptor).  By default it will set appropriate values for a USB
    mouse.  There is also a ``pyb.hid_keyboard`` constant, which is an
    appropriate tuple for a USB keyboard.

    The *high_speed* parameter, when set to ``True``, enables USB HS mode if
    it is supported by the hardware.
    """
