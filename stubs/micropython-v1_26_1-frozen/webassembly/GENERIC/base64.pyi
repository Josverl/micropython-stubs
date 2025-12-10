__all__ = [
    "encode",
    "decode",
    "encodebytes",
    "decodebytes",
    "b64encode",
    "b64decode",
    "b32encode",
    "b32decode",
    "b16encode",
    "b16decode",
    "standard_b64encode",
    "standard_b64decode",
    "urlsafe_b64encode",
    "urlsafe_b64decode",
]

def b64encode(s, altchars=None):
    """Encode a byte string using Base64.

    s is the byte string to encode.  Optional altchars must be a byte
    string of length 2 which specifies an alternative alphabet for the
    '+' and '/' characters.  This allows an application to
    e.g. generate url or filesystem safe Base64 strings.

    The encoded byte string is returned.
    """

def b64decode(s, altchars=None, validate: bool = False):
    """Decode a Base64 encoded byte string.

    s is the byte string to decode.  Optional altchars must be a
    string of length 2 which specifies the alternative alphabet used
    instead of the '+' and '/' characters.

    The decoded string is returned.  A binascii.Error is raised if s is
    incorrectly padded.

    If validate is False (the default), non-base64-alphabet characters are
    discarded prior to the padding check.  If validate is True,
    non-base64-alphabet characters in the input result in a binascii.Error.
    """

def standard_b64encode(s):
    """Encode a byte string using the standard Base64 alphabet.

    s is the byte string to encode.  The encoded byte string is returned.
    """

def standard_b64decode(s):
    """Decode a byte string encoded with the standard Base64 alphabet.

    s is the byte string to decode.  The decoded byte string is
    returned.  binascii.Error is raised if the input is incorrectly
    padded or if there are non-alphabet characters present in the
    input.
    """

def urlsafe_b64encode(s):
    """Encode a byte string using a url-safe Base64 alphabet.

    s is the byte string to encode.  The encoded byte string is
    returned.  The alphabet uses '-' instead of '+' and '_' instead of
    '/'.
    """

def urlsafe_b64decode(s) -> None:
    """Decode a byte string encoded with the standard Base64 alphabet.

    s is the byte string to decode.  The decoded byte string is
    returned.  binascii.Error is raised if the input is incorrectly
    padded or if there are non-alphabet characters present in the
    input.

    The alphabet uses '-' instead of '+' and '_' instead of '/'.
    """

def b32encode(s):
    """Encode a byte string using Base32.

    s is the byte string to encode.  The encoded byte string is returned.
    """

def b32decode(s, casefold: bool = False, map01=None):
    """Decode a Base32 encoded byte string.

    s is the byte string to decode.  Optional casefold is a flag
    specifying whether a lowercase alphabet is acceptable as input.
    For security purposes, the default is False.

    RFC 3548 allows for optional mapping of the digit 0 (zero) to the
    letter O (oh), and for optional mapping of the digit 1 (one) to
    either the letter I (eye) or letter L (el).  The optional argument
    map01 when not None, specifies which letter the digit 1 should be
    mapped to (when map01 is not None, the digit 0 is always mapped to
    the letter O).  For security purposes the default is None, so that
    0 and 1 are not allowed in the input.

    The decoded byte string is returned.  binascii.Error is raised if
    the input is incorrectly padded or if there are non-alphabet
    characters present in the input.
    """

def b16encode(s):
    """Encode a byte string using Base16.

    s is the byte string to encode.  The encoded byte string is returned.
    """

def b16decode(s, casefold: bool = False):
    """Decode a Base16 encoded byte string.

    s is the byte string to decode.  Optional casefold is a flag
    specifying whether a lowercase alphabet is acceptable as input.
    For security purposes, the default is False.

    The decoded byte string is returned.  binascii.Error is raised if
    s were incorrectly padded or if there are non-alphabet characters
    present in the string.
    """

def encode(input, output) -> None:
    """Encode a file; input and output are binary files."""

def decode(input, output) -> None:
    """Decode a file; input and output are binary files."""

def encodebytes(s):
    """Encode a bytestring into a bytestring containing multiple lines
    of base-64 data."""

def decodebytes(s):
    """Decode a bytestring of base-64 data into a bytestring."""
