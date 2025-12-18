from _typeshed import Incomplete

__version__: str
version: Incomplete

class Ext:
    """
    The Ext class facilitates creating a serializable extension object to store
    an application-defined type and data byte array.
    """

    type: Incomplete
    data: Incomplete
    def __init__(self, type, data) -> None:
        """
        Construct a new Ext object.

        Args:
            type (int): application-defined type integer
            data (bytes): application-defined data byte array

        Raises:
            TypeError:
                Type is not an integer.
            ValueError:
                Type is out of range of -128 to 127.
            TypeError:
                Data is not type \'bytes\' (Python 3) or not type \'str\' (Python 2).

        Example:
            >>> foo = umsgpack.Ext(5, b"\\x01\\x02\\x03")
            >>> umsgpack.packb({u"special stuff": foo, u"awesome": True})
            \'\\x82\\xa7awesome\\xc3\\xadspecial stuff\\xc7\\x03\\x05\\x01\\x02\\x03\'
            >>> bar = umsgpack.unpackb(_)
            >>> print(bar["special stuff"])
            Ext Object (Type: 5, Data: 01 02 03)
        """
    def __eq__(self, other):
        """
        Compare this Ext object with another for equality.
        """
    def __ne__(self, other):
        """
        Compare this Ext object with another for inequality.
        """
    def __str__(self) -> str:
        """
        String representation of this Ext object.
        """
    def __hash__(self):
        """
        Provide a hash of this Ext object.
        """

class InvalidString(bytes):
    """Subclass of bytes to hold invalid UTF-8 strings."""

_ext_class_to_type: Incomplete
_ext_type_to_class: Incomplete

def ext_serializable(ext_type):
    """
    Return a decorator to register a class for automatic packing and unpacking
    with the specified Ext type code. The application class should implement a
    `packb()` method that returns serialized bytes, and an `unpackb()` class
    method or static method that accepts serialized bytes and returns an
    instance of the application class.

    Args:
        ext_type (int): application-defined Ext type code

    Raises:
        TypeError:
            Ext type is not an integer.
        ValueError:
            Ext type is out of range of -128 to 127.
        ValueError:
            Ext type or class already registered.
    """

class PackException(Exception):
    """Base class for exceptions encountered during packing."""

class UnpackException(Exception):
    """Base class for exceptions encountered during unpacking."""

class UnsupportedTypeException(PackException):
    """Object type not supported for packing."""

class InsufficientDataException(UnpackException):
    """Insufficient data to unpack the serialized object."""

class InvalidStringException(UnpackException):
    """Invalid UTF-8 string encountered during unpacking."""

class UnsupportedTimestampException(UnpackException):
    """Unsupported timestamp format encountered during unpacking."""

class ReservedCodeException(UnpackException):
    """Reserved code encountered during unpacking."""

class UnhashableKeyException(UnpackException):
    """
    Unhashable key encountered during map unpacking.
    The serialized map cannot be deserialized into a Python dictionary.
    """

class DuplicateKeyException(UnpackException):
    """Duplicate key encountered during map unpacking."""

def _pack_integer(obj, fp, options) -> None: ...
def _pack_nil(obj, fp, options) -> None: ...
def _pack_boolean(obj, fp, options) -> None: ...
def _pack_float(obj, fp, options) -> None: ...
def _pack_string(obj, fp, options) -> None: ...
def _pack_binary(obj, fp, options) -> None: ...
def _pack_oldspec_raw(obj, fp, options) -> None: ...
def _pack_ext(obj, fp, options) -> None: ...
def _pack_array(obj, fp, options) -> None: ...
def _pack_map(obj, fp, options) -> None: ...
def pack(obj, fp, **options) -> None:
    """
    Serialize a Python object into MessagePack bytes.

    Args:
        obj: a Python object
        fp: a .write()-supporting file-like object

    Keyword Args:
        ext_handlers (dict): dictionary of Ext handlers, mapping a custom type
                             to a callable that packs an instance of the type
                             into an Ext object
        force_float_precision (str): "single" to force packing floats as
                                     IEEE-754 single-precision floats,
                                     "double" to force packing floats as
                                     IEEE-754 double-precision floats

    Returns:
        None

    Raises:
        UnsupportedTypeException(PackException):
            Object type not supported for packing.

    Example:
        >>> f = open(\'test.bin\', \'wb\')
        >>> umsgpack.pack({u"compact": True, u"schema": 0}, f)
    """

def packb(obj, **options):
    """
    Serialize a Python object into MessagePack bytes.

    Args:
        obj: a Python object

    Keyword Args:
        ext_handlers (dict): dictionary of Ext handlers, mapping a custom type
                             to a callable that packs an instance of the type
                             into an Ext object
        force_float_precision (str): "single" to force packing floats as
                                     IEEE-754 single-precision floats,
                                     "double" to force packing floats as
                                     IEEE-754 double-precision floats

    Returns:
        bytes: Serialized MessagePack bytes

    Raises:
        UnsupportedTypeException(PackException):
            Object type not supported for packing.

    Example:
        >>> umsgpack.packb({u"compact": True, u"schema": 0})
        b\'\\x82\\xa7compact\\xc3\\xa6schema\\x00\'
    """

def _read_except(fp, n): ...
def _unpack_integer(code, fp, options): ...
def _unpack_reserved(code, fp, options) -> None: ...
def _unpack_nil(code, fp, options) -> None: ...
def _unpack_boolean(code, fp, options): ...
def _unpack_float(code, fp, options): ...
def _unpack_string(code, fp, options): ...
def _unpack_binary(code, fp, options): ...
def _unpack_ext(code, fp, options): ...
def _unpack_array(code, fp, options): ...
def _deep_list_to_tuple(obj): ...
def _unpack_map(code, fp, options): ...
def _unpack(fp, options): ...
def unpack(fp, **options):
    """
    Deserialize MessagePack bytes into a Python object.

    Args:
        fp: a .read()-supporting file-like object

    Keyword Args:
        ext_handlers (dict): dictionary of Ext handlers, mapping integer Ext
                             type to a callable that unpacks an instance of
                             Ext into an object
        use_ordered_dict (bool): unpack maps into OrderedDict, instead of dict
                                 (default False)
        use_tuple (bool): unpacks arrays into tuples, instead of lists (default
                          False)
        allow_invalid_utf8 (bool): unpack invalid strings into instances of
                                   :class:`InvalidString`, for access to the
                                   bytes (default False)

    Returns:
        Python object

    Raises:
        InsufficientDataException(UnpackException):
            Insufficient data to unpack the serialized object.
        InvalidStringException(UnpackException):
            Invalid UTF-8 string encountered during unpacking.
        UnsupportedTimestampException(UnpackException):
            Unsupported timestamp format encountered during unpacking.
        ReservedCodeException(UnpackException):
            Reserved code encountered during unpacking.
        UnhashableKeyException(UnpackException):
            Unhashable key encountered during map unpacking.
            The serialized map cannot be deserialized into a Python dictionary.
        DuplicateKeyException(UnpackException):
            Duplicate key encountered during map unpacking.

    Example:
        >>> f = open('test.bin', 'rb')
        >>> umsgpack.unpackb(f)
        {'compact': True, 'schema': 0}
    """

def unpackb(s, **options):
    """
    Deserialize MessagePack bytes into a Python object.

    Args:
        s (bytes, bytearray): serialized MessagePack bytes

    Keyword Args:
        ext_handlers (dict): dictionary of Ext handlers, mapping integer Ext
                             type to a callable that unpacks an instance of
                             Ext into an object
        use_ordered_dict (bool): unpack maps into OrderedDict, instead of dict
                                 (default False)
        use_tuple (bool): unpacks arrays into tuples, instead of lists (default
                          False)
        allow_invalid_utf8 (bool): unpack invalid strings into instances of
                                   :class:`InvalidString`, for access to the
                                   bytes (default False)

    Returns:
        Python object

    Raises:
        TypeError:
            Packed data type is neither 'bytes' nor 'bytearray'.
        InsufficientDataException(UnpackException):
            Insufficient data to unpack the serialized object.
        InvalidStringException(UnpackException):
            Invalid UTF-8 string encountered during unpacking.
        UnsupportedTimestampException(UnpackException):
            Unsupported timestamp format encountered during unpacking.
        ReservedCodeException(UnpackException):
            Reserved code encountered during unpacking.
        UnhashableKeyException(UnpackException):
            Unhashable key encountered during map unpacking.
            The serialized map cannot be deserialized into a Python dictionary.
        DuplicateKeyException(UnpackException):
            Duplicate key encountered during map unpacking.

    Example:
        >>> umsgpack.unpackb(b'\\x82\\xa7compact\\xc3\\xa6schema\\x00')
        {'compact': True, 'schema': 0}
    """

def __init() -> None: ...
