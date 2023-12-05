"""
Functions related to the hardware.

MicroPython module: https://docs.micropython.org/en/v1.21.0/library/machine.html

The ``machine`` module contains specific functions related to the hardware
on a particular board. Most functions in this module allow to achieve direct
and unrestricted access to and control of hardware blocks on a system
(like CPU, timers, buses, etc.). Used incorrectly, this can lead to
malfunction, lockups, crashes of your board, and in extreme cases, hardware
damage.
"""
from _typeshed import Incomplete, Incomplete as Incomplete
from typing import Any, Callable, List, NoReturn, Optional, Tuple, Union

def time_pulse_us(pin, pulse_level, timeout_us=1000000, /) -> int:
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

def idle() -> Incomplete:
    """
    Gates the clock to the CPU, useful to reduce power consumption at any time during
    short or long periods. Peripherals continue working and execution resumes as soon
    as any interrupt is triggered (on many ports this includes system timer
    interrupt occurring at regular intervals on the order of millisecond).
    """
    ...

mem32: Incomplete
mem8: Incomplete

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
    def __init__(self, pin_obj, *args, invert=False) -> None: ...

mem16: Incomplete

class PinBase:
    def __init__(self, *argv, **kwargs) -> None: ...
