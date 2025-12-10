from .iso7816 import SmartCard as SmartCard
from _typeshed import Incomplete

_RESULT_OK: int
_APPLET_NAD: int
_APPLET_AID: Incomplete
_CLA_KSE05X: int
_INS_WRITE: int
_INS_READ: int
_INS_CRYPTO: int
_INS_MGMT: int
_INS_PROCESS: int
_INS_IMPORT_EXTERNAL: int
_INS_TRANSIENT: int
_INS_AUTH_OBJECT: int
_INS_ATTEST: int
_P1_DEFAULT: int
_P1_EC: int
_P1_AES: int
_P1_DES: int
_P1_HMAC: int
_P1_BINARY: int
_P1_USERID: int
_P1_CURVE: int
_P1_SIGNATURE: int
_P1_MAC: int
_P1_CIPHER: int
_P1_KEY_PRIVATE: int
_P1_KEY_PUBLIC: int
_P2_DEFAULT: int
_P2_GENERATE: int
_P2_CREATE: int
_P2_SIZE: int
_P2_SIGN: int
_P2_VERIFY: int
_P2_SESSION_CREATE: int
_P2_SESSION_CLOSE: int
_P2_VERSION: int
_P2_LIST: int
_P2_EXIST: int
_P2_DELETE_OBJECT: int
_P2_SESSION_USERID: int
_P2_DH: int
_P2_ENCRYPT_ONESHOT: int
_P2_DECRYPT_ONESHOT: int
_P2_SCP: int
_P2_ONESHOT: int
_TLV_TAG1: int
_TLV_TAG2: int
_TLV_TAG3: int
_TLV_TAG4: int
_TLV_TAG5: int
_TLV_TAG6: int
_TLV_TAG7: int
_TLV_TAG8: int
_TLV_TAG9: int
_TLV_TAG10: int
_TLV_TAG11: int
_TLV_TAG_SESSION_ID: int
_TLV_TAG_POLICY: int
_TLV_TAG_MAX_ATTEMPTS: int
_TLV_TAG_IMPORT_AUTH_DATA: int
_TLV_TAG_IMPORT_AUTH_KEY_ID: int
_TLV_TAG_POLICY_CHECK: int
_SIG_ECDSA_SHA_1: int
_SIG_ECDSA_SHA_224: int
_SIG_ECDSA_SHA_256: int
_SIG_ECDSA_SHA_384: int
_SIG_ECDSA_SHA_512: int

class I2CBus:
    addr: Incomplete
    bus: Incomplete
    def __init__(self, addr, freq) -> None: ...
    def read(self, buf): ...
    def write(self, buf) -> None: ...

class SE05X:
    rst: Incomplete
    scard: Incomplete
    bus: Incomplete
    ecdsa_algo: Incomplete
    tlv_offs: int
    tlv_buf: Incomplete
    def __init__(self, addr: int = 72, freq: int = 400000, rst=...) -> None: ...
    def _tlv_pack(self, fmt, *args) -> None: ...
    def _tlv_flush(self): ...
    def _ecdsa_algo(self, hash_size): ...
    def reset(self, reset_card: bool = True) -> None: ...
    def version(self): ...
    def read(self, obj_id, size: int = 0): ...
    def write(self, obj_id, obj_type, **kwargs) -> None: ...
    def delete(self, obj_id) -> None: ...
    def exists(self, obj_id): ...
    def sign(self, obj_id, data): ...
    def verify(self, obj_id, data, sign): ...
