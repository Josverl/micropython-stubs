from stdlib.io import *
import abc
from _typeshed import Incomplete as Incomplete
from typing import Any, IO, Optional

class FileIO(IO, metaclass=abc.ABCMeta):
    """
    This is type of a file open in binary mode, e.g. using ``open(name, "rb")``.
    You should not instantiate this class directly.
    """

    def __init__(self, *args, **kwargs) -> None: ...

class TextIOWrapper(IO, metaclass=abc.ABCMeta):
    """
    This is type of a file open in text mode, e.g. using ``open(name, "rt")``.
    You should not instantiate this class directly.
    """

    def __init__(self, *args, **kwargs) -> None: ...

class StringIO(IO, metaclass=abc.ABCMeta):
    def __init__(self, string: Optional[Any] = ...) -> None: ...

class BytesIO(IO, metaclass=abc.ABCMeta):
    """
    In-memory file-like objects for input/output. `StringIO` is used for
    text-mode I/O (similar to a normal file opened with "t" modifier).
    `BytesIO` is used for binary-mode I/O (similar to a normal file
    opened with "b" modifier). Initial contents of file-like objects
    can be specified with *string* parameter (should be normal string
    for `StringIO` or bytes object for `BytesIO`). All the usual file
    methods like ``read()``, ``write()``, ``seek()``, ``flush()``,
    ``close()`` are available on these objects, and additionally, a
    following method:
    """

    def __init__(self, string: Optional[Any] = ...) -> None: ...
    def getvalue(self) -> Incomplete:
        """
        Get the current contents of the underlying buffer which holds data.
        """

def open(name, mode: str = ..., **kwargs) -> Incomplete:
    """
    Open a file. Builtin ``open()`` function is aliased to this function.
    All ports (which provide access to file system) are required to support
    *mode* parameter, but support for other arguments vary by port.
    """
