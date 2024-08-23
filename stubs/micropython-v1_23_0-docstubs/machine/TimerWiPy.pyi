""" """

from __future__ import annotations
from typing import Any, Callable, Optional
from _typeshed import Incomplete

class TimerWiPy:
    """
    Construct a new timer object of the given id. Id of -1 constructs a
    virtual timer (if supported by a board).
    """

    ONE_SHOT: Incomplete
    PERIODIC: Incomplete
    """Timer operating mode."""
    def __init__(self, id, *args, **kwargs) -> None: ...
    def init(self, mode, *, width=16) -> None:
        """
        Initialise the timer. Example::

            tim.init(Timer.PERIODIC)             # periodic 16-bit timer
            tim.init(Timer.ONE_SHOT, width=32)   # one shot 32-bit timer

        Keyword arguments:

          - ``mode`` can be one of:

            - ``TimerWiPy.ONE_SHOT`` - The timer runs once until the configured
              period of the channel expires.
            - ``TimerWiPy.PERIODIC`` - The timer runs periodically at the configured
              frequency of the channel.
            - ``TimerWiPy.PWM``      - Output a PWM signal on a pin.

          - ``width`` must be either 16 or 32 (bits). For really low frequencies < 5Hz
            (or large periods), 32-bit timers should be used. 32-bit mode is only available
            for ``ONE_SHOT`` AND ``PERIODIC`` modes.
        """
        ...

    def deinit(self) -> None:
        """
        Deinitialises the timer. Stops the timer, and disables the timer peripheral.
        """
        ...

    def channel(self, channel, *, freq, period, polarity=POSITIVE, duty_cycle=0) -> Incomplete:
        """
        If only a channel identifier passed, then a previously initialized channel
        object is returned (or ``None`` if there is no previous channel).

        Otherwise, a TimerChannel object is initialized and returned.

        The operating mode is is the one configured to the Timer object that was used to
        create the channel.

        - ``channel`` if the width of the timer is 16-bit, then must be either ``TIMER.A``, ``TIMER.B``.
          If the width is 32-bit then it **must be** ``TIMER.A | TIMER.B``.

        Keyword only arguments:

          - ``freq`` sets the frequency in Hz.
          - ``period`` sets the period in microseconds.

          .. note::

             Either ``freq`` or ``period`` must be given, never both.

          - ``polarity`` this is applicable for ``PWM``, and defines the polarity of the duty cycle
          - ``duty_cycle`` only applicable to ``PWM``. It's a percentage (0.00-100.00). Since the WiPy
            doesn't support floating point numbers the duty cycle must be specified in the range 0-10000,
            where 10000 would represent 100.00, 5050 represents 50.50, and so on.

        .. note::

           When the channel is in PWM mode, the corresponding pin is assigned automatically, therefore
           there's no need to assign the alternate function of the pin via the ``Pin`` class. The pins which
           support PWM functionality are the following:

           - ``GP24`` on Timer 0 channel A.
           - ``GP25`` on Timer 1 channel A.
           - ``GP9``  on Timer 2 channel B.
           - ``GP10`` on Timer 3 channel A.
           - ``GP11`` on Timer 3 channel B.
        """
        ...

class timerchannel:
    """ """

    def irq(self, *, trigger, priority=1, handler=None) -> Callable[..., Incomplete]:
        """
        The behaviour of this callback is heavily dependent on the operating
        mode of the timer channel:

            - If mode is ``TimerWiPy.PERIODIC`` the callback is executed periodically
              with the configured frequency or period.
            - If mode is ``TimerWiPy.ONE_SHOT`` the callback is executed once when
              the configured timer expires.
            - If mode is ``TimerWiPy.PWM`` the callback is executed when reaching the duty
              cycle value.

        The accepted params are:

            - ``priority`` level of the interrupt. Can take values in the range 1-7.
              Higher values represent higher priorities.
            - ``handler`` is an optional function to be called when the interrupt is triggered.
            - ``trigger`` must be ``TimerWiPy.TIMEOUT`` when the operating mode is either ``TimerWiPy.PERIODIC`` or
              ``TimerWiPy.ONE_SHOT``. In the case that mode is ``TimerWiPy.PWM`` then trigger must be equal to
              ``TimerWiPy.MATCH``.

        Returns a callback object.
        """
        ...

    def freq(self, value: Optional[Any] = None) -> Incomplete:
        """
        Get or set the timer channel frequency (in Hz).
        """
        ...

    def period(self, value: Optional[Any] = None) -> Incomplete:
        """
        Get or set the timer channel period (in microseconds).
        """
        ...

    def duty_cycle(self, value: Optional[Any] = None) -> Incomplete:
        """
        Get or set the duty cycle of the PWM signal. It's a percentage (0.00-100.00). Since the WiPy
        doesn't support floating point numbers the duty cycle must be specified in the range 0-10000,
        where 10000 would represent 100.00, 5050 represents 50.50, and so on.
        """
        ...
