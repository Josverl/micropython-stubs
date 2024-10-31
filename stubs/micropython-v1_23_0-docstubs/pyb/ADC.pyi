""" """

from __future__ import annotations
from _typeshed import Incomplete

class ADC:
    """
    Create an ADC object associated with the given pin.
    This allows you to then read analog values on that pin.
    """

    def __init__(self, pin) -> None: ...
    def read(self) -> Incomplete:
        """
        Read the value on the analog pin and return it.  The returned value
        will be between 0 and 4095.
        """
        ...

    def read_timed(self, buf, timer) -> Incomplete:
        """
        Read analog values into ``buf`` at a rate set by the ``timer`` object.

        ``buf`` can be bytearray or array.array for example.  The ADC values have
        12-bit resolution and are stored directly into ``buf`` if its element size is
        16 bits or greater.  If ``buf`` has only 8-bit elements (eg a bytearray) then
        the sample resolution will be reduced to 8 bits.

        ``timer`` should be a Timer object, and a sample is read each time the timer
        triggers.  The timer must already be initialised and running at the desired
        sampling frequency.

        To support previous behaviour of this function, ``timer`` can also be an
        integer which specifies the frequency (in Hz) to sample at.  In this case
        Timer(6) will be automatically configured to run at the given frequency.

        Example using a Timer object (preferred way)::

            adc = pyb.ADC(pyb.Pin.board.X19)    # create an ADC on pin X19
            tim = pyb.Timer(6, freq=10)         # create a timer running at 10Hz
            buf = bytearray(100)                # creat a buffer to store the samples
            adc.read_timed(buf, tim)            # sample 100 values, taking 10s

        Example using an integer for the frequency::

            adc = pyb.ADC(pyb.Pin.board.X19)    # create an ADC on pin X19
            buf = bytearray(100)                # create a buffer of 100 bytes
            adc.read_timed(buf, 10)             # read analog values into buf at 10Hz
                                                #   this will take 10 seconds to finish
            for val in buf:                     # loop over all values
                print(val)                      # print the value out

        This function does not allocate any heap memory. It has blocking behaviour:
        it does not return to the calling program until the buffer is full.
        """
        ...

    def read_timed_multi(self, adcs, bufs, timer) -> bool:
        """
        This is a static method. It can be used to extract relative timing or
        phase data from multiple ADC's.

        It reads analog values from multiple ADC's into buffers at a rate set by
        the *timer* object. Each time the timer triggers a sample is rapidly
        read from each ADC in turn.

        ADC and buffer instances are passed in tuples with each ADC having an
        associated buffer. All buffers must be of the same type and length and
        the number of buffers must equal the number of ADC's.

        Buffers can be ``bytearray`` or ``array.array`` for example. The ADC values
        have 12-bit resolution and are stored directly into the buffer if its element
        size is 16 bits or greater.  If buffers have only 8-bit elements (eg a
        ``bytearray``) then the sample resolution will be reduced to 8 bits.

        *timer* must be a Timer object. The timer must already be initialised
        and running at the desired sampling frequency.

        Example reading 3 ADC's::

            adc0 = pyb.ADC(pyb.Pin.board.X1)    # Create ADC's
            adc1 = pyb.ADC(pyb.Pin.board.X2)
            adc2 = pyb.ADC(pyb.Pin.board.X3)
            tim = pyb.Timer(8, freq=100)        # Create timer
            rx0 = array.array('H', (0 for i in range(100))) # ADC buffers of
            rx1 = array.array('H', (0 for i in range(100))) # 100 16-bit words
            rx2 = array.array('H', (0 for i in range(100)))
            # read analog values into buffers at 100Hz (takes one second)
            pyb.ADC.read_timed_multi((adc0, adc1, adc2), (rx0, rx1, rx2), tim)
            for n in range(len(rx0)):
                print(rx0[n], rx1[n], rx2[n])

        This function does not allocate any heap memory. It has blocking behaviour:
        it does not return to the calling program until the buffers are full.

        The function returns ``True`` if all samples were acquired with correct
        timing. At high sample rates the time taken to acquire a set of samples
        can exceed the timer period. In this case the function returns ``False``,
        indicating a loss of precision in the sample interval. In extreme cases
        samples may be missed.

        The maximum rate depends on factors including the data width and the
        number of ADC's being read. In testing two ADC's were sampled at a timer
        rate of 210kHz without overrun. Samples were missed at 215kHz.  For three
        ADC's the limit is around 140kHz, and for four it is around 110kHz.
        At high sample rates disabling interrupts for the duration can reduce the
        risk of sporadic data loss.
        """
        ...
