"""
Module: 'ussl' on micropython-v1.22.0-esp32-ESP32_GENERIC
"""
# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'cpu': 'ESP32', 'mpy': 'v6.2', 'arch': 'xtensawin'}
# Stubber: v1.16.2
from _typeshed import Incomplete

MBEDTLS_VERSION = "mbed TLS 3.4.1"  # type: str
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
