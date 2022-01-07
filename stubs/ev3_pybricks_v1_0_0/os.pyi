from typing import Any

F_OK: int
O_ACCMODE: int
O_APPEND: int
O_CREAT: int
O_EXCL: int
O_NOCTTY: int
O_NONBLOCK: int
O_RDONLY: int
O_RDWR: int
O_TRUNC: int
O_WRONLY: int
R_OK: int
W_OK: int
X_OK: int

def _exit() -> None: ...

_exit_: Any

def access() -> None: ...

access_: Any
array: Any

def chdir() -> None: ...

chdir_: Any

def check_error() -> None: ...
def close() -> None: ...

close_: Any
curdir: str

def dup() -> None: ...

dup_: Any
environ: Any
errno_: Any

class error: ...

def execvp() -> None: ...

execvp_: Any
ffilib: Any

def fork() -> None: ...

fork_: Any

def fsdecode() -> None: ...
def fsencode() -> None: ...
def getcwd() -> None: ...

getcwd_: Any

def getenv() -> None: ...

getenv_: Any

def getpid() -> None: ...

getpid_: Any

def ilistdir() -> None: ...
def kill() -> None: ...

kill_: Any
libc: Any

def listdir() -> None: ...
def makedirs() -> None: ...
def mkdir() -> None: ...

mkdir_: Any
name: str

def open() -> None: ...

open_: Any
opendir_: Any
pardir: str
path: Any

def pipe() -> None: ...

pipe_: Any

def popen() -> None: ...
def raise_error() -> None: ...
def read() -> None: ...

read_: Any
readdir_: Any

def remove() -> None: ...
def rename() -> None: ...

rename_: Any

def rmdir() -> None: ...

rmdir_: Any
sep: str

def stat() -> None: ...

stat_: Any
struct: Any

def system() -> None: ...

system_: Any

class uname:
    machine: str
    nodename: str
    release: Any
    sysname: str
    version: Any

def unlink() -> None: ...

unlink_: Any
uos: Any

def urandom() -> None: ...
def waitpid() -> None: ...

waitpid_: Any
walk: Any

def write() -> None: ...

write_: Any
