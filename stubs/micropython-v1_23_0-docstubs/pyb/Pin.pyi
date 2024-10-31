""" """

from __future__ import annotations
from typing import Any, List, Optional
from _typeshed import Incomplete

class Pin:
    """
    Create a new Pin object associated with the id.  If additional arguments are given,
    they are used to initialise the pin.  See :meth:`pin.init`.
    """

    ALT: Incomplete
    """initialise the pin to alternate-function mode for input or output"""
    AF_OD: Incomplete
    """initialise the pin to alternate-function mode with an open-drain drive"""
    AF_PP: Incomplete
    """initialise the pin to alternate-function mode with a push-pull drive"""
    ANALOG: Incomplete
    """initialise the pin to analog mode"""
    IN: Incomplete
    """initialise the pin to input mode"""
    OUT_OD: Incomplete
    """initialise the pin to output mode with an open-drain drive"""
    OUT_PP: Incomplete
    """initialise the pin to output mode with a push-pull drive"""
    PULL_DOWN: Incomplete
    """enable the pull-down resistor on the pin"""
    PULL_NONE: Incomplete
    """don't enable any pull up or down resistors on the pin"""
    PULL_UP: Incomplete
    """enable the pull-up resistor on the pin"""
    def __init__(self, id, *args, **kwargs) -> None: ...
    @classmethod
    def debug(cls, state: Optional[Any] = None) -> bool:
        """
        Get or set the debugging state (``True`` or ``False`` for on or off).
        """
        ...

    @classmethod
    def dict(cls, dict: Optional[Any] = None) -> Incomplete:
        """
        Get or set the pin mapper dictionary.
        """
        ...

    @classmethod
    def mapper(cls, fun: Optional[Any] = None) -> Incomplete:
        """
        Get or set the pin mapper function.
        """
        ...

    def init(self, mode, pull=PULL_NONE, *, value=None, alt=-1) -> None:
        """
        Initialise the pin:

          - *mode* can be one of:

             - ``Pin.IN`` - configure the pin for input;
             - ``Pin.OUT_PP`` - configure the pin for output, with push-pull control;
             - ``Pin.OUT_OD`` - configure the pin for output, with open-drain control;
             - ``Pin.ALT`` - configure the pin for alternate function, input or output;
             - ``Pin.AF_PP`` - configure the pin for alternate function, push-pull;
             - ``Pin.AF_OD`` - configure the pin for alternate function, open-drain;
             - ``Pin.ANALOG`` - configure the pin for analog.

          - *pull* can be one of:

             - ``Pin.PULL_NONE`` - no pull up or down resistors;
             - ``Pin.PULL_UP`` - enable the pull-up resistor;
             - ``Pin.PULL_DOWN`` - enable the pull-down resistor.

            When a pin has the ``Pin.PULL_UP`` or ``Pin.PULL_DOWN`` pull-mode enabled,
            that pin has an effective 40k Ohm resistor pulling it to 3V3 or GND
            respectively (except pin Y5 which has 11k Ohm resistors).

          - *value* if not None will set the port output value before enabling the pin.

          - *alt* can be used when mode is ``Pin.ALT`` , ``Pin.AF_PP`` or ``Pin.AF_OD`` to
            set the index or name of one of the alternate functions associated with a pin.
            This arg was previously called *af* which can still be used if needed.

        Returns: ``None``.
        """
        ...

    def value(self, value: Optional[Any] = None) -> int:
        """
        Get or set the digital logic level of the pin:

          - With no argument, return 0 or 1 depending on the logic level of the pin.
          - With ``value`` given, set the logic level of the pin.  ``value`` can be
            anything that converts to a boolean.  If it converts to ``True``, the pin
            is set high, otherwise it is set low.
        """
        ...

    def __str__(self) -> str:
        """
        Return a string describing the pin object.
        """
        ...

    def af(self) -> Incomplete:
        """
        Returns the currently configured alternate-function of the pin. The
        integer returned will match one of the allowed constants for the af
        argument to the init function.
        """
        ...

    def af_list(self) -> List:
        """
        Returns an array of alternate functions available for this pin.
        """
        ...

    def gpio(self) -> int:
        """
        Returns the base address of the GPIO block associated with this pin.
        """
        ...

    def mode(self) -> Incomplete:
        """
        Returns the currently configured mode of the pin. The integer returned
        will match one of the allowed constants for the mode argument to the init
        function.
        """
        ...

    def name(self) -> str:
        """
        Get the pin name.
        """
        ...

    def names(self) -> str:
        """
        Returns the cpu and board names for this pin.
        """
        ...

    def pin(self) -> int:
        """
        Get the pin number.
        """
        ...

    def port(self) -> Incomplete:
        """
        Get the pin port.
        """
        ...

    def pull(self) -> Incomplete:
        """
        Returns the currently configured pull of the pin. The integer returned
        will match one of the allowed constants for the pull argument to the init
        function.
        """
        ...

class pinaf:
    """ """

    def __str__(self) -> str:
        """
        Return a string describing the alternate function.
        """
        ...

    def index(self) -> int:
        """
        Return the alternate function index.
        """
        ...

    def name(self) -> str:
        """
        Return the name of the alternate function.
        """
        ...

    def reg(self) -> Incomplete:
        """
        Return the base register associated with the peripheral assigned to this
        alternate function. For example, if the alternate function were TIM2_CH3
        this would return stm.TIM2
        """
        ...
