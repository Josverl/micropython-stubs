from _typeshed import Incomplete as Incomplete

class GzipFile:
    """
    This class can be used to wrap a *fileobj* which is any
    :term:`stream-like <stream>` object such as a file, socket, or stream
    (including :class:`io.BytesIO`). It is itself a stream and implements the
    standard read/readinto/write/close methods.

    When the *mode* argument is ``"rb"``, reads from the GzipFile instance will
    decompress the data in the underlying stream and return decompressed data.

    If compression support is enabled then the *mode* argument can be set to
    ``"wb"``, and writes to the GzipFile instance will be compressed and written
    to the underlying stream.

    By default the GzipFile class will read and write data using the gzip file
    format, including a header and footer with checksum and a window size of 512
    bytes.

    The **file**, **compresslevel**, and **mtime** arguments are not
    supported. **fileobj** and **mode** must always be specified as keyword
    arguments.
    """

    def __init__(self, *, fileobj, mode) -> None: ...

def open(filename, mode) -> Incomplete:
    """
    Wrapper around built-in :func:`open` returning a GzipFile instance.
    """

def decompress(data) -> Incomplete:
    """
    Decompresses *data* into a bytes object.
    """

def compress(data) -> Incomplete:
    """
    Compresses *data* into a bytes object.
    """
