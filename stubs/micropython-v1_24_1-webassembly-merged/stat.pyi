"""
Module: 'stat' on micropython-v1.24.1-webassembly
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'webassembly', 'board': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

S_IRWXU: Final[int] = 448
S_IFSOCK: Final[int] = 49152
S_IRWXO: Final[int] = 7
UF_IMMUTABLE: Final[int] = 2
UF_NOUNLINK: Final[int] = 16
UF_NODUMP: Final[int] = 1
S_IREAD: Final[int] = 256
S_IRWXG: Final[int] = 56
UF_OPAQUE: Final[int] = 8
S_IRUSR: Final[int] = 256
S_IRGRP: Final[int] = 32
S_IROTH: Final[int] = 4
S_IWOTH: Final[int] = 2
UF_HIDDEN: Final[int] = 32768
S_IWGRP: Final[int] = 16
S_IXGRP: Final[int] = 8
S_IWRITE: Final[int] = 128
S_IWUSR: Final[int] = 128
UF_COMPRESSED: Final[int] = 32
S_ISVTX: Final[int] = 512
S_ISGID: Final[int] = 1024
S_ISUID: Final[int] = 2048
UF_APPEND: Final[int] = 4
S_IXUSR: Final[int] = 64
S_IXOTH: Final[int] = 1
ST_DEV: Final[int] = 2
S_IFREG: Final[int] = 32768
ST_CTIME: Final[int] = 9
ST_MODE: Final[int] = 0
ST_GID: Final[int] = 5
ST_INO: Final[int] = 1
SF_ARCHIVED: Final[int] = 65536
ST_ATIME: Final[int] = 7
SF_APPEND: Final[int] = 262144
SF_SNAPSHOT: Final[int] = 2097152
SF_IMMUTABLE: Final[int] = 131072
SF_NOUNLINK: Final[int] = 1048576
S_IFDIR: Final[int] = 16384
ST_MTIME: Final[int] = 8
S_IFCHR: Final[int] = 8192
_filemode_table: tuple = ()
S_IFIFO: Final[int] = 4096
S_IFLNK: Final[int] = 40960
ST_SIZE: Final[int] = 6
S_IFBLK: Final[int] = 24576
ST_NLINK: Final[int] = 3
S_IEXEC: Final[int] = 64
ST_UID: Final[int] = 4
S_ENFMT: Final[int] = 1024

def filemode(*args, **kwargs) -> Incomplete: ...
def S_ISCHR(*args, **kwargs) -> Incomplete: ...
def S_ISBLK(*args, **kwargs) -> Incomplete: ...
def S_IMODE(*args, **kwargs) -> Incomplete: ...
def S_IFMT(*args, **kwargs) -> Incomplete: ...
def S_ISSOCK(*args, **kwargs) -> Incomplete: ...
def S_ISDIR(*args, **kwargs) -> Incomplete: ...
def S_ISREG(*args, **kwargs) -> Incomplete: ...
def S_ISLNK(*args, **kwargs) -> Incomplete: ...
def S_ISFIFO(*args, **kwargs) -> Incomplete: ...
