"""
Functions related to the hardware.

MicroPython module: https://docs.micropython.org/en/v1.21.0/library/machine.html

The ``machine`` module contains specific functions related to the hardware
on a particular board. Most functions in this module allow to achieve direct
and unrestricted access to and control of hardware blocks on a system
(like CPU, timers, buses, etc.). Used incorrectly, this can lead to
malfunction, lockups, crashes of your board, and in extreme cases, hardware
damage.

---
Module: 'umachine' on micropython-v1.21.0-samd-SEEED_WIO_TERMINAL
"""

from __future__ import annotations

# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'cpu': 'SAMD51P19A', 'mpy': 'v6.1', 'arch': 'armv7emsp'}
# Stubber: v1.16.2
from _typeshed import Incomplete
from typing import Any, Callable, List, NoReturn, Optional, Tuple, Union

PWRON_RESET = 1  # type: int
HARD_RESET = 16  # type: int
SOFT_RESET = 64  # type: int
WDT_RESET = 32  # type: int
DEEPSLEEP_RESET = 128  # type: int


def dht_readinto(*args, **kwargs) -> Incomplete: ...


def enable_irq(state) -> Incomplete:
    """
    Re-enable interrupt requests.
    The *state* parameter should be the value that was returned from the most
    recent call to the `disable_irq()` function.
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


def bootloader(value: Optional[Any] = None) -> None:
    """
    Reset the device and enter its bootloader.  This is typically used to put the
    device into a state where it can be programmed with new firmware.

    Some ports support passing in an optional *value* argument which can control
    which bootloader to enter, what to pass to it, or other things.
    """
    ...


def reset_cause() -> int:
    """
    Get the reset cause. See :ref:`constants <machine_constants>` for the possible return values.
    """
    ...


def soft_reset() -> NoReturn:
    """
    Performs a soft reset of the interpreter, deleting all Python objects and
    resetting the Python heap.  It tries to retain the method by which the user
    is connected to the MicroPython REPL (eg serial, USB, Wifi).
    """
    ...


def freq(hz: Optional[Any] = None) -> Incomplete:
    """
    Returns the CPU frequency in hertz.

    On some ports this can also be used to set the CPU frequency by passing in *hz*.
    """
    ...


def reset() -> NoReturn:
    """
    Resets the device in a manner similar to pushing the external RESET
    button.
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


def idle() -> Incomplete:
    """
    Gates the clock to the CPU, useful to reduce power consumption at any time during
    short or long periods. Peripherals continue working and execution resumes as soon
    as any interrupt is triggered (on many ports this includes system timer
    interrupt occurring at regular intervals on the order of millisecond).
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


class WDT:
    """
    Create a WDT object and start it. The timeout must be given in milliseconds.
    Once it is running the timeout cannot be changed and the WDT cannot be stopped either.

    Notes: On the esp8266 a timeout cannot be specified, it is determined by the underlying system.
    On rp2040 devices, the maximum timeout is 8388 ms.
    """

    def timeout_ms(self, *args, **kwargs) -> Incomplete: ...

    def feed(self) -> None:
        """
        Feed the WDT to prevent it from resetting the system. The application
        should place this call in a sensible place ensuring that the WDT is
        only fed after verifying that everything is functioning correctly.
        """
        ...

    def __init__(self, *argv, **kwargs) -> None: ...


mem8: Incomplete  ## <class 'mem'> = <8-bit memory>
mem32: Incomplete  ## <class 'mem'> = <32-bit memory>
mem16: Incomplete  ## <class 'mem'> = <16-bit memory>


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

    def duty_u16(self, value: Optional[Any] = None) -> int:
        """
        Get or set the current duty cycle of the PWM output, as an unsigned 16-bit
        value in the range 0 to 65535 inclusive.

        With no arguments the duty cycle is returned.

        With a single *value* argument the duty cycle is set to that value, measured
        as the ratio ``value / 65535``.
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

    def init(self, *, freq, duty_u16, duty_ns) -> None:
        """
        Modify settings for the PWM object.  See the above constructor for details
        about the parameters.
        """
        ...

    def duty_ns(self, value: Optional[Any] = None) -> int:
        """
        Get or set the current pulse width of the PWM output, as a value in nanoseconds.

        With no arguments the pulse width in nanoseconds is returned.

        With a single *value* argument the pulse width is set to that value.
        """
        ...

    def deinit(self) -> None:
        """
        Disable the PWM output.
        """
        ...

    def __init__(self, *argv, **kwargs) -> None: ...


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

    def read_u16(self) -> int:
        """
        Take an analog reading and return an integer in the range 0-65535.
        The return value represents the raw reading taken by the ADC, scaled
        such that the minimum value is 0 and the maximum value is 65535.
        """
        ...

    def deinit(self, *args, **kwargs) -> Incomplete: ...

    def __init__(self, *argv, **kwargs) -> None: ...


class DAC:
    def write(self, *args, **kwargs) -> Incomplete: ...

    def __init__(self, *argv, **kwargs) -> None: ...


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

    def readfrom_mem(self, addr, memaddr, nbytes, *, addrsize=8) -> bytes:
        """
        Read *nbytes* from the peripheral specified by *addr* starting from the memory
        address specified by *memaddr*.
        The argument *addrsize* specifies the address size in bits.
        Returns a `bytes` object with the data read.
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

    def scan(self) -> List:
        """
        Scan all I2C addresses between 0x08 and 0x77 inclusive and return a list of
        those that respond.  A device responds if it pulls the SDA line low after
        its address (including a write bit) is sent on the bus.
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

    def start(self) -> None:
        """
        Generate a START condition on the bus (SDA transitions to low while SCL is high).
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

    def stop(self) -> None:
        """
        Generate a STOP condition on the bus (SDA transitions to high while SCL is high).
        """
        ...

    def write(self, buf) -> int:
        """
        Write the bytes from *buf* to the bus.  Checks that an ACK is received
        after each byte and stops transmitting the remaining bytes if a NACK is
        received.  The function returns the number of ACKs that were received.
        """
        ...

    def __init__(self, *argv, **kwargs) -> None: ...


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

    OUT = 1  # type: int
    OPEN_DRAIN = 2  # type: int
    LOW_POWER = 0  # type: int
    PULL_DOWN = 2  # type: int
    PULL_OFF = 0  # type: int
    PULL_UP = 1  # type: int
    IRQ_RISING = 1  # type: int
    HIGH_POWER = 1  # type: int
    IN = 0  # type: int
    IRQ_FALLING = 2  # type: int

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

    def toggle(self, *args, **kwargs) -> Incomplete: ...

    def init(self, mode=-1, pull=-1, *, value=None, drive=0, alt=-1) -> None:
        """
        Re-initialise the pin using the given parameters.  Only those arguments that
        are specified will be set.  The rest of the pin peripheral state will remain
        unchanged.  See the constructor documentation for details of the arguments.

        Returns ``None``.
        """
        ...

    def on(self) -> None:
        """
        Set pin to "1" output level.
        """
        ...

    def low(self) -> None:
        """
        Set pin to "0" output level.

        Availability: nrf, rp2, stm32 ports.
        """
        ...

    def off(self) -> None:
        """
        Set pin to "0" output level.
        """
        ...

    def high(self) -> None:
        """
        Set pin to "1" output level.

        Availability: nrf, rp2, stm32 ports.
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

    def disable(self, *args, **kwargs) -> Incomplete: ...

    def drive(self, drive: Optional[Any] = None) -> Incomplete:
        """
        Get or set the pin drive strength.
        See the constructor documentation for details of the ``drive`` argument.

        Availability: cc3200 port.
        """
        ...

    class board:
        LCD_YU: Incomplete  ## <class 'Pin'> = Pin("LCD_YU", mode=IN, pull=PULL_OFF, GPIO=PC11)
        QSPI_SCK: Incomplete  ## <class 'Pin'> = Pin("QSPI_SCK", mode=IN, pull=PULL_OFF, GPIO=PB10)
        QSPI_D3: Incomplete  ## <class 'Pin'> = Pin("QSPI_D3", mode=IN, pull=PULL_OFF, GPIO=PA11)
        QSPI_D2: Incomplete  ## <class 'Pin'> = Pin("QSPI_D2", mode=IN, pull=PULL_OFF, GPIO=PA10)
        RX: Incomplete  ## <class 'Pin'> = Pin("RX", mode=IN, pull=PULL_OFF, GPIO=PB27)
        SCL1: Incomplete  ## <class 'Pin'> = Pin("SCL1", mode=IN, pull=PULL_OFF, GPIO=PA16)
        SCL0: Incomplete  ## <class 'Pin'> = Pin("SCL0", mode=IN, pull=PULL_OFF, GPIO=PA12)
        SCK: Incomplete  ## <class 'Pin'> = Pin("SCK", mode=IN, pull=PULL_OFF, GPIO=PB03)
        QSPI_D1: Incomplete  ## <class 'Pin'> = Pin("QSPI_D1", mode=IN, pull=PULL_OFF, GPIO=PA09)
        MIC: Incomplete  ## <class 'Pin'> = Pin("MIC", mode=IN, pull=PULL_OFF, GPIO=PC30)
        LED_LCD: Incomplete  ## <class 'Pin'> = Pin("LED_LCD", mode=IN, pull=PULL_OFF, GPIO=PC05)
        LED_BLUE: Incomplete  ## <class 'Pin'> = Pin("LED_BLUE", mode=OUT, pull=PULL_OFF, GPIO=PA15)
        MISO: Incomplete  ## <class 'Pin'> = Pin("MISO", mode=IN, pull=PULL_OFF, GPIO=PB00)
        QSPI_D0: Incomplete  ## <class 'Pin'> = Pin("QSPI_D0", mode=IN, pull=PULL_OFF, GPIO=PA08)
        QSPI_CS: Incomplete  ## <class 'Pin'> = Pin("QSPI_CS", mode=IN, pull=PULL_OFF, GPIO=PB11)
        MOSI: Incomplete  ## <class 'Pin'> = Pin("MOSI", mode=IN, pull=PULL_OFF, GPIO=PB02)
        SDA0: Incomplete  ## <class 'Pin'> = Pin("SDA0", mode=IN, pull=PULL_OFF, GPIO=PA13)
        SWITCH_X: Incomplete  ## <class 'Pin'> = Pin("SWITCH_X", mode=IN, pull=PULL_OFF, GPIO=PD08)
        SWITCH_U: Incomplete  ## <class 'Pin'> = Pin("SWITCH_U", mode=IN, pull=PULL_OFF, GPIO=PD20)
        SWITCH_B: Incomplete  ## <class 'Pin'> = Pin("SWITCH_B", mode=IN, pull=PULL_OFF, GPIO=PD12)
        SWITCH_Y: Incomplete  ## <class 'Pin'> = Pin("SWITCH_Y", mode=IN, pull=PULL_OFF, GPIO=PD09)
        USB_DM: Incomplete  ## <class 'Pin'> = Pin("USB_DM", mode=OUT, pull=PULL_OFF, GPIO=PA24)
        TX: Incomplete  ## <class 'Pin'> = Pin("TX", mode=IN, pull=PULL_OFF, GPIO=PB26)
        SWITCH_Z: Incomplete  ## <class 'Pin'> = Pin("SWITCH_Z", mode=IN, pull=PULL_OFF, GPIO=PD10)
        SWDIO: Incomplete  ## <class 'Pin'> = Pin("SWDIO", mode=IN, pull=PULL_OFF, GPIO=PA31)
        SD_DET: Incomplete  ## <class 'Pin'> = Pin("SD_DET", mode=IN, pull=PULL_OFF, GPIO=PD21)
        SD_CS: Incomplete  ## <class 'Pin'> = Pin("SD_CS", mode=IN, pull=PULL_OFF, GPIO=PC19)
        SDA1: Incomplete  ## <class 'Pin'> = Pin("SDA1", mode=IN, pull=PULL_OFF, GPIO=PA17)
        SD_MISO: Incomplete  ## <class 'Pin'> = Pin("SD_MISO", mode=IN, pull=PULL_OFF, GPIO=PC18)
        SWCLK: Incomplete  ## <class 'Pin'> = Pin("SWCLK", mode=IN, pull=PULL_OFF, GPIO=PA30)
        SD_SCK: Incomplete  ## <class 'Pin'> = Pin("SD_SCK", mode=IN, pull=PULL_OFF, GPIO=PC17)
        SD_MOSI: Incomplete  ## <class 'Pin'> = Pin("SD_MOSI", mode=IN, pull=PULL_OFF, GPIO=PC16)
        USB_DP: Incomplete  ## <class 'Pin'> = Pin("USB_DP", mode=OUT, pull=PULL_OFF, GPIO=PA25)
        LCD_YD: Incomplete  ## <class 'Pin'> = Pin("LCD_YD", mode=IN, pull=PULL_OFF, GPIO=PC13)
        BUTTON_2: Incomplete  ## <class 'Pin'> = Pin("BUTTON_2", mode=IN, pull=PULL_OFF, GPIO=PC27)
        BUTTON_1: Incomplete  ## <class 'Pin'> = Pin("BUTTON_1", mode=IN, pull=PULL_OFF, GPIO=PC26)
        A8_D8: Incomplete  ## <class 'Pin'> = Pin("A8_D8", mode=IN, pull=PULL_OFF, GPIO=PA06)
        BUTTON_3: Incomplete  ## <class 'Pin'> = Pin("BUTTON_3", mode=IN, pull=PULL_OFF, GPIO=PC28)
        ENABLE_3V3: Incomplete  ## <class 'Pin'> = Pin("ENABLE_3V3", mode=IN, pull=PULL_OFF, GPIO=PC15)
        CS: Incomplete  ## <class 'Pin'> = Pin("CS", mode=IN, pull=PULL_OFF, GPIO=PB01)
        BUZZER: Incomplete  ## <class 'Pin'> = Pin("BUZZER", mode=IN, pull=PULL_OFF, GPIO=PD11)
        A7_D7: Incomplete  ## <class 'Pin'> = Pin("A7_D7", mode=IN, pull=PULL_OFF, GPIO=PB07)
        A2_D2: Incomplete  ## <class 'Pin'> = Pin("A2_D2", mode=IN, pull=PULL_OFF, GPIO=PA07)
        A1_D1: Incomplete  ## <class 'Pin'> = Pin("A1_D1", mode=IN, pull=PULL_OFF, GPIO=PB09)
        A0_D0: Incomplete  ## <class 'Pin'> = Pin("A0_D0", mode=IN, pull=PULL_OFF, GPIO=PB08)
        A3_D3: Incomplete  ## <class 'Pin'> = Pin("A3_D3", mode=IN, pull=PULL_OFF, GPIO=PB04)
        A6_D6: Incomplete  ## <class 'Pin'> = Pin("A6_D6", mode=IN, pull=PULL_OFF, GPIO=PA04)
        A5_D5: Incomplete  ## <class 'Pin'> = Pin("A5_D5", mode=IN, pull=PULL_OFF, GPIO=PB06)
        A4_D4: Incomplete  ## <class 'Pin'> = Pin("A4_D4", mode=IN, pull=PULL_OFF, GPIO=PB05)
        ENABLE_5V: Incomplete  ## <class 'Pin'> = Pin("ENABLE_5V", mode=IN, pull=PULL_OFF, GPIO=PC14)
        LCD_MOSI: Incomplete  ## <class 'Pin'> = Pin("LCD_MOSI", mode=IN, pull=PULL_OFF, GPIO=PB19)
        LCD_MISO: Incomplete  ## <class 'Pin'> = Pin("LCD_MISO", mode=IN, pull=PULL_OFF, GPIO=PB18)
        LCD_D_C: Incomplete  ## <class 'Pin'> = Pin("LCD_D_C", mode=IN, pull=PULL_OFF, GPIO=PC06)
        LCD_RESET: Incomplete  ## <class 'Pin'> = Pin("LCD_RESET", mode=IN, pull=PULL_OFF, GPIO=PC07)
        LCD_XR: Incomplete  ## <class 'Pin'> = Pin("LCD_XR", mode=IN, pull=PULL_OFF, GPIO=PC12)
        LCD_XL: Incomplete  ## <class 'Pin'> = Pin("LCD_XL", mode=IN, pull=PULL_OFF, GPIO=PC10)
        LCD_SCK: Incomplete  ## <class 'Pin'> = Pin("LCD_SCK", mode=IN, pull=PULL_OFF, GPIO=PB20)
        LCD_CS: Incomplete  ## <class 'Pin'> = Pin("LCD_CS", mode=IN, pull=PULL_OFF, GPIO=PB21)
        GPCLK2: Incomplete  ## <class 'Pin'> = Pin("GPCLK2", mode=IN, pull=PULL_OFF, GPIO=PB13)
        GPCLK1: Incomplete  ## <class 'Pin'> = Pin("GPCLK1", mode=IN, pull=PULL_OFF, GPIO=PB12)
        GPCLK0: Incomplete  ## <class 'Pin'> = Pin("GPCLK0", mode=IN, pull=PULL_OFF, GPIO=PB15)
        I2C_BCLK: Incomplete  ## <class 'Pin'> = Pin("I2C_BCLK", mode=IN, pull=PULL_OFF, GPIO=PB16)
        I2S_SDOUT: Incomplete  ## <class 'Pin'> = Pin("I2S_SDOUT", mode=IN, pull=PULL_OFF, GPIO=PA22)
        I2S_SDIN: Incomplete  ## <class 'Pin'> = Pin("I2S_SDIN", mode=IN, pull=PULL_OFF, GPIO=PA21)
        I2S_LRCLK: Incomplete  ## <class 'Pin'> = Pin("I2S_LRCLK", mode=IN, pull=PULL_OFF, GPIO=PA20)

        def __init__(self, *argv, **kwargs) -> None: ...

    class cpu:
        PC04: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC04)
        PC14: Incomplete  ## <class 'Pin'> = Pin("ENABLE_5V", mode=IN, pull=PULL_OFF, GPIO=PC14)
        PC05: Incomplete  ## <class 'Pin'> = Pin("LED_LCD", mode=IN, pull=PULL_OFF, GPIO=PC05)
        PC01: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC01)
        PC03: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC03)
        PC02: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC02)
        PC12: Incomplete  ## <class 'Pin'> = Pin("LCD_XR", mode=IN, pull=PULL_OFF, GPIO=PC12)
        PC06: Incomplete  ## <class 'Pin'> = Pin("LCD_D_C", mode=IN, pull=PULL_OFF, GPIO=PC06)
        PC13: Incomplete  ## <class 'Pin'> = Pin("LCD_YD", mode=IN, pull=PULL_OFF, GPIO=PC13)
        PC07: Incomplete  ## <class 'Pin'> = Pin("LCD_RESET", mode=IN, pull=PULL_OFF, GPIO=PC07)
        PC11: Incomplete  ## <class 'Pin'> = Pin("LCD_YU", mode=IN, pull=PULL_OFF, GPIO=PC11)
        PC10: Incomplete  ## <class 'Pin'> = Pin("LCD_XL", mode=IN, pull=PULL_OFF, GPIO=PC10)
        PB24: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB24)
        PC00: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC00)
        PB25: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB25)
        PB21: Incomplete  ## <class 'Pin'> = Pin("LCD_CS", mode=IN, pull=PULL_OFF, GPIO=PB21)
        PB23: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB23)
        PB22: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB22)
        PB30: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB30)
        PB26: Incomplete  ## <class 'Pin'> = Pin("TX", mode=IN, pull=PULL_OFF, GPIO=PB26)
        PB31: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB31)
        PB27: Incomplete  ## <class 'Pin'> = Pin("RX", mode=IN, pull=PULL_OFF, GPIO=PB27)
        PB29: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB29)
        PB28: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB28)
        PB20: Incomplete  ## <class 'Pin'> = Pin("LCD_SCK", mode=IN, pull=PULL_OFF, GPIO=PB20)
        PD00: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PD00)
        PC15: Incomplete  ## <class 'Pin'> = Pin("ENABLE_3V3", mode=IN, pull=PULL_OFF, GPIO=PC15)
        PD01: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PD01)
        PC28: Incomplete  ## <class 'Pin'> = Pin("BUTTON_3", mode=IN, pull=PULL_OFF, GPIO=PC28)
        PC31: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC31)
        PC30: Incomplete  ## <class 'Pin'> = Pin("MIC", mode=IN, pull=PULL_OFF, GPIO=PC30)
        PD12: Incomplete  ## <class 'Pin'> = Pin("SWITCH_B", mode=IN, pull=PULL_OFF, GPIO=PD12)
        PD08: Incomplete  ## <class 'Pin'> = Pin("SWITCH_X", mode=IN, pull=PULL_OFF, GPIO=PD08)
        PD20: Incomplete  ## <class 'Pin'> = Pin("SWITCH_U", mode=IN, pull=PULL_OFF, GPIO=PD20)
        PD09: Incomplete  ## <class 'Pin'> = Pin("SWITCH_Y", mode=IN, pull=PULL_OFF, GPIO=PD09)
        PD11: Incomplete  ## <class 'Pin'> = Pin("BUZZER", mode=IN, pull=PULL_OFF, GPIO=PD11)
        PD10: Incomplete  ## <class 'Pin'> = Pin("SWITCH_Z", mode=IN, pull=PULL_OFF, GPIO=PD10)
        PC19: Incomplete  ## <class 'Pin'> = Pin("SD_CS", mode=IN, pull=PULL_OFF, GPIO=PC19)
        PC27: Incomplete  ## <class 'Pin'> = Pin("BUTTON_2", mode=IN, pull=PULL_OFF, GPIO=PC27)
        PC20: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC20)
        PC16: Incomplete  ## <class 'Pin'> = Pin("SD_MOSI", mode=IN, pull=PULL_OFF, GPIO=PC16)
        PC18: Incomplete  ## <class 'Pin'> = Pin("SD_MISO", mode=IN, pull=PULL_OFF, GPIO=PC18)
        PC17: Incomplete  ## <class 'Pin'> = Pin("SD_SCK", mode=IN, pull=PULL_OFF, GPIO=PC17)
        PC25: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC25)
        PC21: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC21)
        PC26: Incomplete  ## <class 'Pin'> = Pin("BUTTON_1", mode=IN, pull=PULL_OFF, GPIO=PC26)
        PC22: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC22)
        PC24: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC24)
        PC23: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC23)
        PD21: Incomplete  ## <class 'Pin'> = Pin("SD_DET", mode=IN, pull=PULL_OFF, GPIO=PD21)
        PA15: Incomplete  ## <class 'Pin'> = Pin("LED_BLUE", mode=OUT, pull=PULL_OFF, GPIO=PA15)
        PA23: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA23)
        PA16: Incomplete  ## <class 'Pin'> = Pin("SCL1", mode=IN, pull=PULL_OFF, GPIO=PA16)
        PA12: Incomplete  ## <class 'Pin'> = Pin("SCL0", mode=IN, pull=PULL_OFF, GPIO=PA12)
        PA14: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA14)
        PA13: Incomplete  ## <class 'Pin'> = Pin("SDA0", mode=IN, pull=PULL_OFF, GPIO=PA13)
        PA21: Incomplete  ## <class 'Pin'> = Pin("I2S_SDIN", mode=IN, pull=PULL_OFF, GPIO=PA21)
        PA17: Incomplete  ## <class 'Pin'> = Pin("SDA1", mode=IN, pull=PULL_OFF, GPIO=PA17)
        PA22: Incomplete  ## <class 'Pin'> = Pin("I2S_SDOUT", mode=IN, pull=PULL_OFF, GPIO=PA22)
        PA18: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA18)
        PA20: Incomplete  ## <class 'Pin'> = Pin("I2S_LRCLK", mode=IN, pull=PULL_OFF, GPIO=PA20)
        PA19: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA19)
        PA03: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA03)
        PA11: Incomplete  ## <class 'Pin'> = Pin("QSPI_D3", mode=IN, pull=PULL_OFF, GPIO=PA11)
        PA04: Incomplete  ## <class 'Pin'> = Pin("A6_D6", mode=IN, pull=PULL_OFF, GPIO=PA04)
        PA00: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA00)
        PA02: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA02)
        PA01: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA01)
        PA09: Incomplete  ## <class 'Pin'> = Pin("QSPI_D1", mode=IN, pull=PULL_OFF, GPIO=PA09)
        PA05: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA05)
        PA10: Incomplete  ## <class 'Pin'> = Pin("QSPI_D2", mode=IN, pull=PULL_OFF, GPIO=PA10)
        PA06: Incomplete  ## <class 'Pin'> = Pin("A8_D8", mode=IN, pull=PULL_OFF, GPIO=PA06)
        PA08: Incomplete  ## <class 'Pin'> = Pin("QSPI_D0", mode=IN, pull=PULL_OFF, GPIO=PA08)
        PA07: Incomplete  ## <class 'Pin'> = Pin("A2_D2", mode=IN, pull=PULL_OFF, GPIO=PA07)
        PB19: Incomplete  ## <class 'Pin'> = Pin("LCD_MOSI", mode=IN, pull=PULL_OFF, GPIO=PB19)
        PB11: Incomplete  ## <class 'Pin'> = Pin("QSPI_CS", mode=IN, pull=PULL_OFF, GPIO=PB11)
        PA24: Incomplete  ## <class 'Pin'> = Pin("USB_DM", mode=OUT, pull=PULL_OFF, GPIO=PA24)
        PB12: Incomplete  ## <class 'Pin'> = Pin("GPCLK1", mode=IN, pull=PULL_OFF, GPIO=PB12)
        PB08: Incomplete  ## <class 'Pin'> = Pin("A0_D0", mode=IN, pull=PULL_OFF, GPIO=PB08)
        PB10: Incomplete  ## <class 'Pin'> = Pin("QSPI_SCK", mode=IN, pull=PULL_OFF, GPIO=PB10)
        PB09: Incomplete  ## <class 'Pin'> = Pin("A1_D1", mode=IN, pull=PULL_OFF, GPIO=PB09)
        PB17: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB17)
        PB13: Incomplete  ## <class 'Pin'> = Pin("GPCLK2", mode=IN, pull=PULL_OFF, GPIO=PB13)
        PB18: Incomplete  ## <class 'Pin'> = Pin("LCD_MISO", mode=IN, pull=PULL_OFF, GPIO=PB18)
        PB14: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB14)
        PB16: Incomplete  ## <class 'Pin'> = Pin("I2C_BCLK", mode=IN, pull=PULL_OFF, GPIO=PB16)
        PB15: Incomplete  ## <class 'Pin'> = Pin("GPCLK0", mode=IN, pull=PULL_OFF, GPIO=PB15)
        PA31: Incomplete  ## <class 'Pin'> = Pin("SWDIO", mode=IN, pull=PULL_OFF, GPIO=PA31)
        PB07: Incomplete  ## <class 'Pin'> = Pin("A7_D7", mode=IN, pull=PULL_OFF, GPIO=PB07)
        PB00: Incomplete  ## <class 'Pin'> = Pin("MISO", mode=IN, pull=PULL_OFF, GPIO=PB00)
        PA25: Incomplete  ## <class 'Pin'> = Pin("USB_DP", mode=OUT, pull=PULL_OFF, GPIO=PA25)
        PA30: Incomplete  ## <class 'Pin'> = Pin("SWCLK", mode=IN, pull=PULL_OFF, GPIO=PA30)
        PA27: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA27)
        PB05: Incomplete  ## <class 'Pin'> = Pin("A4_D4", mode=IN, pull=PULL_OFF, GPIO=PB05)
        PB01: Incomplete  ## <class 'Pin'> = Pin("CS", mode=IN, pull=PULL_OFF, GPIO=PB01)
        PB06: Incomplete  ## <class 'Pin'> = Pin("A5_D5", mode=IN, pull=PULL_OFF, GPIO=PB06)
        PB02: Incomplete  ## <class 'Pin'> = Pin("MOSI", mode=IN, pull=PULL_OFF, GPIO=PB02)
        PB04: Incomplete  ## <class 'Pin'> = Pin("A3_D3", mode=IN, pull=PULL_OFF, GPIO=PB04)
        PB03: Incomplete  ## <class 'Pin'> = Pin("SCK", mode=IN, pull=PULL_OFF, GPIO=PB03)

        def __init__(self, *argv, **kwargs) -> None: ...

    def __init__(self, *argv, **kwargs) -> None: ...

    def __call__(self, x: Optional[Any] = None) -> Incomplete:
        """
        Pin objects are callable.  The call method provides a (fast) shortcut to set
        and get the value of the pin.  It is equivalent to Pin.value([x]).
        See :meth:`Pin.value` for more details.
        """
        ...


class SoftSPI(SPI):
    """
    Construct a new software SPI object.  Additional parameters must be
    given, usually at least *sck*, *mosi* and *miso*, and these are used
    to initialise the bus.  See `SPI.init` for a description of the parameters.
    """

    LSB = 1  # type: int
    MSB = 0  # type: int

    def deinit(self, *args, **kwargs) -> Incomplete: ...

    def init(self, *args, **kwargs) -> Incomplete: ...

    def write_readinto(self, *args, **kwargs) -> Incomplete: ...

    def read(self, *args, **kwargs) -> Incomplete: ...

    def write(self, *args, **kwargs) -> Incomplete: ...

    def readinto(self, *args, **kwargs) -> Incomplete: ...

    def __init__(self, *argv, **kwargs) -> None: ...


class Timer:
    """
    Construct a new timer object of the given ``id``. ``id`` of -1 constructs a
    virtual timer (if supported by a board).
    ``id`` shall not be passed as a keyword argument.

    See ``init`` for parameters of initialisation.
    """

    PERIODIC = 2  # type: int
    ONE_SHOT = 1  # type: int

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

    def __init__(self, *argv, **kwargs) -> None: ...


class UART:
    """
    Construct a UART object of the given id.
    """

    def flush(self) -> Incomplete:
        """
        Waits until all data has been sent. In case of a timeout, an exception is raised. The timeout
        duration depends on the tx buffer size and the baud rate. Unless flow control is enabled, a timeout
        should not occur.

        .. note::

            For the rp2, esp8266 and nrf ports the call returns while the last byte is sent.
            If required, a one character wait time has to be added in the calling script.

        Availability: rp2, esp32, esp8266, mimxrt, cc3200, stm32, nrf ports, renesas-ra
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

    def txdone(self) -> bool:
        """
        Tells whether all data has been sent or no data transfer is happening. In this case,
        it returns ``True``. If a data transmission is ongoing it returns ``False``.

        .. note::

            For the rp2, esp8266 and nrf ports the call may return ``True`` even if the last byte
            of a transfer is still being sent. If required, a one character wait time has to be
            added in the calling script.

        Availability: rp2, esp32, esp8266, mimxrt, cc3200, stm32, nrf ports, renesas-ra
        """
        ...

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

    def sendbreak(self) -> None:
        """
        Send a break condition on the bus. This drives the bus low for a duration
        longer than required for a normal transmission of a character.
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

    def write(self, buf) -> Union[int, None]:
        """
        Write the buffer of bytes to the bus.

        Return value: number of bytes written or ``None`` on timeout.
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

    def __init__(self, *argv, **kwargs) -> None: ...


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

    def readfrom_mem_into(self, *args, **kwargs) -> Incomplete: ...

    def readfrom_into(self, *args, **kwargs) -> Incomplete: ...

    def readfrom_mem(self, *args, **kwargs) -> Incomplete: ...

    def writeto_mem(self, *args, **kwargs) -> Incomplete: ...

    def scan(self, *args, **kwargs) -> Incomplete: ...

    def writeto(self, *args, **kwargs) -> Incomplete: ...

    def writevto(self, *args, **kwargs) -> Incomplete: ...

    def start(self, *args, **kwargs) -> Incomplete: ...

    def readfrom(self, *args, **kwargs) -> Incomplete: ...

    def readinto(self, *args, **kwargs) -> Incomplete: ...

    def init(self, *args, **kwargs) -> Incomplete: ...

    def stop(self, *args, **kwargs) -> Incomplete: ...

    def write(self, *args, **kwargs) -> Incomplete: ...

    def __init__(self, *argv, **kwargs) -> None: ...


class RTC:
    """
    Create an RTC object. See init for parameters of initialization.
    """

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

    def calibration(self, *args, **kwargs) -> Incomplete: ...

    def __init__(self, *argv, **kwargs) -> None: ...


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

    LSB = 1  # type: int
    MSB = 0  # type: int

    def deinit(self) -> None:
        """
        Turn off the SPI bus.
        """
        ...

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

    def write_readinto(self, write_buf, read_buf) -> int:
        """
        Write the bytes from ``write_buf`` while reading into ``read_buf``.  The
        buffers can be the same or different, but both buffers must have the
        same length.
        Returns ``None``.

        Note: on WiPy this function returns the number of bytes written.
        """
        ...

    def read(self, nbytes, write=0x00) -> bytes:
        """
        Read a number of bytes specified by ``nbytes`` while continuously writing
        the single byte given by ``write``.
        Returns a ``bytes`` object with the data that was read.
        """
        ...

    def write(self, buf) -> int:
        """
        Write the bytes contained in ``buf``.
        Returns ``None``.

        Note: on WiPy this function returns the number of bytes written.
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

    def __init__(self, *argv, **kwargs) -> None: ...


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

    def off(self) -> None:
        """
        Deactivate signal.
        """
        ...

    def on(self) -> None:
        """
        Activate signal.
        """
        ...

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

    def __init__(self, *argv, **kwargs) -> None: ...
