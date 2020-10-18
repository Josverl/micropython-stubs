"""
Module: 'socket' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2
AF_INET = 2
AF_INET6 = 10
AF_UNIX = 1
INADDR_ANY = 0
IPPROTO_IP = 0
IP_ADD_MEMBERSHIP = 35
IP_DROP_MEMBERSHIP = 36
MSG_DONTROUTE = 4
MSG_DONTWAIT = 64
SOCK_DGRAM = 2
SOCK_RAW = 3
SOCK_STREAM = 1
SOL_SOCKET = 1
SO_BROADCAST = 6
SO_ERROR = 4
SO_KEEPALIVE = 9
SO_LINGER = 13
SO_REUSEADDR = 2
_GLOBAL_DEFAULT_TIMEOUT = 30
def _resolve_addr():
    pass

_socket = None
def create_connection():
    pass


class error:
    ''
def getaddrinfo():
    pass

def inet_aton():
    pass

def inet_ntop():
    pass

def inet_pton():
    pass

def sockaddr():
    pass


class socket:
    ''
    accept = None
    bind = None
    def close():
        pass

    connect = None
    def fileno():
        pass

    def listen():
        pass

    def makefile():
        pass

    def read():
        pass

    def readinto():
        pass

    def readline():
        pass

    def recv():
        pass

    def recvfrom():
        pass

    def send():
        pass

    def sendall():
        pass

    sendto = None
    def setblocking():
        pass

    def setsockopt():
        pass

    def write():
        pass

