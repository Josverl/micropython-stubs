from _typeshed import Incomplete as Incomplete

stream_awrite: Incomplete
open_connection: Incomplete
start_server: Incomplete

class StreamWriter:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    awritestr: Incomplete
    wait_closed: Incomplete
    drain: Incomplete
    readexactly: Incomplete
    readinto: Incomplete
    read: Incomplete
    awrite: Incomplete
    readline: Incomplete
    aclose: Incomplete
    def __init__(self, *argv, **kwargs) -> None: ...

class Server:
    def close(self, *args, **kwargs) -> Incomplete: ...
    wait_closed: Incomplete
    def __init__(self, *argv, **kwargs) -> None: ...

class Stream:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    awritestr: Incomplete
    wait_closed: Incomplete
    drain: Incomplete
    readexactly: Incomplete
    readinto: Incomplete
    read: Incomplete
    awrite: Incomplete
    readline: Incomplete
    aclose: Incomplete
    def __init__(self, *argv, **kwargs) -> None: ...

class StreamReader:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    awritestr: Incomplete
    wait_closed: Incomplete
    drain: Incomplete
    readexactly: Incomplete
    readinto: Incomplete
    read: Incomplete
    awrite: Incomplete
    readline: Incomplete
    aclose: Incomplete
    def __init__(self, *argv, **kwargs) -> None: ...
