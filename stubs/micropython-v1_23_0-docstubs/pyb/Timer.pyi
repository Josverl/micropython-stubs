""" """

from __future__ import annotations
from typing import Any, Optional
from _typeshed import Incomplete

class Timer:
    """
    Construct a new timer object of the given id.  If additional
    arguments are given, then the timer is initialised by ``init(...)``.
    ``id`` can be 1 to 14.
    """

    UP: int
    """Configures the timer to count Up, Down, or from 0 to ARR and then back down to 0."""
    DOWN: int
    """Configures the timer to count Up, Down, or from 0 to ARR and then back down to 0."""
    CENTER: int
    """Configures the timer to count Up, Down, or from 0 to ARR and then back down to 0."""
    BRK_OFF: Incomplete
    """Configures the break mode when passed to the ``brk`` keyword argument."""
    BRK_LOW: Incomplete
    """Configures the break mode when passed to the ``brk`` keyword argument."""
    BRK_HIGH: Incomplete
    """Configures the break mode when passed to the ``brk`` keyword argument."""
    def __init__(self, id, *args, **kwargs) -> None: ...
    def init(self, *, freq, prescaler, period, mode=UP, div=1, callback=None, deadtime=0, brk=BRK_OFF) -> None:
        """
        Initialise the timer.  Initialisation must be either by frequency (in Hz)
        or by prescaler and period::

            tim.init(freq=100)                  # set the timer to trigger at 100Hz
            tim.init(prescaler=83, period=999)  # set the prescaler and period directly

        Keyword arguments:

          - ``freq`` --- specifies the periodic frequency of the timer. You might also
            view this as the frequency with which the timer goes through one complete cycle.

          - ``prescaler`` [0-0xffff] - specifies the value to be loaded into the
            timer's Prescaler Register (PSC). The timer clock source is divided by
            (``prescaler + 1``) to arrive at the timer clock. Timers 2-7 and 12-14
            have a clock source of 84 MHz (pyb.freq()[2] * 2), and Timers 1, and 8-11
            have a clock source of 168 MHz (pyb.freq()[3] * 2).

          - ``period`` [0-0xffff] for timers 1, 3, 4, and 6-15. [0-0x3fffffff] for timers 2 & 5.
            Specifies the value to be loaded into the timer's AutoReload
            Register (ARR). This determines the period of the timer (i.e. when the
            counter cycles). The timer counter will roll-over after ``period + 1``
            timer clock cycles.

          - ``mode`` can be one of:

            - ``Timer.UP`` - configures the timer to count from 0 to ARR (default)
            - ``Timer.DOWN`` - configures the timer to count from ARR down to 0.
            - ``Timer.CENTER`` - configures the timer to count from 0 to ARR and
              then back down to 0.

          - ``div`` can be one of 1, 2, or 4. Divides the timer clock to determine
            the sampling clock used by the digital filters.

          - ``callback`` - as per Timer.callback()

          - ``deadtime`` - specifies the amount of "dead" or inactive time between
            transitions on complimentary channels (both channels will be inactive)
            for this time). ``deadtime`` may be an integer between 0 and 1008, with
            the following restrictions: 0-128 in steps of 1. 128-256 in steps of
            2, 256-512 in steps of 8, and 512-1008 in steps of 16. ``deadtime``
            measures ticks of ``source_freq`` divided by ``div`` clock ticks.
            ``deadtime`` is only available on timers 1 and 8.

          - ``brk`` - specifies if the break mode is used to kill the output of
            the PWM when the ``BRK_IN`` input is asserted. The value of this
            argument determines if break is enabled and what the polarity is, and
            can be one of ``Timer.BRK_OFF``, ``Timer.BRK_LOW`` or
            ``Timer.BRK_HIGH``. To select the ``BRK_IN`` pin construct a Pin object with
            ``mode=Pin.ALT, alt=Pin.AFn_TIMx``. The pin's GPIO input features are
            available in alt mode - ``pull=`` , ``value()`` and ``irq()``.

         You must either specify freq or both of period and prescaler.
        """
        ...

    def deinit(self) -> None:
        """
        Deinitialises the timer.

        Disables the callback (and the associated irq).

        Disables any channel callbacks (and the associated irq).
        Stops the timer, and disables the timer peripheral.
        """
        ...

    def callback(self, fun) -> None:
        """
        Set the function to be called when the timer triggers.
        ``fun`` is passed 1 argument, the timer object.
        If ``fun`` is ``None`` then the callback will be disabled.
        """
        ...

    def channel(self, channel, mode, pin=None, *args) -> Incomplete:
        """
        If only a channel number is passed, then a previously initialized channel
        object is returned (or ``None`` if there is no previous channel).

        Otherwise, a TimerChannel object is initialized and returned.

        Each channel can be configured to perform pwm, output compare, or
        input capture. All channels share the same underlying timer, which means
        that they share the same timer clock.

        Keyword arguments:

          - ``mode`` can be one of:

            - ``Timer.PWM`` --- configure the timer in PWM mode (active high).
            - ``Timer.PWM_INVERTED`` --- configure the timer in PWM mode (active low).
            - ``Timer.OC_TIMING`` --- indicates that no pin is driven.
            - ``Timer.OC_ACTIVE`` --- the pin will be made active when a compare match occurs (active is determined by polarity)
            - ``Timer.OC_INACTIVE`` --- the pin will be made inactive when a compare match occurs.
            - ``Timer.OC_TOGGLE`` --- the pin will be toggled when an compare match occurs.
            - ``Timer.OC_FORCED_ACTIVE`` --- the pin is forced active (compare match is ignored).
            - ``Timer.OC_FORCED_INACTIVE`` --- the pin is forced inactive (compare match is ignored).
            - ``Timer.IC`` --- configure the timer in Input Capture mode.
            - ``Timer.ENC_A`` --- configure the timer in Encoder mode. The counter only changes when CH1 changes.
            - ``Timer.ENC_B`` --- configure the timer in Encoder mode. The counter only changes when CH2 changes.
            - ``Timer.ENC_AB`` --- configure the timer in Encoder mode. The counter changes when CH1 or CH2 changes.

          - ``callback`` - as per TimerChannel.callback()

          - ``pin`` None (the default) or a Pin object. If specified (and not None)
            this will cause the alternate function of the the indicated pin
            to be configured for this timer channel. An error will be raised if
            the pin doesn't support any alternate functions for this timer channel.

        Keyword arguments for Timer.PWM modes:

          - ``pulse_width`` - determines the initial pulse width value to use.
          - ``pulse_width_percent`` - determines the initial pulse width percentage to use.

        Keyword arguments for Timer.OC modes:

          - ``compare`` - determines the initial value of the compare register.

          - ``polarity`` can be one of:

            - ``Timer.HIGH`` - output is active high
            - ``Timer.LOW`` - output is active low

        Optional keyword arguments for Timer.IC modes:

          - ``polarity`` can be one of:

            - ``Timer.RISING`` - captures on rising edge.
            - ``Timer.FALLING`` - captures on falling edge.
            - ``Timer.BOTH`` - captures on both edges.

          Note that capture only works on the primary channel, and not on the
          complimentary channels.

        Notes for Timer.ENC modes:

          - Requires 2 pins, so one or both pins will need to be configured to use
            the appropriate timer AF using the Pin API.
          - Read the encoder value using the timer.counter() method.
          - Only works on CH1 and CH2 (and not on CH1N or CH2N)
          - The channel number is ignored when setting the encoder mode.

        PWM Example::

            timer = pyb.Timer(2, freq=1000)
            ch2 = timer.channel(2, pyb.Timer.PWM, pin=pyb.Pin.board.X2, pulse_width=8000)
            ch3 = timer.channel(3, pyb.Timer.PWM, pin=pyb.Pin.board.X3, pulse_width=16000)

        PWM Motor Example with complementary outputs, dead time, break input and break callback::

            from pyb import Timer
            from machine import Pin # machine.Pin supports alt mode and irq on the same pin.
            pin_t8_1 = Pin(Pin.board.Y1, mode=Pin.ALT, af=Pin.AF3_TIM8)   # Pin PC6, TIM8_CH1
            pin_t8_1n = Pin(Pin.board.X8, mode=Pin.ALT, af=Pin.AF3_TIM8)  # Pin PA7, TIM8_CH1N
            pin_bkin = Pin(Pin.board.X7, mode=Pin.ALT, af=Pin.AF3_TIM8)   # Pin PA6, TIM8_BKIN
            pin_bkin.irq(handler=break_callabck, trigger=Pin.IRQ_FALLING)
            timer = pyb.Timer(8, freq=1000, deadtime=1008, brk=Timer.BRK_LOW)
            ch1 = timer.channel(1, pyb.Timer.PWM, pulse_width_percent=30)
        """
        ...

    def counter(self, value: Optional[Any] = None) -> Incomplete:
        """
        Get or set the timer counter.
        """
        ...

    def freq(self, value: Optional[Any] = None) -> Incomplete:
        """
        Get or set the frequency for the timer (changes prescaler and period if set).
        """
        ...

    def period(self, value: Optional[Any] = None) -> Incomplete:
        """
        Get or set the period of the timer.
        """
        ...

    def prescaler(self, value: Optional[Any] = None) -> Incomplete:
        """
        Get or set the prescaler for the timer.
        """
        ...

    def source_freq(self) -> Incomplete:
        """
        Get the frequency of the source of the timer.
        """
        ...

class timerchannel:
    """ """

    def callback(self, fun) -> None:
        """
        Set the function to be called when the timer channel triggers.
        ``fun`` is passed 1 argument, the timer object.
        If ``fun`` is ``None`` then the callback will be disabled.
        """
        ...

    def capture(self, value: Optional[Any] = None) -> Incomplete:
        """
        Get or set the capture value associated with a channel.
        capture, compare, and pulse_width are all aliases for the same function.
        capture is the logical name to use when the channel is in input capture mode.
        """
        ...

    def compare(self, value: Optional[Any] = None) -> Incomplete:
        """
        Get or set the compare value associated with a channel.
        capture, compare, and pulse_width are all aliases for the same function.
        compare is the logical name to use when the channel is in output compare mode.
        """
        ...

    def pulse_width(self, value: Optional[Any] = None) -> Incomplete:
        """
        Get or set the pulse width value associated with a channel.
        capture, compare, and pulse_width are all aliases for the same function.
        pulse_width is the logical name to use when the channel is in PWM mode.

        In edge aligned mode, a pulse_width of ``period + 1`` corresponds to a duty cycle of 100%
        In center aligned mode, a pulse width of ``period`` corresponds to a duty cycle of 100%
        """
        ...

    def pulse_width_percent(self, value: Optional[Any] = None) -> Incomplete:
        """
        Get or set the pulse width percentage associated with a channel.  The value
        is a number between 0 and 100 and sets the percentage of the timer period
        for which the pulse is active.  The value can be an integer or
        floating-point number for more accuracy.  For example, a value of 25 gives
        a duty cycle of 25%.
        """
        ...
