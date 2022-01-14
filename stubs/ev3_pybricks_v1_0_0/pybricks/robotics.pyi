from typing import Any

class DriveBase:
    def drive(self, *argv) -> Any: ...
    def drive_time(self, *argv) -> Any: ...
    def stop(self, *argv) -> Any: ...

class Stop:
    BRAKE: int
    COAST: int
    HOLD: int

pi: float

def wait() -> None: ...
