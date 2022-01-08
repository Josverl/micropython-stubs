from typing import Any

class CardKB:
    def _available() -> None: ...
    def _monitor() -> None: ...
    def deinit() -> None: ...
    def isNewKeyPress() -> None: ...
    keyData: Any
    keyString: Any

i2c_bus: Any
machine: Any
timEx: Any
unit: Any
