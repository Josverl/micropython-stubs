""" """

from __future__ import annotations

from typing import Any, Callable, Dict, List, overload

from _typeshed import Incomplete

class Pin:
    """
    A pin is the basic object to control I/O pins.  It has methods to set
    the mode of the pin (input, output, etc) and methods to get and set the
    digital logic level. For analog control of a pin, see the ADC class.

    Usage Model:

    All Board Pins are predefined as pyb.Pin.board.Name::

        x1_pin = pyb.Pin.board.X1

        g = pyb.Pin(pyb.Pin.board.X1, pyb.Pin.IN)

    CPU pins which correspond to the board pins are available
    as ``pyb.Pin.cpu.Name``. For the CPU pins, the names are the port letter
    followed by the pin number. On the PYBv1.0, ``pyb.Pin.board.X1`` and
    ``pyb.Pin.cpu.A0`` are the same pin.

    You can also use strings::

        g = pyb.Pin('X1', pyb.Pin.OUT_PP)

    Users can add their own names::

        MyMapperDict = { 'LeftMotorDir' : pyb.Pin.cpu.C12 }
        pyb.Pin.dict(MyMapperDict)
        g = pyb.Pin("LeftMotorDir", pyb.Pin.OUT_OD)

    and can query mappings::

        pin = pyb.Pin("LeftMotorDir")

    Users can also add their own mapping function::

        def MyMapper(pin_name):
           if pin_name == "LeftMotorDir":
               return pyb.Pin.cpu.A0

        pyb.Pin.mapper(MyMapper)

    So, if you were to call: ``pyb.Pin("LeftMotorDir", pyb.Pin.OUT_PP)``
    then ``"LeftMotorDir"`` is passed directly to the mapper function.

    To summarise, the following order determines how things get mapped into
    an ordinal pin number:

    1. Directly specify a pin object
    2. User supplied mapping function
    3. User supplied mapping (object must be usable as a dictionary key)
    4. Supply a string which matches a board pin
    5. Supply a string which matches a CPU port/pin

    You can set ``pyb.Pin.debug(True)`` to get some debug information about
    how a particular object gets mapped to a pin.

    When a pin has the ``Pin.PULL_UP`` or ``Pin.PULL_DOWN`` pull-mode enabled,
    that pin has an effective 40k Ohm resistor pulling it to 3V3 or GND
    respectively (except pin Y5 which has 11k Ohm resistors).

    Now every time a falling edge is seen on the gpio pin, the callback will be
    executed. Caution: mechanical push buttons have "bounce" and pushing or
    releasing a switch will often generate multiple edges.
    See: http://www.eng.utah.edu/~cs5780/debouncing.pdf for a detailed
    explanation, along with various techniques for debouncing.

    All pin objects go through the pin mapper to come up with one of the
    gpio pins.
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
    def __init__(
        self,
        id: Pin | str | int,
        /,
        mode: int = IN,
        pull: int = PULL_NONE,
        *,
        value: Any = None,
        alt: str | int = -1,
    ) -> None:
        """
        Create a new Pin object associated with the id.  If additional arguments are given,
        they are used to initialise the pin.  See :meth:`pin.init`.
        """

    @overload
    @staticmethod
    def debug() -> bool:
        """
        Get or set the debugging state (``True`` or ``False`` for on or off).
        """

    @overload
    @staticmethod
    def debug(state: bool, /) -> None:
        """
        Get or set the debugging state (``True`` or ``False`` for on or off).
        """

    @overload
    @staticmethod
    def dict() -> Dict[str, Pin]:
        """
        Get or set the pin mapper dictionary.
        """

    @overload
    @staticmethod
    def dict(dict: Dict[str, Pin], /) -> None:
        """
        Get or set the pin mapper dictionary.
        """

    @overload
    @staticmethod
    def mapper() -> Callable[[str], Pin]:
        """
        Get or set the pin mapper function.
        """

    @overload
    @staticmethod
    def mapper(fun: Callable[[str], Pin], /) -> None:
        """
        Get or set the pin mapper function.
        """

    def init(
        self,
        mode: int = IN,
        pull: int = PULL_NONE,
        *,
        value: Any = None,
        alt: str | int = -1,
    ) -> None:
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

    @overload
    def value(self) -> int:
        """
        Get or set the digital logic level of the pin:

          - With no argument, return 0 or 1 depending on the logic level of the pin.
          - With ``value`` given, set the logic level of the pin.  ``value`` can be
            anything that converts to a boolean.  If it converts to ``True``, the pin
            is set high, otherwise it is set low.
        """

    @overload
    def value(self, value: Any, /) -> None:
        """
        Get or set the digital logic level of the pin:

          - With no argument, return 0 or 1 depending on the logic level of the pin.
          - With ``value`` given, set the logic level of the pin.  ``value`` can be
            anything that converts to a boolean.  If it converts to ``True``, the pin
            is set high, otherwise it is set low.
        """

    def __str__(self) -> str:
        """
        Return a string describing the pin object.
        """
        ...

    def af(self) -> int:
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

    def mode(self) -> int:
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

    def port(self) -> int:
        """
        Get the pin port.
        """
        ...

    def pull(self) -> int:
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
