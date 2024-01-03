"""
Module: 'ssl' on micropython-v1.22.0-rp2-ARDUINO_NANO_RP2040_CONNECT
"""
# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'rp2', 'board': 'ARDUINO_NANO_RP2040_CONNECT', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.16.2
from _typeshed import Incomplete

MBEDTLS_VERSION = "mbed TLS 2.28.3"  # type: str
PROTOCOL_TLS_SERVER = 1  # type: int
PROTOCOL_TLS_CLIENT = 0  # type: int
CERT_NONE = 0  # type: int
CERT_REQUIRED = 2  # type: int
CERT_OPTIONAL = 1  # type: int


def wrap_socket(*args, **kwargs) -> Incomplete:
    ...


class SSLContext:
    def load_verify_locations(self, *args, **kwargs) -> Incomplete:
        ...

    def set_ciphers(self, *args, **kwargs) -> Incomplete:
        ...

    def wrap_socket(self, *args, **kwargs) -> Incomplete:
        ...

    def load_cert_chain(self, *args, **kwargs) -> Incomplete:
        ...

    def get_ciphers(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
