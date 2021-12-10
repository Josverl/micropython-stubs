from typing import Any, Tuple

mem8: Any
mem16: Any
mem32: int
GPIOA: int
GPIOB: int
GPIO_BSRR: Any
GPIO_IDR: Any
GPIO_ODR: int

def rfcore_status() -> int: ...
def rfcore_fw_version(id) -> Tuple: ...
def rfcore_sys_hci(ogf, ocf, data, timeout_ms: int = ...) -> bytes: ...
