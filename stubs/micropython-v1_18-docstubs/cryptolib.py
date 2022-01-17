"""
cryptographic ciphers. See: https://docs.micropython.org/en/v1.18/library/cryptolib.html
"""

# source version: v1_18
# origin module:: micropython/docs/library/cryptolib.rst
from typing import Any, Optional


class aes:
    def __init__(self, key, mode, IV: Optional[Any]) -> None:
        """
        Initialize cipher object, suitable for encryption/decryption. Note:
        after initialization, cipher object can be use only either for
        encryption or decryption. Running decrypt() operation after encrypt()
        or vice versa is not supported.

        Parameters are:

            * *key* is an encryption/decryption key (bytes-like).
            * *mode* is:

                * ``1`` (or ``cryptolib.MODE_ECB`` if it exists) for Electronic Code Book (ECB).
                * ``2`` (or ``cryptolib.MODE_CBC`` if it exists) for Cipher Block Chaining (CBC).
                * ``6`` (or ``cryptolib.MODE_CTR`` if it exists) for Counter mode (CTR).

            * *IV* is an initialization vector for CBC mode.
            * For Counter mode, *IV* is the initial value for the counter.
        """
        ...

    def encrypt(self, in_buf, out_buf: Optional[Any]) -> Any:
        """
        Encrypt *in_buf*. If no *out_buf* is given result is returned as a
        newly allocated `bytes` object. Otherwise, result is written into
        mutable buffer *out_buf*. *in_buf* and *out_buf* can also refer
        to the same mutable buffer, in which case data is encrypted in-place.
        """
        ...

    def decrypt(self, in_buf, out_buf: Optional[Any]) -> Any:
        """
        Like `encrypt()`, but for decryption.
        """
        ...
