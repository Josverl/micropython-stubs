from typing import Any

stream_awrite: Any

class StreamWriter:
    def get_extra_info(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def close(self, *args, **kwargs) -> Any: ...
    awrite: Any
    readexactly: Any
    awritestr: Any
    drain: Any
    readinto: Any
    read: Any
    aclose: Any
    readline: Any
    wait_closed: Any
    def __init__(self, *argv, **kwargs) -> None: ...

class Stream:
    def get_extra_info(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def close(self, *args, **kwargs) -> Any: ...
    awrite: Any
    readexactly: Any
    awritestr: Any
    drain: Any
    readinto: Any
    read: Any
    aclose: Any
    readline: Any
    wait_closed: Any
    def __init__(self, *argv, **kwargs) -> None: ...

class Server:
    def close(self, *args, **kwargs) -> Any: ...
    wait_closed: Any
    def __init__(self, *argv, **kwargs) -> None: ...

class StreamReader:
    def get_extra_info(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def close(self, *args, **kwargs) -> Any: ...
    awrite: Any
    readexactly: Any
    awritestr: Any
    drain: Any
    readinto: Any
    read: Any
    aclose: Any
    readline: Any
    wait_closed: Any
    def __init__(self, *argv, **kwargs) -> None: ...

open_connection: Any
start_server: Any
