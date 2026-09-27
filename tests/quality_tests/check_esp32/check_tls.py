"""
Sample from https://github.com/Josverl/micropython-stubs/issues/928

`tls.SSLContext.verify_mode` is a writable int attribute implemented by the
C level attribute handler, so it is not visible to createstubs.
"""

import socket

import tls

ssl_ctx = tls.SSLContext(tls.PROTOCOL_TLS_CLIENT)
ssl_ctx.verify_mode = tls.CERT_NONE  # stubs-ignore: version<1.29.0
print(ssl_ctx.verify_mode)  # stubs-ignore: version<1.29.0

sock = socket.socket()
wrapped = ssl_ctx.wrap_socket(sock, server_hostname="micropython.org")
wrapped.close()
