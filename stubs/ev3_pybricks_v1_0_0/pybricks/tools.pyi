from typing import Any

class StopWatch:
    def pause(self, *argv) -> Any: ...
    def reset(self, *argv) -> Any: ...
    def resume(self, *argv) -> Any: ...
    def time(self, *argv) -> Any: ...

def builtinprint() -> None: ...
def print() -> None: ...

stderr: Any

def wait() -> None: ...
