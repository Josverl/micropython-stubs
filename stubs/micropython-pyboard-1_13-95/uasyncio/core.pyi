from typing import Any

class CancelledError: ...

class IOQueue:
    def _dequeue() -> None: ...
    def _enqueue() -> None: ...
    def queue_read() -> None: ...
    def queue_write() -> None: ...
    def remove() -> None: ...
    def wait_io_event() -> None: ...

class Loop:
    _exc_handler: Any
    def call_exception_handler() -> None: ...
    def close() -> None: ...
    def create_task() -> None: ...
    def default_exception_handler() -> None: ...
    def get_exception_handler() -> None: ...
    def run_forever() -> None: ...
    def run_until_complete() -> None: ...
    def set_exception_handler() -> None: ...
    def stop() -> None: ...

class SingletonGenerator: ...
class Task: ...
