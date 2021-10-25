class CancelledError: ...

DEBUG: int

class EventLoop:
    def call_at_() -> None: ...
    def call_later() -> None: ...
    def call_later_ms() -> None: ...
    def call_soon() -> None: ...
    def close() -> None: ...
    def create_task() -> None: ...
    def run_forever() -> None: ...
    def run_until_complete() -> None: ...
    def stop() -> None: ...
    def time() -> None: ...
    def wait() -> None: ...

class IORead:
    def handle() -> None: ...

class IOReadDone:
    def handle() -> None: ...

class IOWrite:
    def handle() -> None: ...

class IOWriteDone:
    def handle() -> None: ...

class PollEventLoop: ...
