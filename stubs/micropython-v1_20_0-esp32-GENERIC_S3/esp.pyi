from typing import Any

LOG_NONE: int
LOG_WARNING: int
LOG_VERBOSE: int
LOG_DEBUG: int
LOG_INFO: int
LOG_ERROR: int

def osdebug(*args, **kwargs) -> Any: ...
def flash_write(*args, **kwargs) -> Any: ...
def gpio_matrix_in(*args, **kwargs) -> Any: ...
def gpio_matrix_out(*args, **kwargs) -> Any: ...
def flash_user_start(*args, **kwargs) -> Any: ...
def flash_erase(*args, **kwargs) -> Any: ...
def flash_read(*args, **kwargs) -> Any: ...
def flash_size(*args, **kwargs) -> Any: ...
