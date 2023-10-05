from typing import Any

class Stream:
    def __init__(self, *args) -> None: ...
    def close(self, *args) -> Any: ...
    read: Any
    readinto: Any
    readline: Any
    def write(self, *args) -> Any: ...
    wait_closed: Any
    aclose: Any
    awrite: Any
    awritestr: Any
    def get_extra_info(self, *args) -> Any: ...
    readexactly: Any
    drain: Any

class StreamReader:
    def __init__(self, *args) -> None: ...
    def close(self, *args) -> Any: ...
    read: Any
    readinto: Any
    readline: Any
    def write(self, *args) -> Any: ...
    wait_closed: Any
    aclose: Any
    awrite: Any
    awritestr: Any
    def get_extra_info(self, *args) -> Any: ...
    readexactly: Any
    drain: Any

class StreamWriter:
    def __init__(self, *args) -> None: ...
    def close(self, *args) -> Any: ...
    read: Any
    readinto: Any
    readline: Any
    def write(self, *args) -> Any: ...
    wait_closed: Any
    aclose: Any
    awrite: Any
    awritestr: Any
    def get_extra_info(self, *args) -> Any: ...
    readexactly: Any
    drain: Any

open_connection: Any

class Server:
    def close(self, *args) -> Any: ...
    wait_closed: Any

start_server: Any
stream_awrite: Any
