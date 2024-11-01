""" """

from __future__ import annotations
from _typeshed import Incomplete

class I2S:
    """
    Construct an I2S object of the given id:

    - ``id`` identifies a particular I2S bus; it is board and port specific

    Keyword-only parameters that are supported on all ports:

      - ``sck`` is a pin object for the serial clock line
      - ``ws`` is a pin object for the word select line
      - ``sd`` is a pin object for the serial data line
      - ``mck`` is a pin object for the master clock line;
        master clock frequency is sampling rate * 256
      - ``mode`` specifies receive or transmit
      - ``bits`` specifies sample size (bits), 16 or 32
      - ``format`` specifies channel format, STEREO or MONO
      - ``rate`` specifies audio sampling rate (Hz);
        this is the frequency of the ``ws`` signal
      - ``ibuf`` specifies internal buffer length (bytes)

    For all ports, DMA runs continuously in the background and allows user applications to perform other operations while
    sample data is transferred between the internal buffer and the I2S peripheral unit.
    Increasing the size of the internal buffer has the potential to increase the time that user applications can perform non-I2S operations
    before underflow (e.g. ``write`` method) or overflow (e.g. ``readinto`` method).
    """

    RX: Incomplete
    """for initialising the I2S bus ``mode`` to receive"""
    TX: Incomplete
    """for initialising the I2S bus ``mode`` to transmit"""
    STEREO: Incomplete
    """for initialising the I2S bus ``format`` to stereo"""
    MONO: Incomplete
    """for initialising the I2S bus ``format`` to mono"""
    def __init__(self, id, *, sck, ws, sd, mck=None, mode, bits, format, rate, ibuf) -> None: ...
    def init(self, sck, *args, **kwargs) -> Incomplete:
        """
        see Constructor for argument descriptions
        """
        ...

    def deinit(self) -> Incomplete:
        """
        Deinitialize the I2S bus
        """
        ...

    def readinto(self, buf) -> int:
        """
        Read audio samples into the buffer specified by ``buf``.  ``buf`` must support the buffer protocol, such as bytearray or array.
        "buf" byte ordering is little-endian.  For Stereo format, left channel sample precedes right channel sample. For Mono format,
        the left channel sample data is used.
        Returns number of bytes read
        """
        ...

    def write(self, buf) -> int:
        """
        Write audio samples contained in ``buf``. ``buf`` must support the buffer protocol, such as bytearray or array.
        "buf" byte ordering is little-endian.  For Stereo format, left channel sample precedes right channel sample. For Mono format,
        the sample data is written to both the right and left channels.
        Returns number of bytes written
        """
        ...

    def irq(self, handler) -> Incomplete:
        """
        Set a callback. ``handler`` is called when ``buf`` is emptied (``write`` method) or becomes full (``readinto`` method).
        Setting a callback changes the ``write`` and ``readinto`` methods to non-blocking operation.
        ``handler`` is called in the context of the MicroPython scheduler.
        """
        ...

    @staticmethod
    def shift(*, buf, bits, shift) -> Incomplete:
        """
        bitwise shift of all samples contained in ``buf``. ``bits`` specifies sample size in bits. ``shift`` specifies the number of bits to shift each sample.
        Positive for left shift, negative for right shift.
        Typically used for volume control.  Each bit shift changes sample volume by 6dB.
        """
        ...
