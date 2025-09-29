""" """

from __future__ import annotations

from typing import Any, Callable

from _mpy_shed import AnyReadableBuf, AnyWritableBuf
from _typeshed import Incomplete
from machine.Pin import Pin, PinLike
from typing_extensions import TypeAlias

ID_T: TypeAlias = int | str

class I2S:
    """
    I2S is a synchronous serial protocol used to connect digital audio devices.
    At the physical level, a bus consists of 3 lines: SCK, WS, SD.
    The I2S class supports controller operation.  Peripheral operation is not supported.

    The I2S class is currently available as a Technical Preview.  During the preview period, feedback from
    users is encouraged.  Based on this feedback, the I2S class API and implementation may be changed.

    I2S objects can be created and initialized using::

        from machine import I2S
        from machine import Pin

        # ESP32
        sck_pin = Pin(14)   # Serial clock output
        ws_pin = Pin(13)    # Word clock output
        sd_pin = Pin(12)    # Serial data output

        or

        # PyBoards
        sck_pin = Pin("Y6")   # Serial clock output
        ws_pin = Pin("Y5")    # Word clock output
        sd_pin = Pin("Y8")    # Serial data output

        audio_out = I2S(2,
                        sck=sck_pin, ws=ws_pin, sd=sd_pin,
                        mode=I2S.TX,
                        bits=16,
                        format=I2S.MONO,
                        rate=44100,
                        ibuf=20000)

        audio_in = I2S(2,
                       sck=sck_pin, ws=ws_pin, sd=sd_pin,
                       mode=I2S.RX,
                       bits=32,
                       format=I2S.STEREO,
                       rate=22050,
                       ibuf=20000)

    3 modes of operation are supported:
     - blocking
     - non-blocking
     - uasyncio

    blocking::

       num_written = audio_out.write(buf) # blocks until buf emptied

       num_read = audio_in.readinto(buf) # blocks until buf filled

    non-blocking::

       audio_out.irq(i2s_callback)         # i2s_callback is called when buf is emptied
       num_written = audio_out.write(buf)  # returns immediately

       audio_in.irq(i2s_callback)          # i2s_callback is called when buf is filled
       num_read = audio_in.readinto(buf)   # returns immediately

    uasyncio::

       swriter = uasyncio.StreamWriter(audio_out)
       swriter.write(buf)
       await swriter.drain()

       sreader = uasyncio.StreamReader(audio_in)
       num_read = await sreader.readinto(buf)
    """

    RX: Incomplete
    """for initialising the I2S bus ``mode`` to receive"""
    TX: Incomplete
    """for initialising the I2S bus ``mode`` to transmit"""
    STEREO: Incomplete
    """for initialising the I2S bus ``format`` to stereo"""
    MONO: Incomplete
    """for initialising the I2S bus ``format`` to mono"""
    def __init__(
        self,
        id: ID_T,
        /,
        *,
        sck: PinLike,
        ws: PinLike,
        sd: PinLike,
        mode: int,
        bits: int,
        format: int,
        rate: int,
        ibuf: int,
    ) -> None:
        """
        Construct an I2S object of the given id:

        - ``id`` identifies a particular I2S bus.

        ``id`` is board and port specific:

          - PYBv1.0/v1.1: has one I2S bus with id=2.
          - PYBD-SFxW: has two I2S buses with id=1 and id=2.
          - ESP32: has two I2S buses with id=0 and id=1.

        Keyword-only parameters that are supported on all ports:

          - ``sck`` is a pin object for the serial clock line
          - ``ws`` is a pin object for the word select line
          - ``sd`` is a pin object for the serial data line
          - ``mode`` specifies receive or transmit
          - ``bits`` specifies sample size (bits), 16 or 32
          - ``format`` specifies channel format, STEREO or MONO
          - ``rate`` specifies audio sampling rate (samples/s)
          - ``ibuf`` specifies internal buffer length (bytes)

        For all ports, DMA runs continuously in the background and allows user applications to perform other operations while
        sample data is transfered between the internal buffer and the I2S peripheral unit.
        Increasing the size of the internal buffer has the potential to increase the time that user applications can perform non-I2S operations
        before underflow (e.g. ``write`` method) or overflow (e.g. ``readinto`` method).
        """

    def init(
        self,
        *,
        sck: PinLike,
        ws: PinLike,
        sd: PinLike,
        mode: int,
        bits: int,
        format: int,
        rate: int,
        ibuf: int,
    ) -> None:
        """
        see Constructor for argument descriptions
        """
        ...

    def deinit(self) -> None:
        """
        Deinitialize the I2S bus
        """
        ...

    def readinto(
        self,
        buf: AnyWritableBuf,
        /,
    ) -> int:
        """
        Read audio samples into the buffer specified by ``buf``.  ``buf`` must support the buffer protocol, such as bytearray or array.
        "buf" byte ordering is little-endian.  For Stereo format, left channel sample precedes right channel sample. For Mono format,
        the left channel sample data is used.
        Returns number of bytes read
        """
        ...

    def write(
        self,
        buf: AnyReadableBuf,
        /,
    ) -> int:
        """
        Write audio samples contained in ``buf``. ``buf`` must support the buffer protocol, such as bytearray or array.
        "buf" byte ordering is little-endian.  For Stereo format, left channel sample precedes right channel sample. For Mono format,
        the sample data is written to both the right and left channels.
        Returns number of bytes written
        """
        ...

    def irq(
        self,
        handler: Callable[[Any], None],
        /,
    ) -> None:
        """
        Set a callback. ``handler`` is called when ``buf`` is emptied (``write`` method) or becomes full (``readinto`` method).
        Setting a callback changes the ``write`` and ``readinto`` methods to non-blocking operation.
        ``handler`` is called in the context of the MicroPython scheduler.
        """
        ...

    @staticmethod
    def shift(
        buf: AnyWritableBuf,
        bits: int,
        shift: int,
        /,
    ) -> None:
        """
        bitwise shift of all samples contained in ``buf``. ``bits`` specifies sample size in bits. ``shift`` specifies the number of bits to shift each sample.
        Positive for left shift, negative for right shift.
        Typically used for volume control.  Each bit shift changes sample volume by 6dB.
        """
        ...
