from typing import Any

EINTR: int
POLLIN: int

class Timeout:
    _ONE: Any
    def _run(self, *argv) -> Any: ...
    def cancel(self, *argv) -> Any: ...
    def close(self, *argv) -> Any: ...
    def start(self, *argv) -> Any: ...
    def wait(self, *argv) -> Any: ...

class Timer:
    def elapsed_time(self, *argv) -> Any: ...
    def reset(self, *argv) -> Any: ...
    def wait(self, *argv) -> Any: ...

UINT32: int
UINT64: int
_EFD_CLOEXEC: int
_eventfd: Any
_libc: Any
_thread: Any

def _thread_runner() -> None: ...
def addressof() -> None: ...
def debug_print() -> None: ...
def fork() -> None: ...
def libc() -> None: ...

os: Any

def poll() -> None: ...
def sizeof() -> None: ...

class struct: ...

sys: Any
time: Any

def write_at_index() -> None: ...
