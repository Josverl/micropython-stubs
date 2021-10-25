AF_INET: int
AF_INET6: int
IPPROTO_IP: int
IP_ADD_MEMBERSHIP: int
SOCK_DGRAM: int
SOCK_RAW: int
SOCK_STREAM: int
SOL_SOCKET: int
SO_REUSEADDR: int

def callback() -> None: ...
def getaddrinfo() -> None: ...
def print_pcbs() -> None: ...
def reset() -> None: ...

class socket:
    def accept() -> None: ...
    def bind() -> None: ...
    def close() -> None: ...
    def connect() -> None: ...
    def listen() -> None: ...
    def makefile() -> None: ...
    def read() -> None: ...
    def readinto() -> None: ...
    def readline() -> None: ...
    def recv() -> None: ...
    def recvfrom() -> None: ...
    def send() -> None: ...
    def sendall() -> None: ...
    def sendto() -> None: ...
    def setblocking() -> None: ...
    def setsockopt() -> None: ...
    def settimeout() -> None: ...
    def write() -> None: ...
