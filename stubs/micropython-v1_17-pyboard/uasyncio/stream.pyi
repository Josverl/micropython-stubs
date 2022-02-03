from typing import Any

class Stream:
    def __init__(self, *argv, **kwargs) -> None: ...
    def close(self, *args, **kwargs) -> Any: ...
    read: Any
    readinto: Any
    readline: Any
    def write(self, *args, **kwargs) -> Any: ...
    wait_closed: Any
    aclose: Any
    awrite: Any
    awritestr: Any
    def get_extra_info(self, *args, **kwargs) -> Any: ...
    readexactly: Any
    drain: Any

class StreamReader:
    def __init__(self, *argv, **kwargs) -> None: ...
    def close(self, *args, **kwargs) -> Any: ...
    read: Any
    readinto: Any
    readline: Any
    def write(self, *args, **kwargs) -> Any: ...
    wait_closed: Any
    aclose: Any
    awrite: Any
    awritestr: Any
    def get_extra_info(self, *args, **kwargs) -> Any: ...
    readexactly: Any
    drain: Any

class StreamWriter:
    def __init__(self, *argv, **kwargs) -> None: ...
    def close(self, *args, **kwargs) -> Any: ...
    read: Any
    readinto: Any
    readline: Any
    def write(self, *args, **kwargs) -> Any: ...
    wait_closed: Any
    aclose: Any
    awrite: Any
    awritestr: Any
    def get_extra_info(self, *args, **kwargs) -> Any: ...
    readexactly: Any
    drain: Any

open_connection: Any

class Server:
    def __init__(self, *argv, **kwargs) -> None: ...
    def close(self, *args, **kwargs) -> Any: ...
    wait_closed: Any

start_server: Any
stream_awrite: Any
