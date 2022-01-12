from typing import Any

class StepMotor:
    def _available() -> None: ...
    def deinit() -> None: ...
    def g_code() -> None: ...
    def get_code_time() -> None: ...
    def grbl_init() -> None: ...
    def lock_motor() -> None: ...
    def read_clean() -> None: ...
    def read_idle() -> None: ...
    def read_line() -> None: ...
    def set_mode() -> None: ...
    def turn() -> None: ...
    def unlock_motor() -> None: ...
    def wait_idle() -> None: ...

i2c_bus: Any
math: Any
module: Any
re: Any

def sleep_ms() -> None: ...