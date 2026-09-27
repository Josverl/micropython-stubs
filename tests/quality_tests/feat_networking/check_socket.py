from typing_extensions import assert_type

from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from select import poll

# socket.socket
# Create STREAM TCP socket
socket(AF_INET, SOCK_STREAM)
# Create DGRAM UDP socket
socket(AF_INET, SOCK_DGRAM)


# poll: () -> _poll

x = poll()


received, address = socket(AF_INET, SOCK_DGRAM).recvfrom(1024)
# recvfrom was typed as a bare Tuple until the v1.29.0 stubs were generated
assert_type(received, bytes)  # stubs-ignore: version<1.29.0
