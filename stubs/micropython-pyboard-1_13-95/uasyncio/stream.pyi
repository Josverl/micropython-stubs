from typing import Any

class Server:
    _serve: Any
    def close() -> None: ...
    wait_closed: Any

class Stream:
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

core: Any
open_connection: Any
start_server: Any
stream_awrite: Any
