from typing import Any

AF_INET: int
AF_INET6: int
IPPROTO_IP: int
IP_ADD_MEMBERSHIP: int
SOCK_DGRAM: int
SOCK_RAW: int
SOCK_STREAM: int
SOL_SOCKET: int
SO_REUSEADDR: int

def callback(*args) -> Any: ...
def getaddrinfo(*args) -> Any: ...
def print_pcbs(*args) -> Any: ...
def reset(*args) -> Any: ...

class socket:
    def accept(self, *args) -> Any: ...
    def bind(self, *args) -> Any: ...
    def close(self, *args) -> Any: ...
    def connect(self, *args) -> Any: ...
