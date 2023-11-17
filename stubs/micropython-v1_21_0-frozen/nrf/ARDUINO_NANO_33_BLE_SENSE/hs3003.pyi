from _typeshed import Incomplete

class HS3003:
    bus: Incomplete
    address: Incomplete
    def __init__(self, bus, address: int = ...) -> None: ...
    def _read_data(self): ...
    def humidity(self):
        """Returns the relative humidity in percent."""
    def temperature(self):
        """Returns the temperature in degrees Celsius."""
