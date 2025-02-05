from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from select import poll

# socket.socket
# Create STREAM TCP socket
socket(AF_INET, SOCK_STREAM)
# Create DGRAM UDP socket
socket(AF_INET, SOCK_DGRAM)


# poll: () -> _poll

x = poll()
