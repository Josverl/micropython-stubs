""" """

from __future__ import annotations

from typing import overload

class ADCWiPy:
    """
    Create an ADC object associated with the given pin.
    This allows you to then read analog values on that pin.
    For more info check the `pinout and alternate functions
    table. <https://raw.githubusercontent.com/wipy/wipy/master/docs/PinOUT.png>`_
    """

    def __init__(self, id=0, *, bits=12) -> None: ...
    @overload
    def channel(self, id: int, *, pin=None) -> adcchannel: ...
    @overload
    def channel(self, *, pin) -> adcchannel: ...
    @overload
    def channel(self, id: int, *, pin) -> adcchannel:
        """
        Create an analog pin. If only channel ID is given, the correct pin will
        be selected. Alternatively, only the pin can be passed and the correct
        channel will be selected. Examples::

           # all of these are equivalent and enable ADC channel 1 on GP3
           apin = adc.channel(1)
           apin = adc.channel(pin='GP3')
           apin = adc.channel(id=1, pin='GP3')
        """
        ...

    def init(self) -> None:
        """
        Enable the ADC block.
        """
        ...

    def deinit(self) -> None:
        """
        Disable the ADC block.
        """
        ...

class adcchannel:
    """ """

    def __call__(self) -> int:
        """
        Fast method to read the channel value.
        """
        ...

    def value(self) -> int:
        """
        Read the channel value.
        """
        ...

    def init(self) -> None:
        """
        Re-init (and effectively enable) the ADC channel.
        """
        ...

    def deinit(self) -> None:
        """
        Disable the ADC channel.
        """
        ...
