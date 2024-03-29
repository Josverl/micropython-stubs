from typing import Any

class CancelledError(Exception): ...

class Event:
    def clear(self, *args) -> Any: ...
    def is_set(self, *args) -> Any: ...
    def set(self, *args) -> Any: ...
    wait: Any

class IOQueue:
    def _dequeue(self, *args) -> Any: ...
    def _enqueue(self, *args) -> Any: ...
    def queue_read(self, *args) -> Any: ...
    def queue_write(self, *args) -> Any: ...
    def remove(self, *args) -> Any: ...
    def wait_io_event(self, *args) -> Any: ...

class Lock:
    acquire: Any
    def locked(self, *args) -> Any: ...
    def release(self, *args) -> Any: ...

class Loop:
    _exc_handler: Any
    def call_exception_handler(self, *args) -> Any: ...
    def close(self, *args) -> Any: ...
    def create_task(self, *args) -> Any: ...
    def default_exception_handler(self, *args) -> Any: ...
    def get_exception_handler(self, *args) -> Any: ...
    def run_forever(self, *args) -> Any: ...
    def run_until_complete(self, *args) -> Any: ...
    def set_exception_handler(self, *args) -> Any: ...
    def stop(self, *args) -> Any: ...

class SingletonGenerator: ...

class StreamReader:
    aclose: Any
    awrite: Any
    awritestr: Any
    def close(self, *args) -> Any: ...
    drain: Any
    def get_extra_info(self, *args) -> Any: ...
    read: Any
    readexactly: Any
    readline: Any
    wait_closed: Any
    def write(self, *args) -> Any: ...

class StreamWriter:
    aclose: Any
    awrite: Any
    awritestr: Any
    def close(self, *args) -> Any: ...
    drain: Any
    def get_extra_info(self, *args) -> Any: ...
    read: Any
    readexactly: Any
    readline: Any
    wait_closed: Any
    def write(self, *args) -> Any: ...

class Task: ...
