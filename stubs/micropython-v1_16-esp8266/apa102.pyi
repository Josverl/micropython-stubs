from typing import Any

def apa102_write(*args, **kwargs) -> Any: ...

class NeoPixel:
    def __init__(self, *argv, **kwargs) -> None: ...
    def write(self, *args, **kwargs) -> Any: ...
    def fill(self, *args, **kwargs) -> Any: ...
    ORDER: tuple

class APA102:
    def __init__(self, *argv, **kwargs) -> None: ...
    def write(self, *args, **kwargs) -> Any: ...
    def fill(self, *args, **kwargs) -> Any: ...
    ORDER: tuple
