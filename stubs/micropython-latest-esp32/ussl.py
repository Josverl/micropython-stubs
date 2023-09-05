"""
Module: 'ussl' on micropython-v1.20.0-449-esp32-Generic_ESP32_module_with_SPIRAM_with_ESP32
"""
# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'family': 'micropython', 'build': '449', 'arch': 'xtensawin', 'ver': 'v1.20.0-449', 'cpu': 'SPIRAM'})
# Stubber: v1.13.7
from typing import Any

CERT_REQUIRED = 2 # type: int
PROTOCOL_TLS_CLIENT = 0 # type: int
PROTOCOL_TLS_SERVER = 1 # type: int
CERT_OPTIONAL = 1 # type: int
CERT_NONE = 0 # type: int
def wrap_socket(*args, **kwargs) -> Any:
    ...


class SSLContext():
    def wrap_socket(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

