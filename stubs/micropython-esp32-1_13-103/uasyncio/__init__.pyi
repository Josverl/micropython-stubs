from typing import Any

class CancelledError: ...

class Event:
    def clear() -> None: ...
    def is_set() -> None: ...
    def set() -> None: ...
    wait: Any

class IOQueue:
    def _dequeue() -> None: ...
    def _enqueue() -> None: ...
    def queue_read() -> None: ...
    def queue_write() -> None: ...
    def remove() -> None: ...
    def wait_io_event() -> None: ...

class Lock:
    acquire: Any
    def locked() -> None: ...
    def release() -> None: ...

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

class StreamReader:
    aclose: Any
    awrite: Any
    awritestr: Any
    def close() -> None: ...
    drain: Any
    def get_extra_info() -> None: ...
    read: Any
    readexactly: Any
    readline: Any
    wait_closed: Any
    def write() -> None: ...

class StreamWriter:
    aclose: Any
    awrite: Any
    awritestr: Any
    def close() -> None: ...
    drain: Any
    def get_extra_info() -> None: ...
    read: Any
    readexactly: Any
    readline: Any
    wait_closed: Any
    def write() -> None: ...

class Task: ...

class TaskQueue:
    def peek() -> None: ...
    def pop_head() -> None: ...
    def push_head() -> None: ...
    def push_sorted() -> None: ...
    def remove() -> None: ...

class TimeoutError: ...

_attrs: Any

def create_task() -> None: ...

gather: Any

def get_event_loop() -> None: ...
def new_event_loop() -> None: ...

open_connection: Any

def run() -> None: ...
def run_until_complete() -> None: ...

select: Any

def sleep() -> None: ...
def sleep_ms() -> None: ...

start_server: Any
sys: Any

def ticks() -> None: ...
def ticks_add() -> None: ...
def ticks_diff() -> None: ...

wait_for: Any

def wait_for_ms() -> None: ...
