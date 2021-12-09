"""
functionality specific to the ESP32. See: https://docs.micropython.org/en/v1.15/library/esp32.html

The ``esp32`` module contains functions and classes specifically aimed at
controlling ESP32 modules.

"""

# + module: esp32.rst
# source version: v1.15
# origin module:: micropython/docs/library/esp32.rst
from typing import IO, Any, Callable, Coroutine, Dict, Generator, Iterator, List, NoReturn, Optional, Tuple, Union
from __future__ import annotations
#     Used in `idf_heap_info`.
HEAP_DATA : Any
#     Used in `idf_heap_info`.
HEAP_EXEC : Any
#    Selects the wake level for pins.
WAKEUP_ALL_LOW : Any
#    Selects the wake level for pins.
WAKEUP_ANY_HIGH : Any
class Partition():
    """
        Create an object representing a partition.  *id* can be a string which is the label
        of the partition to retrieve, or one of the constants: ``BOOT`` or ``RUNNING``.
    """
    #     Used in the `Partition` constructor to fetch various partitions: ``BOOT`` is the
    #     partition that will be booted at the next reset and ``RUNNING`` is the currently
    #     running partition.
    BOOT : Any
    #     Used in the `Partition` constructor to fetch various partitions: ``BOOT`` is the
    #     partition that will be booted at the next reset and ``RUNNING`` is the currently
    #     running partition.
    RUNNING : Any
    #     Used in `Partition.find` to specify the partition type: ``APP`` is for bootable
    #     firmware partitions (typically labelled ``factory``, ``ota_0``, ``ota_1``), and
    #     ``DATA`` is for other partitions, e.g. ``nvs``, ``otadata``, ``phy_init``, ``vfs``.
    TYPE_APP : Any
    #     Used in `Partition.find` to specify the partition type: ``APP`` is for bootable
    #     firmware partitions (typically labelled ``factory``, ``ota_0``, ``ota_1``), and
    #     ``DATA`` is for other partitions, e.g. ``nvs``, ``otadata``, ``phy_init``, ``vfs``.
    TYPE_DATA : Any
    def __init__(self, id) -> None:
        ...
    @classmethod
    def find(cls, type=TYPE_APP, subtype=0xff, label=None) -> List:
        """
            Find a partition specified by *type*, *subtype* and *label*.  Returns a
            (possibly empty) list of Partition objects. Note: ``subtype=0xff`` matches any subtype
            and ``label=None`` matches any label.
        """
        ...
    def info(self) -> Tuple:
        """
            Returns a 6-tuple ``(type, subtype, addr, size, label, encrypted)``.
        """
        ...
    def readblocks(self, block_num, buf, offset: Optional[int]) -> Any:
        ...
    def writeblocks(self, block_num, buf, offset: Optional[int]) -> Any:
        ...
    def ioctl(self, cmd, arg) -> Any:
        """
            These methods implement the simple and :ref:`extended
            <block-device-interface>` block protocol defined by
            :class:`uos.AbstractBlockDev`.
        """
        ...
    def set_boot(self) -> None:
        """
            Sets the partition as the boot partition.
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
    def mark_app_valid_cancel_rollback(cls, ) -> Any:
        """
            Signals that the current boot is considered successful.
            Calling ``mark_app_valid_cancel_rollback`` is required on the first boot of a new
            partition to avoid an automatic rollback at the next boot.
            This uses the ESP-IDF "app rollback" feature with "CONFIG_BOOTLOADER_APP_ROLLBACK_ENABLE"
            and  an ``OSError(-261)`` is raised if called on firmware that doesn't have the
            feature enabled.
            It is OK to call ``mark_app_valid_cancel_rollback`` on every boot and it is not
            necessary when booting firmare that was loaded using esptool.
        """
        ...
class RMT():
    """
        This class provides access to one of the eight RMT channels. *channel* is
        required and identifies which RMT channel (0-7) will be configured. *pin*,
        also required, configures which Pin is bound to the RMT channel. *clock_div*
        is an 8-bit clock divider that divides the source clock (80MHz) to the RMT
        channel allowing the resolution to be specified. *carrier_freq* is used to
        enable the carrier feature and specify its frequency, default value is ``0``
        (not enabled).  To enable, specify a positive integer.  *carrier_duty_percent*
        defaults to 50.
    """
    def __init__(self, channel, *, pin=None, clock_div=8, carrier_freq=0, carrier_duty_percent=50) -> None:
        ...
    def source_freq(self) -> Any:
        """
            Returns the source clock frequency. Currently the source clock is not
            configurable so this will always return 80MHz.
        """
        ...
    def clock_div(self) -> Any:
        """
            Return the clock divider. Note that the channel resolution is
            ``1 / (source_freq / clock_div)``.
        """
        ...
    def wait_done(self, timeout=0) -> bool:
        """
            Returns ``True`` if the channel is currently transmitting a stream of pulses
            started with a call to `RMT.write_pulses`.
        
            If *timeout* (defined in ticks of ``source_freq / clock_div``) is specified
            the method will wait for *timeout* or until transmission is complete,
            returning ``False`` if the channel continues to transmit. If looping is
            enabled with `RMT.loop` and a stream has started, then this method will
            always (wait and) return ``False``.
        """
        ...
    def loop(self, enable_loop) -> None:
        """
            Configure looping on the channel. *enable_loop* is bool, set to ``True`` to
            enable looping on the *next* call to `RMT.write_pulses`. If called with
            ``False`` while a looping stream is currently being transmitted then the
            current set of pulses will be completed before transmission stops.
        """
        ...
    def write_pulses(self, pulses, start) -> Any:
        """
            Begin sending *pulses*, a list or tuple defining the stream of pulses. The
            length of each pulse is defined by a number to be multiplied by the channel
            resolution ``(1 / (source_freq / clock_div))``. *start* defines whether the
            stream starts at 0 or 1.
        
            If transmission of a stream is currently in progress then this method will
            block until transmission of that stream has ended before beginning sending
            *pulses*.
        
            If looping is enabled with `RMT.loop`, the stream of pulses will be repeated
            indefinitely. Further calls to `RMT.write_pulses` will end the previous
            stream - blocking until the last set of pulses has been transmitted -
            before starting the next stream.
        
        """
        ...
class ULP():
    """
        This class provides access to the Ultra-Low-Power co-processor.
    """
    def __init__(self) -> None:
        ...
    def set_wakeup_period(self, period_index, period_us) -> None:
        """
            Set the wake-up period.
        """
        ...
    def load_binary(self, load_addr, program_binary) -> None:
        """
            Load a *program_binary* into the ULP at the given *load_addr*.
        """
        ...
    def run(self, entry_point) -> Any:
        """
            Start the ULP running at the given *entry_point*.
        
        """
        ...
class NVS():
    """
        Create an object providing access to a namespace (which is automatically created if not
        present).
    """
    def __init__(self, namespace) -> None:
        ...
    def set_i32(self, key, value) -> None:
        """
            Sets a 32-bit signed integer value for the specified key. Remember to call *commit*!
        """
        ...
    def get_i32(self, key) -> int:
        """
            Returns the signed integer value for the specified key. Raises an OSError if the key does not
            exist or has a different type.
        """
        ...
    def set_blob(self, key, value) -> None:
        """
            Sets a binary blob value for the specified key. The value passed in must support the buffer
            protocol, e.g. bytes, bytearray, str. (Note that esp-idf distinguishes blobs and strings, this
            method always writes a blob even if a string is passed in as value.)
            Remember to call *commit*!
        """
        ...
    def get_blob(self, key, buffer) -> int:
        """
            Reads the value of the blob for the specified key into the buffer, which must be a bytearray.
            Returns the actual length read. Raises an OSError if the key does not exist, has a different
            type, or if the buffer is too small.
        """
        ...
    def erase_key(self, key) -> Any:
        """
            Erases a key-value pair.
        """
        ...
    def commit(self) -> Any:
        """
            Commits changes made by *set_xxx* methods to flash.
        """
        ...
def wake_on_touch(wake) -> None:
    """
        Configure whether or not a touch will wake the device from sleep.
        *wake* should be a boolean value.
    """
    ...
def wake_on_ext0(pin, level) -> None:
    """
        Configure how EXT0 wakes the device from sleep.  *pin* can be ``None``
        or a valid Pin object.  *level* should be ``esp32.WAKEUP_ALL_LOW`` or
        ``esp32.WAKEUP_ANY_HIGH``.
    """
    ...
def wake_on_ext1(pins, level) -> None:
    """
        Configure how EXT1 wakes the device from sleep.  *pins* can be ``None``
        or a tuple/list of valid Pin objects.  *level* should be ``esp32.WAKEUP_ALL_LOW``
        or ``esp32.WAKEUP_ANY_HIGH``.
    """
    ...
def raw_temperature() -> int:
    """
        Read the raw value of the internal temperature sensor, returning an integer.
    """
    ...
def hall_sensor() -> int:
    """
        Read the raw value of the internal Hall sensor, returning an integer.
    """
    ...
def idf_heap_info(capabilities) -> List[Tuple]:
    """
        Returns information about the ESP-IDF heap memory regions. One of them contains
        the MicroPython heap and the others are used by ESP-IDF, e.g., for network
        buffers and other data. This data is useful to get a sense of how much memory
        is available to ESP-IDF and the networking stack in particular. It may shed
        some light on situations where ESP-IDF operations fail due to allocation failures.
        The information returned is *not* useful to troubleshoot Python allocation failures,
        use `micropython.mem_info()` instead.
    
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
    """
    ...
