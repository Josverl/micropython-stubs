from _typeshed import Incomplete

class CBOREncodeError(Exception):
    """Raised when an error occurs while serializing an object into a CBOR datastream."""

def encode_length(major_tag, length): ...
def encode_semantic(encoder, tag, value) -> None: ...
def encode_float(encoder, value) -> None: ...
def encode_int(encoder, value) -> None: ...
def encode_bytestring(encoder, value) -> None: ...
def encode_bytearray(encoder, value) -> None: ...
def encode_string(encoder, value) -> None: ...
def encode_map(encoder, value) -> None: ...
def encode_array(encoder, value) -> None: ...
def encode_boolean(encoder, value) -> None: ...
def encode_none(encoder, value) -> None: ...

cbor_encoders: Incomplete

class CBOREncoder:
    """
    Serializes objects to a byte stream using Concise Binary Object Representation.
    """

    fp: Incomplete
    def __init__(self, fp) -> None: ...
    def _find_encoder(self, obj): ...
    def write(self, data) -> None:
        """
        Write bytes to the data stream.
        :param data: the bytes to write
        """
    def encode(self, obj) -> None:
        """
        Encode the given object using CBOR.
        :param obj: the object to encode
        """

def dumps(obj, **kwargs):
    """
    Serialize an object to a bytestring.
    :param obj: the object to serialize
    :param kwargs: keyword arguments passed to :class:`~.CBOREncoder`
    :return: the serialized output
    :rtype: bytes
    """

def dump(obj, fp, **kwargs) -> None:
    """
    Serialize an object to a file.
    :param obj: the object to serialize
    :param fp: a file-like object
    :param kwargs: keyword arguments passed to :class:`~.CBOREncoder`
    """
