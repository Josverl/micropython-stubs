"""
Functions related to the hardware.

MicroPython module: https://docs.micropython.org/en/v1.24.0-preview/library/machine.html

The ``machine`` module contains specific functions related to the hardware
on a particular board. Most functions in this module allow to achieve direct
and unrestricted access to and control of hardware blocks on a system
(like CPU, timers, buses, etc.). Used incorrectly, this can lead to
malfunction, lockups, crashes of your board, and in extreme cases, hardware
damage.
"""

# source version: v1.24.0-preview
# origin module:: repos/micropython/docs/library/machine.rst
# + module: machine.Pin.rst
# + module: machine.Signal.rst
# + module: machine.ADC.rst
# + module: machine.ADCBlock.rst
# + module: machine.PWM.rst
# + module: machine.UART.rst
# + module: machine.SPI.rst
# + module: machine.I2C.rst
# + module: machine.I2S.rst
# + module: machine.RTC.rst
# + module: machine.Timer.rst
# + module: machine.WDT.rst
# + module: machine.SD.rst
# + module: machine.SDCard.rst
# + module: machine.USBDevice.rst
from __future__ import annotations
from typing import Any, Callable, List, NoReturn, Optional, Tuple, Union
from _typeshed import Incomplete

mem8: Incomplete
"""Read/write 8 bits of memory."""
mem16: Incomplete
"""Read/write 16 bits of memory."""
mem32: int
"""\
Read/write 32 bits of memory.

Use subscript notation ``[...]`` to index these objects with the address of
interest. Note that the address is the byte address, regardless of the size of
memory being accessed.

Example use (registers are specific to an stm32 microcontroller):
"""
IDLE: Incomplete
"""IRQ wake values."""
SLEEP: Incomplete
"""IRQ wake values."""
DEEPSLEEP: Incomplete
"""IRQ wake values."""
PWRON_RESET: Incomplete
"""Reset causes."""
HARD_RESET: Incomplete
"""Reset causes."""
WDT_RESET: Incomplete
"""Reset causes."""
DEEPSLEEP_RESET: Incomplete
"""Reset causes."""
SOFT_RESET: Incomplete
"""Reset causes."""
WLAN_WAKE: Incomplete
"""Wake-up reasons."""
PIN_WAKE: Incomplete
"""Wake-up reasons."""
RTC_WAKE: Incomplete
"""Wake-up reasons."""

class Pin:
    """
    Access the pin peripheral (GPIO pin) associated with the given ``id``.  If
    additional arguments are given in the constructor then they are used to initialise
    the pin.  Any settings that are not specified will remain in their previous state.

    The arguments are:

      - ``id`` is mandatory and can be an arbitrary object.  Among possible value
        types are: int (an internal Pin identifier), str (a Pin name), and tuple
        (pair of [port, pin]).

      - ``mode`` specifies the pin mode, which can be one of:

        - ``Pin.IN`` - Pin is configured for input.  If viewed as an output the pin
          is in high-impedance state.

        - ``Pin.OUT`` - Pin is configured for (normal) output.

        - ``Pin.OPEN_DRAIN`` - Pin is configured for open-drain output. Open-drain
          output works in the following way: if the output value is set to 0 the pin
          is active at a low level; if the output value is 1 the pin is in a high-impedance
          state.  Not all ports implement this mode, or some might only on certain pins.

        - ``Pin.ALT`` - Pin is configured to perform an alternative function, which is
          port specific.  For a pin configured in such a way any other Pin methods
          (except :meth:`Pin.init`) are not applicable (calling them will lead to undefined,
          or a hardware-specific, result).  Not all ports implement this mode.

        - ``Pin.ALT_OPEN_DRAIN`` - The Same as ``Pin.ALT``, but the pin is configured as
          open-drain.  Not all ports implement this mode.

        - ``Pin.ANALOG`` - Pin is configured for analog input, see the :class:`ADC` class.

      - ``pull`` specifies if the pin has a (weak) pull resistor attached, and can be
        one of:

        - ``None`` - No pull up or down resistor.
        - ``Pin.PULL_UP`` - Pull up resistor enabled.
        - ``Pin.PULL_DOWN`` - Pull down resistor enabled.

      - ``value`` is valid only for Pin.OUT and Pin.OPEN_DRAIN modes and specifies initial
        output pin value if given, otherwise the state of the pin peripheral remains
        unchanged.

      - ``drive`` specifies the output power of the pin and can be one of: ``Pin.DRIVE_0``,
        ``Pin.DRIVE_1``, etc., increasing in drive strength.  The actual current driving
        capabilities are port dependent.  Not all ports implement this argument.

      - ``alt`` specifies an alternate function for the pin and the values it can take are
        port dependent.  This argument is valid only for ``Pin.ALT`` and ``Pin.ALT_OPEN_DRAIN``
        modes.  It may be used when a pin supports more than one alternate function.  If only
        one pin alternate function is supported the this argument is not required.  Not all
        ports implement this argument.

    As specified above, the Pin class allows to set an alternate function for a particular
    pin, but it does not specify any further operations on such a pin.  Pins configured in
    alternate-function mode are usually not used as GPIO but are instead driven by other
    hardware peripherals.  The only operation supported on such a pin is re-initialising,
    by calling the constructor or :meth:`Pin.init` method.  If a pin that is configured in
    alternate-function mode is re-initialised with ``Pin.IN``, ``Pin.OUT``, or
    ``Pin.OPEN_DRAIN``, the alternate function will be removed from the pin.
    """

    IN: Incomplete
    """Selects the pin mode."""
    OUT: Incomplete
    """Selects the pin mode."""
    OPEN_DRAIN: Incomplete
    """Selects the pin mode."""
    ALT: Incomplete
    """Selects the pin mode."""
    ALT_OPEN_DRAIN: Incomplete
    """Selects the pin mode."""
    ANALOG: Incomplete
    """Selects the pin mode."""
    PULL_UP: Incomplete
    """\
    Selects whether there is a pull up/down resistor.  Use the value
    ``None`` for no pull.
    """
    PULL_DOWN: Incomplete
    """\
    Selects whether there is a pull up/down resistor.  Use the value
    ``None`` for no pull.
    """
    PULL_HOLD: Incomplete
    """\
    Selects whether there is a pull up/down resistor.  Use the value
    ``None`` for no pull.
    """
    DRIVE_0: int
    """\
    Selects the pin drive strength.  A port may define additional drive
    constants with increasing number corresponding to increasing drive
    strength.
    """
    DRIVE_1: int
    """\
    Selects the pin drive strength.  A port may define additional drive
    constants with increasing number corresponding to increasing drive
    strength.
    """
    DRIVE_2: int
    """\
    Selects the pin drive strength.  A port may define additional drive
    constants with increasing number corresponding to increasing drive
    strength.
    """
    IRQ_FALLING: Incomplete
    """Selects the IRQ trigger type."""
    IRQ_RISING: Incomplete
    """Selects the IRQ trigger type."""
    IRQ_LOW_LEVEL: Incomplete
    """Selects the IRQ trigger type."""
    IRQ_HIGH_LEVEL: Incomplete
    """Selects the IRQ trigger type."""
    def __init__(self, id, mode=-1, pull=-1, *, value=None, drive=0, alt=-1) -> None: ...
    def init(self, mode=-1, pull=-1, *, value=None, drive=0, alt=-1) -> None:
        """
        Re-initialise the pin using the given parameters.  Only those arguments that
        are specified will be set.  The rest of the pin peripheral state will remain
        unchanged.  See the constructor documentation for details of the arguments.

        Returns ``None``.
        """
        ...

    def value(self, x: Optional[Any] = None) -> int:
        """
        This method allows to set and get the value of the pin, depending on whether
        the argument ``x`` is supplied or not.

        If the argument is omitted then this method gets the digital logic level of
        the pin, returning 0 or 1 corresponding to low and high voltage signals
        respectively.  The behaviour of this method depends on the mode of the pin:

          - ``Pin.IN`` - The method returns the actual input value currently present
            on the pin.
          - ``Pin.OUT`` - The behaviour and return value of the method is undefined.
          - ``Pin.OPEN_DRAIN`` - If the pin is in state '0' then the behaviour and
            return value of the method is undefined.  Otherwise, if the pin is in
            state '1', the method returns the actual input value currently present
            on the pin.

        If the argument is supplied then this method sets the digital logic level of
        the pin.  The argument ``x`` can be anything that converts to a boolean.
        If it converts to ``True``, the pin is set to state '1', otherwise it is set
        to state '0'.  The behaviour of this method depends on the mode of the pin:

          - ``Pin.IN`` - The value is stored in the output buffer for the pin.  The
            pin state does not change, it remains in the high-impedance state.  The
            stored value will become active on the pin as soon as it is changed to
            ``Pin.OUT`` or ``Pin.OPEN_DRAIN`` mode.
          - ``Pin.OUT`` - The output buffer is set to the given value immediately.
          - ``Pin.OPEN_DRAIN`` - If the value is '0' the pin is set to a low voltage
            state.  Otherwise the pin is set to high-impedance state.

        When setting the value this method returns ``None``.
        """
        ...

    def __call__(self, x: Optional[Any] = None) -> Incomplete:
        """
        Pin objects are callable.  The call method provides a (fast) shortcut to set
        and get the value of the pin.  It is equivalent to Pin.value([x]).
        See :meth:`Pin.value` for more details.
        """
        ...

    def on(self) -> None:
        """
        Set pin to "1" output level.
        """
        ...

    def off(self) -> None:
        """
        Set pin to "0" output level.
        """
        ...

    def irq(self, handler=None, trigger=IRQ_FALLING, *, priority=1, wake=None, hard=False) -> Callable[..., Incomplete]:
        """
           Configure an interrupt handler to be called when the trigger source of the
           pin is active.  If the pin mode is ``Pin.IN`` then the trigger source is
           the external value on the pin.  If the pin mode is ``Pin.OUT`` then the
           trigger source is the output buffer of the pin.  Otherwise, if the pin mode
           is ``Pin.OPEN_DRAIN`` then the trigger source is the output buffer for
           state '0' and the external pin value for state '1'.

           The arguments are:

             - ``handler`` is an optional function to be called when the interrupt
               triggers. The handler must take exactly one argument which is the
               ``Pin`` instance.

             - ``trigger`` configures the event which can generate an interrupt.
               Possible values are:

               - ``Pin.IRQ_FALLING`` interrupt on falling edge.
               - ``Pin.IRQ_RISING`` interrupt on rising edge.
               - ``Pin.IRQ_LOW_LEVEL`` interrupt on low level.
               - ``Pin.IRQ_HIGH_LEVEL`` interrupt on high level.

               These values can be OR'ed together to trigger on multiple events.

             - ``priority`` sets the priority level of the interrupt.  The values it
               can take are port-specific, but higher values always represent higher
               priorities.

             - ``wake`` selects the power mode in which this interrupt can wake up the
               system.  It can be ``machine.IDLE``, ``machine.SLEEP`` or ``machine.DEEPSLEEP``.
               These values can also be OR'ed together to make a pin generate interrupts in
               more than one power mode.

             - ``hard`` if true a hardware interrupt is used. This reduces the delay
               between the pin change and the handler being called. Hard interrupt
               handlers may not allocate memory; see :ref:`isr_rules`.
               Not all ports support this argument.

           This method returns a callback object.

        The following methods are not part of the core Pin API and only implemented on certain ports.
        """
        ...

    def low(self) -> None:
        """
        Set pin to "0" output level.

        Availability: nrf, rp2, stm32 ports.
        """
        ...

    def high(self) -> None:
        """
        Set pin to "1" output level.

        Availability: nrf, rp2, stm32 ports.
        """
        ...

    def mode(self, mode: Optional[Any] = None) -> Incomplete:
        """
        Get or set the pin mode.
        See the constructor documentation for details of the ``mode`` argument.

        Availability: cc3200, stm32 ports.
        """
        ...

    def pull(self, pull: Optional[Any] = None) -> Incomplete:
        """
        Get or set the pin pull state.
        See the constructor documentation for details of the ``pull`` argument.

        Availability: cc3200, stm32 ports.
        """
        ...

    def drive(self, drive: Optional[Any] = None) -> Incomplete:
        """
        Get or set the pin drive strength.
        See the constructor documentation for details of the ``drive`` argument.

        Availability: cc3200 port.
        """
        ...

    def toggle(self) -> Incomplete:
        """
        Toggle output pin from "0" to "1" or vice-versa.

        Availability: mimxrt, samd, rp2 ports.
        """
        ...

class Signal(Pin):
    """
            Signal(pin_arguments..., *, invert=False)

    Create a Signal object. There're two ways to create it:

    * By wrapping existing Pin object - universal method which works for
      any board.
    * By passing required Pin parameters directly to Signal constructor,
      skipping the need to create intermediate Pin object. Available on
      many, but not all boards.

    The arguments are:

      - ``pin_obj`` is existing Pin object.

      - ``pin_arguments`` are the same arguments as can be passed to Pin constructor.

      - ``invert`` - if True, the signal will be inverted (active low).
    """

    def __init__(self, pin_obj, *args, invert=False) -> None: ...
    def value(self, x: Optional[Any] = None) -> int:
        """
        This method allows to set and get the value of the signal, depending on whether
        the argument ``x`` is supplied or not.

        If the argument is omitted then this method gets the signal level, 1 meaning
        signal is asserted (active) and 0 - signal inactive.

        If the argument is supplied then this method sets the signal level. The
        argument ``x`` can be anything that converts to a boolean. If it converts
        to ``True``, the signal is active, otherwise it is inactive.

        Correspondence between signal being active and actual logic level on the
        underlying pin depends on whether signal is inverted (active-low) or not.
        For non-inverted signal, active status corresponds to logical 1, inactive -
        to logical 0. For inverted/active-low signal, active status corresponds
        to logical 0, while inactive - to logical 1.
        """
        ...

    def on(self) -> None:
        """
        Activate signal.
        """
        ...

    def off(self) -> None:
        """
        Deactivate signal.
        """
        ...

class ADC:
    """
    Access the ADC associated with a source identified by *id*.  This
    *id* may be an integer (usually specifying a channel number), a
    :ref:`Pin <machine.Pin>` object, or other value supported by the
    underlying machine.

    If additional keyword-arguments are given then they will configure
    various aspects of the ADC.  If not given, these settings will take
    previous or default values.  The settings are:

      - *sample_ns* is the sampling time in nanoseconds.

      - *atten* specifies the input attenuation.
    """

    def __init__(self, id, *, sample_ns: Optional[int] = 0, atten: Optional[int] = ATTN_0DB) -> None: ...
    def init(self, *, sample_ns, atten) -> Incomplete:
        """
        Apply the given settings to the ADC.  Only those arguments that are
        specified will be changed.  See the ADC constructor above for what the
        arguments are.
        """
        ...

    def block(self) -> Incomplete:
        """
        Return the :ref:`ADCBlock <machine.ADCBlock>` instance associated with
        this ADC object.

        This method only exists if the port supports the
        :ref:`ADCBlock <machine.ADCBlock>` class.
        """
        ...

    def read_u16(self) -> int:
        """
        Take an analog reading and return an integer in the range 0-65535.
        The return value represents the raw reading taken by the ADC, scaled
        such that the minimum value is 0 and the maximum value is 65535.
        """
        ...

    def read_uv(self) -> int:
        """
        Take an analog reading and return an integer value with units of
        microvolts.  It is up to the particular port whether or not this value
        is calibrated, and how calibration is done.
        """
        ...

class ADCBlock:
    """
    Access the ADC peripheral identified by *id*, which may be an integer
    or string.

    The *bits* argument, if given, sets the resolution in bits of the
    conversion process.  If not specified then the previous or default
    resolution is used.
    """

    def __init__(self, id, *, bits) -> None: ...
    def init(self, *, bits) -> None:
        """
        Configure the ADC peripheral.  *bits* will set the resolution of the
        conversion process.
        """
        ...

    def connect(self, channel, source, *args, **kwargs) -> Incomplete:
        """
        Connect up a channel on the ADC peripheral so it is ready for sampling,
        and return an :ref:`ADC <machine.ADC>` object that represents that connection.

        The *channel* argument must be an integer, and *source* must be an object
        (for example a :ref:`Pin <machine.Pin>`) which can be connected up for sampling.

        If only *channel* is given then it is configured for sampling.

        If only *source* is given then that object is connected to a default
        channel ready for sampling.

        If both *channel* and *source* are given then they are connected together
        and made ready for sampling.

        Any additional keyword arguments are used to configure the returned ADC object,
        via its :meth:`init <machine.ADC.init>` method.
        """
        ...

class PWM:
    """
    Construct and return a new PWM object using the following parameters:

       - *dest* is the entity on which the PWM is output, which is usually a
         :ref:`machine.Pin <machine.Pin>` object, but a port may allow other values,
         like integers.
       - *freq* should be an integer which sets the frequency in Hz for the
         PWM cycle.
       - *duty_u16* sets the duty cycle as a ratio ``duty_u16 / 65535``.
       - *duty_ns* sets the pulse width in nanoseconds.
       - *invert*  inverts the respective output if the value is True

    Setting *freq* may affect other PWM objects if the objects share the same
    underlying PWM generator (this is hardware specific).
    Only one of *duty_u16* and *duty_ns* should be specified at a time.
    *invert* is not available at all ports.
    """

    def __init__(self, dest, *, freq=0, duty=0, duty_u16=0, duty_ns=0, invert=False) -> None: ...
    def init(self, *, freq, duty_u16, duty_ns) -> None:
        """
        Modify settings for the PWM object.  See the above constructor for details
        about the parameters.
        """
        ...

    def deinit(self) -> None:
        """
        Disable the PWM output.
        """
        ...

    def freq(self, value: Optional[Any] = None) -> Incomplete:
        """
        Get or set the current frequency of the PWM output.

        With no arguments the frequency in Hz is returned.

        With a single *value* argument the frequency is set to that value in Hz.  The
        method may raise a ``ValueError`` if the frequency is outside the valid range.
        """
        ...

    def duty_u16(self, value: Optional[Any] = None) -> int:
        """
        Get or set the current duty cycle of the PWM output, as an unsigned 16-bit
        value in the range 0 to 65535 inclusive.

        With no arguments the duty cycle is returned.

        With a single *value* argument the duty cycle is set to that value, measured
        as the ratio ``value / 65535``.
        """
        ...

    def duty_ns(self, value: Optional[Any] = None) -> int:
        """
        Get or set the current pulse width of the PWM output, as a value in nanoseconds.

        With no arguments the pulse width in nanoseconds is returned.

        With a single *value* argument the pulse width is set to that value.
        """
        ...

class UART:
    """
    Construct a UART object of the given id.
    """

    RTS: Incomplete
    """\
    Flow control options.
    
    Availability: esp32, mimxrt, renesas-ra, rp2, stm32.
    """
    CTS: Incomplete
    """\
    Flow control options.
    
    Availability: esp32, mimxrt, renesas-ra, rp2, stm32.
    """
    IRQ_RXIDLE: Incomplete
    """\
    IRQ trigger sources.
    
    Availability: renesas-ra, stm32, esp32, rp2040, mimxrt, samd, cc3200.
    """
    IRQ_RX: Incomplete
    """\
    IRQ trigger sources.
    
    Availability: renesas-ra, stm32, esp32, rp2040, mimxrt, samd, cc3200.
    """
    IRQ_TXIDLE: Incomplete
    """\
    IRQ trigger sources.
    
    Availability: renesas-ra, stm32, esp32, rp2040, mimxrt, samd, cc3200.
    """
    IRQ_BREAK: Incomplete
    """\
    IRQ trigger sources.
    
    Availability: renesas-ra, stm32, esp32, rp2040, mimxrt, samd, cc3200.
    """
    def __init__(self, id, *args, **kwargs) -> None: ...
    def init(self, baudrate=9600, bits=8, parity=None, stop=1, *args, **kwargs) -> None:
        """
        Initialise the UART bus with the given parameters:

          - *baudrate* is the clock rate.
          - *bits* is the number of bits per character, 7, 8 or 9.
          - *parity* is the parity, ``None``, 0 (even) or 1 (odd).
          - *stop* is the number of stop bits, 1 or 2.

        Additional keyword-only parameters that may be supported by a port are:

          - *tx* specifies the TX pin to use.
          - *rx* specifies the RX pin to use.
          - *rts* specifies the RTS (output) pin to use for hardware receive flow control.
          - *cts* specifies the CTS (input) pin to use for hardware transmit flow control.
          - *txbuf* specifies the length in characters of the TX buffer.
          - *rxbuf* specifies the length in characters of the RX buffer.
          - *timeout* specifies the time to wait for the first character (in ms).
          - *timeout_char* specifies the time to wait between characters (in ms).
          - *invert* specifies which lines to invert.

              - ``0`` will not invert lines (idle state of both lines is logic high).
              - ``UART.INV_TX`` will invert TX line (idle state of TX line now logic low).
              - ``UART.INV_RX`` will invert RX line (idle state of RX line now logic low).
              - ``UART.INV_TX | UART.INV_RX`` will invert both lines (idle state at logic low).

          - *flow* specifies which hardware flow control signals to use. The value
            is a bitmask.

              - ``0`` will ignore hardware flow control signals.
              - ``UART.RTS`` will enable receive flow control by using the RTS output pin to
                signal if the receive FIFO has sufficient space to accept more data.
              - ``UART.CTS`` will enable transmit flow control by pausing transmission when the
                CTS input pin signals that the receiver is running low on buffer space.
              - ``UART.RTS | UART.CTS`` will enable both, for full hardware flow control.

        On the WiPy only the following keyword-only parameter is supported:

          - *pins* is a 4 or 2 item list indicating the TX, RX, RTS and CTS pins (in that order).
            Any of the pins can be None if one wants the UART to operate with limited functionality.
            If the RTS pin is given the the RX pin must be given as well. The same applies to CTS.
            When no pins are given, then the default set of TX and RX pins is taken, and hardware
            flow control will be disabled. If *pins* is ``None``, no pin assignment will be made.

        .. note::
          It is possible to call ``init()`` multiple times on the same object in
          order to reconfigure  UART on the fly. That allows using single UART
          peripheral to serve different devices attached to different GPIO pins.
          Only one device can be served at a time in that case.
          Also do not call ``deinit()`` as it will prevent calling ``init()``
          again.
        """
        ...

    def deinit(self) -> None:
        """
        Turn off the UART bus.

        .. note::
          You will not be able to call ``init()`` on the object after ``deinit()``.
          A new instance needs to be created in that case.
        """
        ...

    def any(self) -> int:
        """
        Returns an integer counting the number of characters that can be read without
        blocking.  It will return 0 if there are no characters available and a positive
        number if there are characters.  The method may return 1 even if there is more
        than one character available for reading.

        For more sophisticated querying of available characters use select.poll::

         poll = select.poll()
         poll.register(uart, select.POLLIN)
         poll.poll(timeout)
        """
        ...

    def read(self, nbytes: Optional[Any] = None) -> bytes:
        """
        Read characters.  If ``nbytes`` is specified then read at most that many bytes,
        otherwise read as much data as possible. It may return sooner if a timeout
        is reached. The timeout is configurable in the constructor.

        Return value: a bytes object containing the bytes read in.  Returns ``None``
        on timeout.
        """
        ...

    def readinto(self, buf, nbytes: Optional[Any] = None) -> Union[int, None]:
        """
        Read bytes into the ``buf``.  If ``nbytes`` is specified then read at most
        that many bytes.  Otherwise, read at most ``len(buf)`` bytes. It may return sooner if a timeout
        is reached. The timeout is configurable in the constructor.

        Return value: number of bytes read and stored into ``buf`` or ``None`` on
        timeout.
        """
        ...

    def readline(self) -> Union[str, None]:
        """
        Read a line, ending in a newline character. It may return sooner if a timeout
        is reached. The timeout is configurable in the constructor.

        Return value: the line read or ``None`` on timeout.
        """
        ...

    def write(self, buf) -> Union[int, None]:
        """
        Write the buffer of bytes to the bus.

        Return value: number of bytes written or ``None`` on timeout.
        """
        ...

    def sendbreak(self) -> None:
        """
        Send a break condition on the bus. This drives the bus low for a duration
        longer than required for a normal transmission of a character.
        """
        ...

    def flush(self) -> Incomplete:
        """
        Waits until all data has been sent. In case of a timeout, an exception is raised. The timeout
        duration depends on the tx buffer size and the baud rate. Unless flow control is enabled, a timeout
        should not occur.

        .. note::

            For the esp8266 and nrf ports the call returns while the last byte is sent.
            If required, a one character wait time has to be added in the calling script.

        Availability: rp2, esp32, esp8266, mimxrt, cc3200, stm32, nrf ports, renesas-ra
        """
        ...

    def txdone(self) -> bool:
        """
        Tells whether all data has been sent or no data transfer is happening. In this case,
        it returns ``True``. If a data transmission is ongoing it returns ``False``.

        .. note::

            For the esp8266 and nrf ports the call may return ``True`` even if the last byte
            of a transfer is still being sent. If required, a one character wait time has to be
            added in the calling script.

        Availability: rp2, esp32, esp8266, mimxrt, cc3200, stm32, nrf ports, renesas-ra
        """
        ...

    def irq(self, handler=None, trigger=0, hard=False) -> Incomplete:
        """
        Configure an interrupt handler to be called when a UART event occurs.

        The arguments are:

          - *handler* is an optional function to be called when the interrupt event
            triggers.  The handler must take exactly one argument which is the
            ``UART`` instance.

          - *trigger* configures the event(s) which can generate an interrupt.
            Possible values are a mask of one or more of the following:

            - ``UART.IRQ_RXIDLE`` interrupt after receiving at least one character
              and then the RX line goes idle.
            - ``UART.IRQ_RX`` interrupt after each received character.
            - ``UART.IRQ_TXIDLE`` interrupt after or while the last character(s) of
              a message are or have been sent.
            - ``UART.IRQ_BREAK`` interrupt when a break state is detected at RX

          - *hard* if true a hardware interrupt is used.  This reduces the delay
            between the pin change and the handler being called. Hard interrupt
            handlers may not allocate memory; see :ref:`isr_rules`.

        Returns an irq object.

        Due to limitations of the hardware not all trigger events are available on all ports.
        """
        ...

class SPI:
    """
    Construct an SPI object on the given bus, *id*. Values of *id* depend
    on a particular port and its hardware. Values 0, 1, etc. are commonly used
    to select hardware SPI block #0, #1, etc.

    With no additional parameters, the SPI object is created but not
    initialised (it has the settings from the last initialisation of
    the bus, if any).  If extra arguments are given, the bus is initialised.
    See ``init`` for parameters of initialisation.
    """

    CONTROLLER: Incomplete
    """for initialising the SPI bus to controller; this is only used for the WiPy"""
    MSB: Incomplete
    """set the first bit to be the most significant bit"""
    LSB: Incomplete
    """set the first bit to be the least significant bit"""
    def __init__(self, id, *args, **kwargs) -> None: ...
    def init(
        self, baudrate=1000000, *, polarity=0, phase=0, bits=8, firstbit=MSB, sck=None, mosi=None, miso=None, pins: Optional[Tuple]
    ) -> None:
        """
        Initialise the SPI bus with the given parameters:

          - ``baudrate`` is the SCK clock rate.
          - ``polarity`` can be 0 or 1, and is the level the idle clock line sits at.
          - ``phase`` can be 0 or 1 to sample data on the first or second clock edge
            respectively.
          - ``bits`` is the width in bits of each transfer. Only 8 is guaranteed to be supported by all hardware.
          - ``firstbit`` can be ``SPI.MSB`` or ``SPI.LSB``.
          - ``sck``, ``mosi``, ``miso`` are pins (machine.Pin) objects to use for bus signals. For most
            hardware SPI blocks (as selected by ``id`` parameter to the constructor), pins are fixed
            and cannot be changed. In some cases, hardware blocks allow 2-3 alternative pin sets for
            a hardware SPI block. Arbitrary pin assignments are possible only for a bitbanging SPI driver
            (``id`` = -1).
          - ``pins`` - WiPy port doesn't ``sck``, ``mosi``, ``miso`` arguments, and instead allows to
            specify them as a tuple of ``pins`` parameter.

        In the case of hardware SPI the actual clock frequency may be lower than the
        requested baudrate. This is dependent on the platform hardware. The actual
        rate may be determined by printing the SPI object.
        """
        ...

    def deinit(self) -> None:
        """
        Turn off the SPI bus.
        """
        ...

    def read(self, nbytes, write=0x00) -> bytes:
        """
        Read a number of bytes specified by ``nbytes`` while continuously writing
        the single byte given by ``write``.
        Returns a ``bytes`` object with the data that was read.
        """
        ...

    def readinto(self, buf, write=0x00) -> int:
        """
        Read into the buffer specified by ``buf`` while continuously writing the
        single byte given by ``write``.
        Returns ``None``.

        Note: on WiPy this function returns the number of bytes read.
        """
        ...

    def write(self, buf) -> int:
        """
        Write the bytes contained in ``buf``.
        Returns ``None``.

        Note: on WiPy this function returns the number of bytes written.
        """
        ...

    def write_readinto(self, write_buf, read_buf) -> int:
        """
        Write the bytes from ``write_buf`` while reading into ``read_buf``.  The
        buffers can be the same or different, but both buffers must have the
        same length.
        Returns ``None``.

        Note: on WiPy this function returns the number of bytes written.
        """
        ...

class SoftSPI(SPI):
    """
    Construct a new software SPI object.  Additional parameters must be
    given, usually at least *sck*, *mosi* and *miso*, and these are used
    to initialise the bus.  See `SPI.init` for a description of the parameters.
    """

    MSB: Incomplete
    """set the first bit to be the most significant bit"""
    LSB: Incomplete
    """set the first bit to be the least significant bit"""
    def __init__(self, baudrate=500000, *, polarity=0, phase=0, bits=8, firstbit=MSB, sck=None, mosi=None, miso=None) -> None: ...

class I2C:
    """
    Construct and return a new I2C object using the following parameters:

       - *id* identifies a particular I2C peripheral.  Allowed values for
         depend on the particular port/board
       - *scl* should be a pin object specifying the pin to use for SCL.
       - *sda* should be a pin object specifying the pin to use for SDA.
       - *freq* should be an integer which sets the maximum frequency
         for SCL.
       - *timeout* is the maximum time in microseconds to allow for I2C
         transactions.  This parameter is not allowed on some ports.

    Note that some ports/boards will have default values of *scl* and *sda*
    that can be changed in this constructor.  Others will have fixed values
    of *scl* and *sda* that cannot be changed.
    """

    def __init__(
        self,
        id: Union[int, str] = -1,
        *,
        scl: Optional[Union[Pin, str]] = None,
        sda: Optional[Union[Pin, str]] = None,
        freq=400_000,
        timeout=50000,
    ) -> None: ...
    def init(self, scl, sda, *, freq=400000) -> None:
        """
        Initialise the I2C bus with the given arguments:

           - *scl* is a pin object for the SCL line
           - *sda* is a pin object for the SDA line
           - *freq* is the SCL clock rate

         In the case of hardware I2C the actual clock frequency may be lower than the
         requested frequency. This is dependent on the platform hardware. The actual
         rate may be determined by printing the I2C object.
        """
        ...

    def deinit(self) -> None:
        """
        Turn off the I2C bus.

        Availability: WiPy.
        """
        ...

    def scan(self) -> List:
        """
        Scan all I2C addresses between 0x08 and 0x77 inclusive and return a list of
        those that respond.  A device responds if it pulls the SDA line low after
        its address (including a write bit) is sent on the bus.
        """
        ...

    def start(self) -> None:
        """
        Generate a START condition on the bus (SDA transitions to low while SCL is high).
        """
        ...

    def stop(self) -> None:
        """
        Generate a STOP condition on the bus (SDA transitions to high while SCL is high).
        """
        ...

    def readinto(
        self,
        buf,
        nack=True,
    ) -> Incomplete:
        """
        Reads bytes from the bus and stores them into *buf*.  The number of bytes
        read is the length of *buf*.  An ACK will be sent on the bus after
        receiving all but the last byte.  After the last byte is received, if *nack*
        is true then a NACK will be sent, otherwise an ACK will be sent (and in this
        case the peripheral assumes more bytes are going to be read in a later call).
        """
        ...

    def write(self, buf) -> int:
        """
        Write the bytes from *buf* to the bus.  Checks that an ACK is received
        after each byte and stops transmitting the remaining bytes if a NACK is
        received.  The function returns the number of ACKs that were received.
        """
        ...

    def readfrom(
        self,
        addr,
        nbytes,
        stop=True,
    ) -> bytes:
        """
        Read *nbytes* from the peripheral specified by *addr*.
        If *stop* is true then a STOP condition is generated at the end of the transfer.
        Returns a `bytes` object with the data read.
        """
        ...

    def readfrom_into(
        self,
        addr,
        buf,
        stop=True,
    ) -> None:
        """
        Read into *buf* from the peripheral specified by *addr*.
        The number of bytes read will be the length of *buf*.
        If *stop* is true then a STOP condition is generated at the end of the transfer.

        The method returns ``None``.
        """
        ...

    def writeto(
        self,
        addr,
        buf,
        stop=True,
    ) -> int:
        """
        Write the bytes from *buf* to the peripheral specified by *addr*.  If a
        NACK is received following the write of a byte from *buf* then the
        remaining bytes are not sent.  If *stop* is true then a STOP condition is
        generated at the end of the transfer, even if a NACK is received.
        The function returns the number of ACKs that were received.
        """
        ...

    def writevto(
        self,
        addr,
        vector,
        stop=True,
    ) -> int:
        """
        Write the bytes contained in *vector* to the peripheral specified by *addr*.
        *vector* should be a tuple or list of objects with the buffer protocol.
        The *addr* is sent once and then the bytes from each object in *vector*
        are written out sequentially.  The objects in *vector* may be zero bytes
        in length in which case they don't contribute to the output.

        If a NACK is received following the write of a byte from one of the
        objects in *vector* then the remaining bytes, and any remaining objects,
        are not sent.  If *stop* is true then a STOP condition is generated at
        the end of the transfer, even if a NACK is received.  The function
        returns the number of ACKs that were received.
        """
        ...

    def readfrom_mem(self, addr, memaddr, nbytes, *, addrsize=8) -> bytes:
        """
        Read *nbytes* from the peripheral specified by *addr* starting from the memory
        address specified by *memaddr*.
        The argument *addrsize* specifies the address size in bits.
        Returns a `bytes` object with the data read.
        """
        ...

    def readfrom_mem_into(self, addr, memaddr, buf, *, addrsize=8) -> None:
        """
        Read into *buf* from the peripheral specified by *addr* starting from the
        memory address specified by *memaddr*.  The number of bytes read is the
        length of *buf*.
        The argument *addrsize* specifies the address size in bits (on ESP8266
        this argument is not recognised and the address size is always 8 bits).

        The method returns ``None``.
        """
        ...

    def writeto_mem(self, addr, memaddr, buf, *, addrsize=8) -> None:
        """
        Write *buf* to the peripheral specified by *addr* starting from the
        memory address specified by *memaddr*.
        The argument *addrsize* specifies the address size in bits (on ESP8266
        this argument is not recognised and the address size is always 8 bits).

        The method returns ``None``.
        """
        ...

class SoftI2C(I2C):
    """
    Construct a new software I2C object.  The parameters are:

       - *scl* should be a pin object specifying the pin to use for SCL.
       - *sda* should be a pin object specifying the pin to use for SDA.
       - *freq* should be an integer which sets the maximum frequency
         for SCL.
       - *timeout* is the maximum time in microseconds to wait for clock
         stretching (SCL held low by another device on the bus), after
         which an ``OSError(ETIMEDOUT)`` exception is raised.
    """

    def __init__(self, scl, sda, *, freq=400000, timeout=50000) -> None: ...

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

class RTC:
    """
    Create an RTC object. See init for parameters of initialization.
    """

    ALARM0: Incomplete
    """irq trigger source"""
    def __init__(self, id=0, *args, **kwargs) -> None: ...
    def datetime(self, datetimetuple: Optional[Any] = None) -> Tuple:
        """
        Get or set the date and time of the RTC.

        With no arguments, this method returns an 8-tuple with the current
        date and time.  With 1 argument (being an 8-tuple) it sets the date
        and time.

        The 8-tuple has the following format:

            (year, month, day, weekday, hours, minutes, seconds, subseconds)

        The meaning of the ``subseconds`` field is hardware dependent.
        """
        ...

    def init(self, datetime) -> None:
        """
        Initialise the RTC. Datetime is a tuple of the form:

           ``(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])``
        """
        ...

    def now(self) -> Tuple:
        """
        Get get the current datetime tuple.
        """
        ...

    def deinit(self) -> None:
        """
        Resets the RTC to the time of January 1, 2015 and starts running it again.
        """
        ...

    def alarm(self, id, time, *, repeat=False) -> None:
        """
        Set the RTC alarm. Time might be either a millisecond value to program the alarm to
        current time + time_in_ms in the future, or a datetimetuple. If the time passed is in
        milliseconds, repeat can be set to ``True`` to make the alarm periodic.
        """
        ...

    def alarm_left(self, alarm_id=0) -> int:
        """
        Get the number of milliseconds left before the alarm expires.
        """
        ...

    def cancel(self, alarm_id=0) -> None:
        """
        Cancel a running alarm.
        """
        ...

    def irq(self, *, trigger, handler=None, wake=IDLE) -> Incomplete:
        """
        Create an irq object triggered by a real time clock alarm.

           - ``trigger`` must be ``RTC.ALARM0``
           - ``handler`` is the function to be called when the callback is triggered.
           - ``wake`` specifies the sleep mode from where this interrupt can wake
             up the system.
        """
        ...

    def memory(self, data: Optional[Any] = None) -> bytes:
        """
        ``RTC.memory(data)`` will write *data* to the RTC memory, where *data* is any
        object which supports the buffer protocol (including `bytes`, `bytearray`,
        `memoryview` and `array.array`). ``RTC.memory()`` reads RTC memory and returns
        a `bytes` object.

        Data written to RTC user memory is persistent across restarts, including
        `machine.soft_reset()` and `machine.deepsleep()`.

        The maximum length of RTC user memory is 2048 bytes by default on esp32,
        and 492 bytes on esp8266.

        Availability: esp32, esp8266 ports.
        """
        ...

class Timer:
    """
    Construct a new timer object of the given ``id``. ``id`` of -1 constructs a
    virtual timer (if supported by a board).
    ``id`` shall not be passed as a keyword argument.

    See ``init`` for parameters of initialisation.
    """

    ONE_SHOT: Incomplete
    """Timer operating mode."""
    PERIODIC: Incomplete
    """Timer operating mode."""
    def __init__(self, id=-1, *args, **kwargs) -> None: ...
    def init(self, *, mode=PERIODIC, freq=-1, period=-1, callback=None) -> None:
        """
        Initialise the timer. Example::

            def mycallback(t):
                pass

            # periodic at 1kHz
            tim.init(mode=Timer.PERIODIC, freq=1000, callback=mycallback)

            # periodic with 100ms period
            tim.init(period=100, callback=mycallback)

            # one shot firing after 1000ms
            tim.init(mode=Timer.ONE_SHOT, period=1000, callback=mycallback)

        Keyword arguments:

          - ``mode`` can be one of:

            - ``Timer.ONE_SHOT`` - The timer runs once until the configured
              period of the channel expires.
            - ``Timer.PERIODIC`` - The timer runs periodically at the configured
              frequency of the channel.

          - ``freq`` - The timer frequency, in units of Hz.  The upper bound of
            the frequency is dependent on the port.  When both the ``freq`` and
            ``period`` arguments are given, ``freq`` has a higher priority and
            ``period`` is ignored.

          - ``period`` - The timer period, in milliseconds.

          - ``callback`` - The callable to call upon expiration of the timer period.
            The callback must take one argument, which is passed the Timer object.
            The ``callback`` argument shall be specified. Otherwise an exception
            will occur upon timer expiration:
            ``TypeError: 'NoneType' object isn't callable``
        """
        ...

    def deinit(self) -> None:
        """
        Deinitialises the timer. Stops the timer, and disables the timer peripheral.
        """
        ...

class WDT:
    """
    Create a WDT object and start it. The timeout must be given in milliseconds.
    Once it is running the timeout cannot be changed and the WDT cannot be stopped either.

    Notes: On the esp8266 a timeout cannot be specified, it is determined by the underlying system.
    On rp2040 devices, the maximum timeout is 8388 ms.
    """

    def __init__(self, id=0, timeout=5000) -> None: ...
    def feed(self) -> None:
        """
        Feed the WDT to prevent it from resetting the system. The application
        should place this call in a sensible place ensuring that the WDT is
        only fed after verifying that everything is functioning correctly.
        """
        ...

class SD:
    """
    Create a SD card object. See ``init()`` for parameters if initialization.
    """

    def __init__(self, id, *args, **kwargs) -> None: ...
    def init(self, id=0, pins=("GP10", "GP11", "GP15")) -> None:
        """
        Enable the SD card. In order to initialize the card, give it a 3-tuple:
        ``(clk_pin, cmd_pin, dat0_pin)``.
        """
        ...

    def deinit(self) -> None:
        """
        Disable the SD card.
        """
        ...

class SDCard:
    """
    This class provides access to SD or MMC storage cards using either
    a dedicated SD/MMC interface hardware or through an SPI channel.
    The class implements the block protocol defined by :class:`vfs.AbstractBlockDev`.
    This allows the mounting of an SD card to be as simple as::

      vfs.mount(machine.SDCard(), "/sd")

    The constructor takes the following parameters:

     - *slot* selects which of the available interfaces to use. Leaving this
       unset will select the default interface.

     - *width* selects the bus width for the SD/MMC interface.

     - *cd* can be used to specify a card-detect pin.

     - *wp* can be used to specify a write-protect pin.

     - *sck* can be used to specify an SPI clock pin.

     - *miso* can be used to specify an SPI miso pin.

     - *mosi* can be used to specify an SPI mosi pin.

     - *cs* can be used to specify an SPI chip select pin.

     - *freq* selects the SD/MMC interface frequency in Hz (only supported on the ESP32).
    """

    def __init__(self, slot=1, width=1, cd=None, wp=None, sck=None, miso=None, mosi=None, cs=None, freq=20000000) -> None: ...

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

    def remote_wakeup(self) -> bool:
        """
        Wake up host if we are in suspend mode and the REMOTE_WAKEUP feature
        is enabled by the host. This has to be enabled in the USB attributes,
        and on the host. Returns ``True`` if remote wakeup was enabled and
        active and the host was woken up.
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

def reset() -> NoReturn:
    """
    Resets the device in a manner similar to pushing the external RESET
    button.
    """
    ...

def soft_reset() -> NoReturn:
    """
    Performs a soft reset of the interpreter, deleting all Python objects and
    resetting the Python heap.  It tries to retain the method by which the user
    is connected to the MicroPython REPL (eg serial, USB, Wifi).
    """
    ...

def reset_cause() -> int:
    """
    Get the reset cause. See :ref:`constants <machine_constants>` for the possible return values.
    """
    ...

def bootloader(value: Optional[Any] = None) -> None:
    """
    Reset the device and enter its bootloader.  This is typically used to put the
    device into a state where it can be programmed with new firmware.

    Some ports support passing in an optional *value* argument which can control
    which bootloader to enter, what to pass to it, or other things.
    """
    ...

def disable_irq() -> Incomplete:
    """
    Disable interrupt requests.
    Returns the previous IRQ state which should be considered an opaque value.
    This return value should be passed to the `enable_irq()` function to restore
    interrupts to their original state, before `disable_irq()` was called.
    """
    ...

def enable_irq(state) -> Incomplete:
    """
    Re-enable interrupt requests.
    The *state* parameter should be the value that was returned from the most
    recent call to the `disable_irq()` function.
    """
    ...

def freq(hz: Optional[Any] = None) -> Incomplete:
    """
    Returns the CPU frequency in hertz.

    On some ports this can also be used to set the CPU frequency by passing in *hz*.
    """
    ...

def idle() -> Incomplete:
    """
    Gates the clock to the CPU, useful to reduce power consumption at any time
    during short or long periods. Peripherals continue working and execution
    resumes as soon as any interrupt is triggered, or at most one millisecond
    after the CPU was paused.

    It is recommended to call this function inside any tight loop that is
    continuously checking for an external change (i.e. polling). This will reduce
    power consumption without significantly impacting performance. To reduce
    power consumption further then see the :func:`lightsleep`,
    :func:`time.sleep()` and :func:`time.sleep_ms()` functions.
    """
    ...

def sleep() -> Incomplete:
    """
    ``Note:`` This function is deprecated, use :func:`lightsleep()` instead with no arguments.
    """
    ...

def lightsleep(time_ms: Optional[Any] = None) -> Incomplete:
    """
    Stops execution in an attempt to enter a low power state.

    If *time_ms* is specified then this will be the maximum time in milliseconds that
    the sleep will last for.  Otherwise the sleep can last indefinitely.

    With or without a timeout, execution may resume at any time if there are events
    that require processing.  Such events, or wake sources, should be configured before
    sleeping, like `Pin` change or `RTC` timeout.

    The precise behaviour and power-saving capabilities of lightsleep and deepsleep is
    highly dependent on the underlying hardware, but the general properties are:

    * A lightsleep has full RAM and state retention.  Upon wake execution is resumed
      from the point where the sleep was requested, with all subsystems operational.

    * A deepsleep may not retain RAM or any other state of the system (for example
      peripherals or network interfaces).  Upon wake execution is resumed from the main
      script, similar to a hard or power-on reset. The `reset_cause()` function will
      return `machine.DEEPSLEEP` and this can be used to distinguish a deepsleep wake
      from other resets.
    """
    ...

def deepsleep(time_ms: Optional[Any] = None) -> NoReturn:
    """
    Stops execution in an attempt to enter a low power state.

    If *time_ms* is specified then this will be the maximum time in milliseconds that
    the sleep will last for.  Otherwise the sleep can last indefinitely.

    With or without a timeout, execution may resume at any time if there are events
    that require processing.  Such events, or wake sources, should be configured before
    sleeping, like `Pin` change or `RTC` timeout.

    The precise behaviour and power-saving capabilities of lightsleep and deepsleep is
    highly dependent on the underlying hardware, but the general properties are:

    * A lightsleep has full RAM and state retention.  Upon wake execution is resumed
      from the point where the sleep was requested, with all subsystems operational.

    * A deepsleep may not retain RAM or any other state of the system (for example
      peripherals or network interfaces).  Upon wake execution is resumed from the main
      script, similar to a hard or power-on reset. The `reset_cause()` function will
      return `machine.DEEPSLEEP` and this can be used to distinguish a deepsleep wake
      from other resets.
    """
    ...

def wake_reason() -> Incomplete:
    """
    Get the wake reason. See :ref:`constants <machine_constants>` for the possible return values.

    Availability: ESP32, WiPy.
    """
    ...

def unique_id() -> bytes:
    """
    Returns a byte string with a unique identifier of a board/SoC. It will vary
    from a board/SoC instance to another, if underlying hardware allows. Length
    varies by hardware (so use substring of a full value if you expect a short
    ID). In some MicroPython ports, ID corresponds to the network MAC address.
    """
    ...

def time_pulse_us(
    pin,
    pulse_level,
    timeout_us=1000000,
) -> int:
    """
    Time a pulse on the given *pin*, and return the duration of the pulse in
    microseconds.  The *pulse_level* argument should be 0 to time a low pulse
    or 1 to time a high pulse.

    If the current input value of the pin is different to *pulse_level*,
    the function first (*) waits until the pin input becomes equal to *pulse_level*,
    then (**) times the duration that the pin is equal to *pulse_level*.
    If the pin is already equal to *pulse_level* then timing starts straight away.

    The function will return -2 if there was timeout waiting for condition marked
    (*) above, and -1 if there was timeout during the main measurement, marked (**)
    above. The timeout is the same for both cases and given by *timeout_us* (which
    is in microseconds).
    """
    ...

def bitstream(
    pin,
    encoding,
    timing,
    data,
) -> Incomplete:
    """
    Transmits *data* by bit-banging the specified *pin*. The *encoding* argument
    specifies how the bits are encoded, and *timing* is an encoding-specific timing
    specification.

    The supported encodings are:

      - ``0`` for "high low" pulse duration modulation. This will transmit 0 and
        1 bits as timed pulses, starting with the most significant bit.
        The *timing* must be a four-tuple of nanoseconds in the format
        ``(high_time_0, low_time_0, high_time_1, low_time_1)``. For example,
        ``(400, 850, 800, 450)`` is the timing specification for WS2812 RGB LEDs
        at 800kHz.

    The accuracy of the timing varies between ports. On Cortex M0 at 48MHz, it is
    at best +/- 120ns, however on faster MCUs (ESP8266, ESP32, STM32, Pyboard), it
    will be closer to +/-30ns.

    ``Note:`` For controlling WS2812 / NeoPixel strips, see the :mod:`neopixel`
       module for a higher-level API.
    """
    ...

def rng() -> int:
    """
    Return a 24-bit software generated random number.

    Availability: WiPy.
    """
    ...
