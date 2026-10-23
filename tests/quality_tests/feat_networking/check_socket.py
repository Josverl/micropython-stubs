from typing import Union

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

sock = socket(AF_INET, SOCK_STREAM)
packet = bytearray(b"\x30\0\0\0")
assert_type(sock.write(packet), Union[int, None])  # stubs-ignore: version<1.29.0 or linter == "pyrefly"
assert_type(sock.write(packet, 2), Union[int, None])  # stubs-ignore: version<1.29.0 or linter == "pyrefly"
assert_type(sock.write(packet, 1, 2), Union[int, None])  # stubs-ignore: version<1.29.0 or linter == "pyrefly"
