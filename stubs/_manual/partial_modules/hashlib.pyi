# manual addition to hashlib.pyi

class _Hash(ABC):
    """
    Abstract base class for hashing algorithms that defines methods available in all algorithms.
    """

    def update(self, data: AnyReadableBuf, /) -> None:
        """
        Feed more binary data into hash.
        """

    def digest(self) -> bytes:
        """
        Return hash for all data passed through hash, as a bytes object. After this
        method is called, more data cannot be fed into the hash any longer.
        """

    def hexdigest(self) -> str:
        """
        This method is NOT implemented. Use ``binascii.hexlify(hash.digest())``
        to achieve a similar effect.
        """
