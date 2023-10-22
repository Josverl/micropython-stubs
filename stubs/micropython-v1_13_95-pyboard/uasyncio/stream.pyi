from typing import Any

class Server:
    _serve: Any
    def close(self, *args) -> Any: ...
    wait_closed: Any

class Stream:
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

core: Any
open_connection: Any
start_server: Any
stream_awrite: Any
