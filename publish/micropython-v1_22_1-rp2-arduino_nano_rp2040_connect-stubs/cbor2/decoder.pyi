from _typeshed import Incomplete

class CBORDecodeError(Exception):
    """Raised when an error occurs deserializing a CBOR datastream."""

break_marker: Incomplete

class CBORSimpleValue:
    """
    Represents a CBOR "simple value".
    :param int value: the value (0-255)
    """

    value: Incomplete
    def __init__(self, value) -> None: ...
    def __eq__(self, other): ...
    def __repr__(self) -> str: ...

def decode_uint(decoder, subtype, allow_indefinite: bool = ...): ...
def decode_negint(decoder, subtype): ...
def decode_bytestring(decoder, subtype): ...
def decode_string(decoder, subtype): ...
def decode_array(decoder, subtype): ...
def decode_map(decoder, subtype): ...
def decode_special(decoder, subtype): ...
def decode_simple_value(decoder): ...
def decode_float16(decoder) -> None: ...
def decode_float32(decoder): ...
def decode_float64(decoder): ...

major_decoders: Incomplete
special_decoders: Incomplete

class CBORDecoder:
    """
    Deserializes a CBOR encoded byte stream.
    """

    fp: Incomplete
    def __init__(self, fp) -> None: ...
    def read(self, amount):
        """
        Read bytes from the data stream.
        :param int amount: the number of bytes to read
        """
    def decode(self):
        """
        Decode the next value from the stream.
        :raises CBORDecodeError: if there is any problem decoding the stream
        """

def loads(payload, **kwargs):
    """
    Deserialize an object from a bytestring.
    :param bytes payload: the bytestring to serialize
    :param kwargs: keyword arguments passed to :class:`~.CBORDecoder`
    :return: the deserialized object
    """

def load(fp, **kwargs):
    """
    Deserialize an object from an open file.
    :param fp: the input file (any file-like object)
    :param kwargs: keyword arguments passed to :class:`~.CBORDecoder`
    :return: the deserialized object
    """
