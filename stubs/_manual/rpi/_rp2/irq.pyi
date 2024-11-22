"""
Functionality specific to the RP2.

MicroPython module: https://docs.micropython.org/en/latest/library/rp2.html

The ``rp2`` module contains references to an IRQ class that is not documented,
also the different ports have different IRQ classes, therefore this is implemented 
as a port specific class.
"""

class _IRQ_RP2:
    """
    IRQ definition for RP2
    """

    def flags(self) -> int:
        """
        Get IRQ flags
        """

    def trigger(self) -> int:
        """
        Trigger the IRQ
        """
