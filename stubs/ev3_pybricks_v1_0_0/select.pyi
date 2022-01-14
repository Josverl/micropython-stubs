from typing import Any

EPOLLERR: int
EPOLLET: int
EPOLLHUP: int
EPOLLIN: int
EPOLLONESHOT: int
EPOLLOUT: int
EPOLLPRI: int
EPOLLRDHUP: int
EPOLL_CTL_ADD: int
EPOLL_CTL_DEL: int
EPOLL_CTL_MOD: int

class Epoll:
    def close(self, *argv) -> Any: ...
    def poll(self, *argv) -> Any: ...
    def poll_ms(self, *argv) -> Any: ...
    def register(self, *argv) -> Any: ...
    def unregister(self, *argv) -> Any: ...

POLLERR: int
POLLHUP: int
POLLIN: int
POLLOUT: int
POLLPRI: int

def epoll() -> None: ...

epoll_create: Any
epoll_ctl: Any
epoll_event: str
epoll_wait: Any
errno: Any
ffi: Any
ffilib: Any
libc: Any
math: Any
os: Any

def poll() -> None: ...

struct: Any
utime: Any
