from .se05x import SE05X  # noqa
from .iso7816 import SmartCard  # noqa
from micropython import const

# Secure Object Types.
EC_KEY = 0x01
AES_KEY = 0x03
DES_KEY = 0x04
HMAC_KEY = 0x05
BINARY = 0x06
USERID = 0x07
CURVE = 0x0B
SIGNATURE = 0x0C
MAC = 0x0D
CIPHER = 0x0E

# Supported EC curves.
EC_CURVE_NIST_P192 = 0x01
EC_CURVE_NIST_P224 = 0x02
EC_CURVE_NIST_P256 = 0x03
EC_CURVE_NIST_P384 = 0x04
EC_CURVE_NIST_P521 = 0x05
