"""
Module: 'ussl' on micropython-v1.21.0-esp32-Generic_ESP32_module_with_SPIRAM_with_ESP32
"""
# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'cpu': 'SPIRAM', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.14.0
from _typeshed import Incomplete

CERT_REQUIRED = 2  # type: int
PROTOCOL_TLS_CLIENT = 0  # type: int
PROTOCOL_TLS_SERVER = 1  # type: int
CERT_OPTIONAL = 1  # type: int
CERT_NONE = 0  # type: int

def wrap_socket(*args, **kwargs) -> Incomplete: ...

class SSLContext:
    def wrap_socket(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
