
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
def roundup(val: Any, align: Any) -> Any: ...
    #   0: return val+align-&~align-
    # ? 0: return val+align-&align-
class FileSection:
    def __init__(self, f: Any, content_len: Any, aligned_len: Any) -> None: ...
    def read(self, sz: Any=) -> Optional[Any]: ...
        #   0: return
        #   0: return 
        #   1: return data
        # ? 1: return data
    def readinto(self, buf: Any) -> Optional[Any]: ...
        #   0: return
        #   0: return 
        #   1: return sz
        # ? 1: return sz
    def skip(self) -> None: ...
class TarInfo:
    def __str__(self) -> Any: ...
        #   0: return %(self.name, self.type, self.size)
        # ? 0: return %Tuple[self.name, self.type, self.size]
class TarFile:
    def __init__(self, name: str=, fileobj: Any=) -> None: ...
    def next(self) -> Optional[Any]: ...
        #   0: return
        #   0: return 
        #   1: return
        #   1: return 
        #   2: return d
        # ? 2: return d
    def __iter__(self) -> Any: ...
        #   0: return self
        # ? 0: return self
    def __next__(self) -> Any: ...
        #   0: return v
        # ? 0: return v
    def extractfile(self, tarinfo: Any) -> Any: ...
        #   0: return tarinfo.subf
        # ? 0: return tarinfo.subf
