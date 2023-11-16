from _typeshed import Incomplete as Incomplete
from typing import Any, Optional

class sha256:
    """
    Create an SHA256 hasher object and optionally feed ``data`` into it.
    """

    def __init__(self, data: Optional[Any] = ...) -> None: ...

class sha1:
    """
    Create an SHA1 hasher object and optionally feed ``data`` into it.
    """

    def __init__(self, data: Optional[Any] = ...) -> None: ...

class md5:
    """
    Create an MD5 hasher object and optionally feed ``data`` into it.
    """

    def __init__(self, data: Optional[Any] = ...) -> None: ...

class hash:
    """ """

    def update(self, data) -> Incomplete:
        """
        Feed more binary data into hash.
        """
    def digest(self) -> bytes:
        """
        Return hash for all data passed through hash, as a bytes object. After this
        method is called, more data cannot be fed into the hash any longer.
        """
    def hexdigest(self) -> Incomplete:
        """
        This method is NOT implemented. Use ``binascii.hexlify(hash.digest())``
        to achieve a similar effect.
        """
