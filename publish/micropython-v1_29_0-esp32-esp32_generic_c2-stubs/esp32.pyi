"""
Functionality specific to the ESP32.

MicroPython module: https://docs.micropython.org/en/v1.29.0/library/esp32.html

The ``esp32`` module contains functions and classes specifically aimed at
controlling ESP32 modules.

---
Module: 'esp32' on micropython-v1.29.0-esp32-ESP32_GENERIC_C2
"""

# MCU: {'variant': '', 'build': '', 'arch': 'rv32imc', 'port': 'esp32', 'board': 'ESP32_GENERIC_C2', 'board_id': 'ESP32_GENERIC_C2', 'mpy': 'v6.3', 'ver': '1.29.0', 'family': 'micropython', 'cpu': 'ESP32-C2', 'version': '1.29.0'}
# Stubber: v1.28.6
from __future__ import annotations

from typing import Any, Final, List, Sequence, Tuple, overload

from _mpy_shed import AnyReadableBuf
from _typeshed import Incomplete
from machine import Pin
from typing_extensions import Awaitable, TypeAlias, TypeVar
from vfs import AbstractBlockDev

WAKEUP_ANY_HIGH: Final[bool] = True
"""Selects the wake level for pins."""
WAKEUP_ALL_LOW: Final[bool] = False
"""Selects the wake level for pins."""
HEAP_EXEC: Final[int] = 1
"""Used in `idf_heap_info`."""
HEAP_DATA: Final[int] = 4
"""Used in `idf_heap_info`."""

def idf_heap_info(capabilities: int) -> List[Tuple]:
    """
    Returns information about the ESP-IDF heap memory regions. One of them contains
    the MicroPython heap and the others are used by ESP-IDF, e.g., for network
    buffers and other data. This data is useful to get a sense of how much memory
    is available to ESP-IDF and the networking stack in particular. It may shed
    some light on situations where ESP-IDF operations fail due to allocation failures.

    The capabilities parameter corresponds to ESP-IDF's ``MALLOC_CAP_XXX`` values but the
    two most useful ones are predefined as `esp32.HEAP_DATA` for data heap regions and
    `esp32.HEAP_EXEC` for executable regions as used by the native code emitter.

    The return value is a list of 4-tuples, where each 4-tuple corresponds to one heap
    and contains: the total bytes, the free bytes, the largest free block, and
    the minimum free seen over time.

    Example after booting::

        >>> import esp32; esp32.idf_heap_info(esp32.HEAP_DATA)
        [(240, 0, 0, 0), (7288, 0, 0, 0), (16648, 4, 4, 4), (79912, 35712, 35512, 35108),
         (15072, 15036, 15036, 15036), (113840, 0, 0, 0)]

    ``Note:`` Free IDF heap memory in the `esp32.HEAP_DATA` region is available
       to be automatically added to the MicroPython heap to prevent a
       MicroPython allocation from failing. However, the information returned
       here is otherwise *not* useful to troubleshoot Python allocation
       failures. :func:`micropython.mem_info()` and :func:`gc.mem_free()` should
       be used instead:

       The "max new split" value in :func:`micropython.mem_info()` output
       corresponds to the largest free block of ESP-IDF heap that could be
       automatically added on demand to the MicroPython heap.

       The result of :func:`gc.mem_free()` is the total of the current "free"
       and "max new split" values printed by :func:`micropython.mem_info()`.
    """
    ...

def mcu_temperature(*args, **kwargs) -> Incomplete: ...
@overload
def wake_on_gpio() -> None:
    """
    Configure how GPIO wakes the device from sleep.  *pins* can be ``None``
    or a tuple/list of valid Pin objects.  *level* should be ``esp32.WAKEUP_ALL_LOW``
    or ``esp32.WAKEUP_ANY_HIGH``.

    ``Note:`` Some boards don't support waking on GPIO from deep sleep,
       on those boards, the pins set here can only be used to wake from light sleep.
    """
    ...

@overload
def wake_on_gpio(pins: List[Pin] | Tuple[Pin, ...] | None, level: bool, /) -> None:
    """
    Configure how GPIO wakes the device from sleep.  *pins* can be ``None``
    or a tuple/list of valid Pin objects.  *level* should be ``esp32.WAKEUP_ALL_LOW``
    or ``esp32.WAKEUP_ANY_HIGH``.

    ``Note:`` Some boards don't support waking on GPIO from deep sleep,
       on those boards, the pins set here can only be used to wake from light sleep.
    """
    ...

class Partition(AbstractBlockDev):
    """
    This class gives access to the partitions in the device's flash memory and includes
    methods to enable over-the-air (OTA) updates.
    """

    RUNNING: Final[int] = 1
    """\
    Used in the `Partition` constructor to fetch various partitions: ``BOOT`` is the
    partition that will be booted at the next reset and ``RUNNING`` is the currently
    running partition.
    """
    TYPE_APP: Final[int] = 0
    """\
    Used in `Partition.find` to specify the partition type: ``APP`` is for bootable
    firmware partitions (typically labelled ``factory``, ``ota_0``, ``ota_1``), and
    ``DATA`` is for other partitions, e.g. ``nvs``, ``otadata``, ``phy_init``, ``vfs``.
    """
    TYPE_DATA: Final[int] = 1
    """\
    Used in `Partition.find` to specify the partition type: ``APP`` is for bootable
    firmware partitions (typically labelled ``factory``, ``ota_0``, ``ota_1``), and
    ``DATA`` is for other partitions, e.g. ``nvs``, ``otadata``, ``phy_init``, ``vfs``.
    """
    BOOT: Final[int] = 0
    """\
    Used in the `Partition` constructor to fetch various partitions: ``BOOT`` is the
    partition that will be booted at the next reset and ``RUNNING`` is the currently
    running partition.
    """

    @overload
    def readblocks(self, block_num: int, buf: bytearray) -> bool:
        """
        The first form reads aligned, multiples of blocks.
        Starting at the block given by the index *block_num*, read blocks from
        the device into *buf* (an array of bytes).
        The number of blocks to read is given by the length of *buf*,
        which will be a multiple of the block size.
        """

    @overload
    def readblocks(self, block_num: int, buf: bytearray, offset: int) -> bool:
        """
        The second form allows reading at arbitrary locations within a block,
        and arbitrary lengths.
        Starting at block index *block_num*, and byte offset within that block
        of *offset*, read bytes from the device into *buf* (an array of bytes).
        The number of bytes to read is given by the length of *buf*.
        """

    @overload
    def ioctl(self, op: int, arg) -> None:
        """
        These methods implement the simple and :ref:`extended
        <block-device-interface>` block protocol defined by
        :class:`vfs.AbstractBlockDev`.
        """
        ...

    @overload
    def ioctl(self, op: int) -> int:
        """
        These methods implement the simple and :ref:`extended
        <block-device-interface>` block protocol defined by
        :class:`vfs.AbstractBlockDev`.
        """
        ...
    def set_boot(self) -> None:
        """
        Sets the partition as the boot partition.

        ``Note:`` Do not enter :func:`deepsleep<machine.deepsleep>` after changing
           the OTA boot partition, without first performing a hard
           :func:`reset<machine.reset>` or power cycle. This ensures the bootloader
           will validate the new image before booting.
        """
        ...

    @overload
    def writeblocks(self, block_num: int, buf: bytes | bytearray, /) -> None:
        """
        The first form writes aligned, multiples of blocks, and requires that the
        blocks that are written to be first erased (if necessary) by this method.
        Starting at the block given by the index *block_num*, write blocks from
        *buf* (an array of bytes) to the device.
        The number of blocks to write is given by the length of *buf*,
        which will be a multiple of the block size.
        """

    @overload
    def writeblocks(self, block_num: int, buf: bytes | bytearray, offset: int, /) -> None:
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
    def info(self) -> Tuple:
        """
        Returns a 6-tuple ``(type, subtype, addr, size, label, encrypted)``.
        """
        ...
    @staticmethod
    def find(type: int = TYPE_APP, subtype: int = 0xFF, /, label: str | None = None) -> List:
        """
        Find a partition specified by *type*, *subtype* and *label*.  Returns a
        (possibly empty) list of Partition objects. Note: ``subtype=0xff`` matches any subtype
        and ``label=None`` matches any label.

        *block_size* specifies the byte size of an individual block used by the returned
        objects.
        """
        ...
    def get_next_update(self) -> Partition:
        """
        Gets the next update partition after this one, and returns a new Partition object.
        Typical usage is ``Partition(Partition.RUNNING).get_next_update()``
        which returns the next partition to update given the current running one.
        """
        ...
    @classmethod
    def mark_app_valid_cancel_rollback(cls) -> None:
        """
        Signals that the current boot is considered successful.
        Calling ``mark_app_valid_cancel_rollback`` is required on the first boot of a new
        partition to avoid an automatic rollback at the next boot.
        This uses the ESP-IDF "app rollback" feature with "CONFIG_BOOTLOADER_APP_ROLLBACK_ENABLE"
        and  an ``OSError(-261)`` is raised if called on firmware that doesn't have the
        feature enabled.
        It is OK to call ``mark_app_valid_cancel_rollback`` on every boot and it is not
        necessary when booting firmware that was loaded using esptool.
        """
        ...
    def __init__(self, id: str, block_size=4096, /) -> None:
        """
        Create an object representing a partition.

        """

class NVS:
    """
    This class gives access to the Non-Volatile storage managed by ESP-IDF. The NVS is partitioned
    into namespaces and each namespace contains typed key-value pairs. The keys are strings and the
    values may be various integer types, strings, and binary blobs. The driver currently only
    supports 32-bit signed integers and blobs.

    .. warning::

        Changes to NVS need to be committed to flash by calling the commit method. Failure
        to call commit results in changes being lost at the next reset.
    """
    def get_i32(self, key: str, /) -> int:
        """
        Returns the signed integer value for the specified key. Raises an OSError if the key does not
        exist or has a different type.
        """
        ...
    def set_i32(self, key: str, value: int, /) -> None:
        """
        Sets a 32-bit signed integer value for the specified key. Remember to call *commit*!
        """
        ...
    def set_blob(self, key: str, value: AnyReadableBuf, /) -> None:
        """
        Sets a binary blob value for the specified key. The value passed in must support the buffer
        protocol, e.g. bytes, bytearray, str. (Note that esp-idf distinguishes blobs and strings, this
        method always writes a blob even if a string is passed in as value.)
        Remember to call *commit*!
        """
        ...
    def commit(self) -> None:
        """
        Commits changes made by *set_xxx* methods to flash.
        """
        ...
    def get_blob(self, key: str, buffer: bytearray, /) -> int:
        """
        Reads the value of the blob for the specified key into the buffer, which must be a bytearray.
        Returns the actual length read. Raises an OSError if the key does not exist, has a different
        type, or if the buffer is too small.
        """
        ...
    def erase_key(self, key: str, /) -> None:
        """
        Erases a key-value pair.
        """
        ...
    def __init__(self, namespace: str, /) -> None:
        """
        Create an object providing access to a namespace (which is automatically created if not
        present).
        """

class PCNT:
    @overload
    def value(self, /) -> int:
        """
        Call this method with no arguments to return the current counter value.

        If the optional *value* argument is set to ``0`` then the counter is
        reset (but the previous value is returned). Read and reset is not atomic and
        so it is possible for a pulse to be missed. Any value other than ``0`` will
        raise an error.
        """
        ...

    @overload
    def value(self, value: int, /) -> int:
        """
        Call this method with no arguments to return the current counter value.

        If the optional *value* argument is set to ``0`` then the counter is
        reset (but the previous value is returned). Read and reset is not atomic and
        so it is possible for a pulse to be missed. Any value other than ``0`` will
        raise an error.
        """
        ...

class RMT:
    @overload
    def active(self, /) -> bool:
        """
        If called without parameters, returns *True* if there is an ongoing transmission.

        If called with parameter *False*, stops the ongoing transmission.
        This is useful to stop an infinite transmission loop.
        The current loop is finished and transmission stops.
        The object is not invalidated, and the RMT channel is again enabled when a new
        transmission is started.

        Calling with parameter *True* does not restart transmission. A new transmission
        should always be initiated by *write_pulses()*.
        """
        ...

    @overload
    def active(self, value: bool, /) -> bool:
        """
        If called without parameters, returns *True* if there is an ongoing transmission.

        If called with parameter *False*, stops the ongoing transmission.
        This is useful to stop an infinite transmission loop.
        The current loop is finished and transmission stops.
        The object is not invalidated, and the RMT channel is again enabled when a new
        transmission is started.

        Calling with parameter *True* does not restart transmission. A new transmission
        should always be initiated by *write_pulses()*.
        """
        ...

    @overload
    def write_pulses(self, duration: Sequence[int] | Tuple[int, ...], data: bool = True, /) -> None:
        """
        Begin transmitting a sequence. There are three ways to specify this:

        **Mode 1:** *duration* is a list or tuple of durations. The optional *data*
        argument specifies the initial output level. The output level will toggle
        after each duration.

        **Mode 2:** *duration* is a positive integer and *data* is a list or tuple
        of output levels. *duration* specifies a fixed duration for each.

        **Mode 3:** *duration* and *data* are lists or tuples of equal length,
        specifying individual durations and the output level for each.

        Durations are in integer units of the channel resolution (as
        described above), between 1 and ``PULSE_MAX`` units. Output levels
        are any value that can be converted to a boolean, with ``True``
        representing high voltage and ``False`` representing low.

        If transmission of an earlier sequence is in progress then this method will
        block until that transmission is complete before beginning the new sequence.

        If looping has been enabled with `RMT.loop`, the sequence will be
        repeated indefinitely. Further calls to this method will block until the
        end of the current loop iteration before immediately beginning to loop the
        new sequence of pulses. Looping sequences longer than 126 pulses is not
        supported by the hardware.
        """

    @overload
    def write_pulses(self, duration: int, data: Sequence[bool] | Tuple[bool, ...], /) -> None:
        """
        Begin transmitting a sequence. There are three ways to specify this:

        **Mode 1:** *duration* is a list or tuple of durations. The optional *data*
        argument specifies the initial output level. The output level will toggle
        after each duration.

        **Mode 2:** *duration* is a positive integer and *data* is a list or tuple
        of output levels. *duration* specifies a fixed duration for each.

        **Mode 3:** *duration* and *data* are lists or tuples of equal length,
        specifying individual durations and the output level for each.

        Durations are in integer units of the channel resolution (as
        described above), between 1 and ``PULSE_MAX`` units. Output levels
        are any value that can be converted to a boolean, with ``True``
        representing high voltage and ``False`` representing low.

        If transmission of an earlier sequence is in progress then this method will
        block until that transmission is complete before beginning the new sequence.

        If looping has been enabled with `RMT.loop`, the sequence will be
        repeated indefinitely. Further calls to this method will block until the
        end of the current loop iteration before immediately beginning to loop the
        new sequence of pulses. Looping sequences longer than 126 pulses is not
        supported by the hardware.
        """

    @overload
    def write_pulses(
        self,
        duration: Sequence[int] | Tuple[int, ...],
        data: List[bool] | Tuple[bool, ...] | int,
        /,
    ) -> None:
        """
        Begin transmitting a sequence. There are three ways to specify this:

        **Mode 1:** *duration* is a list or tuple of durations. The optional *data*
        argument specifies the initial output level. The output level will toggle
        after each duration.

        **Mode 2:** *duration* is a positive integer and *data* is a list or tuple
        of output levels. *duration* specifies a fixed duration for each.

        **Mode 3:** *duration* and *data* are lists or tuples of equal length,
        specifying individual durations and the output level for each.

        Durations are in integer units of the channel resolution (as
        described above), between 1 and ``PULSE_MAX`` units. Output levels
        are any value that can be converted to a boolean, with ``True``
        representing high voltage and ``False`` representing low.

        If transmission of an earlier sequence is in progress then this method will
        block until that transmission is complete before beginning the new sequence.

        If looping has been enabled with `RMT.loop`, the sequence will be
        repeated indefinitely. Further calls to this method will block until the
        end of the current loop iteration before immediately beginning to loop the
        new sequence of pulses. Looping sequences longer than 126 pulses is not
        supported by the hardware.
        """

@overload
def wake_on_ext0() -> None:
    """
    Configure how EXT0 wakes the device from sleep.  *pin* can be ``None``
    or a valid Pin object.  *level* should be ``esp32.WAKEUP_ALL_LOW`` or
    ``esp32.WAKEUP_ANY_HIGH``.

    ``Note:`` This is only available for boards that have ext0 support.
    """
    ...

@overload
def wake_on_ext0(pin: Pin | None, level: bool, /) -> None:
    """
    Configure how EXT0 wakes the device from sleep.  *pin* can be ``None``
    or a valid Pin object.  *level* should be ``esp32.WAKEUP_ALL_LOW`` or
    ``esp32.WAKEUP_ANY_HIGH``.

    ``Note:`` This is only available for boards that have ext0 support.
    """
    ...

@overload
def wake_on_ext1() -> None:
    """
    Configure how EXT1 wakes the device from sleep.  *pins* can be ``None``
    or a tuple/list of valid Pin objects.  *level* should be ``esp32.WAKEUP_ALL_LOW``
    or ``esp32.WAKEUP_ANY_HIGH``.

    ``Note:`` This is only available for boards that have ext1 support.
    """
    ...

@overload
def wake_on_ext1(pins: List[Pin] | Tuple[Pin, ...] | None, level: bool, /) -> None:
    """
    Configure how EXT1 wakes the device from sleep.  *pins* can be ``None``
    or a tuple/list of valid Pin objects.  *level* should be ``esp32.WAKEUP_ALL_LOW``
    or ``esp32.WAKEUP_ANY_HIGH``.

    ``Note:`` This is only available for boards that have ext1 support.
    """
    ...
