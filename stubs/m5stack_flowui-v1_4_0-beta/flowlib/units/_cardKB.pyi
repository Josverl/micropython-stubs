from typing import Any

class CardKB:
    def _available(self, *argv) -> Any: ...
    def _monitor(self, *argv) -> Any: ...
    def deinit(self, *argv) -> Any: ...
    def isNewKeyPress(self, *argv) -> Any: ...
    keyData: Any
    keyString: Any

i2c_bus: Any
machine: Any
timEx: Any
unit: Any
