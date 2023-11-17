from socket import *  # type:  ignore

# socket.socket
# Create STREAM TCP socket
socket(AF_INET, SOCK_STREAM)
# Create DGRAM UDP socket
socket(AF_INET, SOCK_DGRAM)


# poll: () -> _poll
from select import poll

x = poll()
