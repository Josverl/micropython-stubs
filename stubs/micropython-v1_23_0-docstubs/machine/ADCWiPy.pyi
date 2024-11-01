""" """

from __future__ import annotations
from _typeshed import Incomplete

class ADCWiPy:
    """
    Create an ADC object associated with the given pin.
    This allows you to then read analog values on that pin.
    For more info check the `pinout and alternate functions
    table. <https://raw.githubusercontent.com/wipy/wipy/master/docs/PinOUT.png>`_
    """

    def __init__(self, id=0, *, bits=12) -> None: ...
    def channel(self, id, *, pin) -> Incomplete:
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

    def adcchannel(self) -> Incomplete:
        """
        Fast method to read the channel value.
        """
        ...

class adcchannel:
    """ """

    def value(self) -> Incomplete:
        """
        Read the channel value.
        """
        ...

    def init(self) -> Incomplete:
        """
        Re-init (and effectively enable) the ADC channel.
        """
        ...

    def deinit(self) -> None:
        """
        Disable the ADC channel.
        """
        ...
