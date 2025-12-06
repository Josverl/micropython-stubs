from _typeshed import Incomplete
from machine import I2C as I2C

class MAX17048:
    _MAX17048_ADDRESS: int
    _VCELL_REGISTER: int
    _SOC_REGISTER: int
    _MODE_REGISTER: int
    _VERSION_REGISTER: int
    _HIBRT_REGISTER: int
    _CONFIG_REGISTER: int
    _COMMAND_REGISTER: int
    i2c: Incomplete
    address: Incomplete
    def __init__(self, i2c, address=...) -> None: ...
    def _read_register(self, register, num_bytes): ...
    def _write_register(self, register, value, num_bytes) -> None: ...
    @property
    def cell_voltage(self):
        """The voltage of the connected cell in Volts."""
    @property
    def state_of_charge(self):
        """The state of charge of the battery in percentage."""
    @property
    def version(self):
        """The chip version."""
    @property
    def hibernate(self):
        """True if the chip is in hibernate mode, False otherwise."""
    @hibernate.setter
    def hibernate(self, value) -> None: ...
    def quick_start(self) -> None:
        """Perform a quick start to reset the SOC calculation in the chip."""
    def reset(self) -> None:
        """Reset the chip."""
