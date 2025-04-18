import ssl

from typing_extensions import assert_type, get_type_hints

a = ssl.CERT_NONE
b = ssl.CERT_OPTIONAL
c = ssl.CERT_REQUIRED

# valid
ctx = ssl.SSLContext(
    protocol=ssl.PROTOCOL_TLS_SERVER  # stubs-ignore: board in ['rpi_pico_w'] or port == 'esp32'
)

# # below should NOT be available in stubs
# # test with ignoring the error - which will raise an error in pyright / mypy if it is not needed
# not_there = ssl.create_default_context()  # type : ignore

