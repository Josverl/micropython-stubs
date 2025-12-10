from _typeshed import Incomplete

ST_MODE: int
ST_INO: int
ST_DEV: int
ST_NLINK: int
ST_UID: int
ST_GID: int
ST_SIZE: int
ST_ATIME: int
ST_MTIME: int
ST_CTIME: int

def S_IMODE(mode):
    """Return the portion of the file's mode that can be set by
    os.chmod().
    """

def S_IFMT(mode):
    """Return the portion of the file's mode that describes the
    file type.
    """

S_IFDIR: int
S_IFCHR: int
S_IFBLK: int
S_IFREG: int
S_IFIFO: int
S_IFLNK: int
S_IFSOCK: int

def S_ISDIR(mode):
    """Return True if mode is from a directory."""

def S_ISCHR(mode):
    """Return True if mode is from a character special device file."""

def S_ISBLK(mode):
    """Return True if mode is from a block special device file."""

def S_ISREG(mode):
    """Return True if mode is from a regular file."""

def S_ISFIFO(mode):
    """Return True if mode is from a FIFO (named pipe)."""

def S_ISLNK(mode):
    """Return True if mode is from a symbolic link."""

def S_ISSOCK(mode):
    """Return True if mode is from a socket."""

S_ISUID: int
S_ISGID: int
S_ENFMT = S_ISGID
S_ISVTX: int
S_IREAD: int
S_IWRITE: int
S_IEXEC: int
S_IRWXU: int
S_IRUSR: int
S_IWUSR: int
S_IXUSR: int
S_IRWXG: int
S_IRGRP: int
S_IWGRP: int
S_IXGRP: int
S_IRWXO: int
S_IROTH: int
S_IWOTH: int
S_IXOTH: int
UF_NODUMP: int
UF_IMMUTABLE: int
UF_APPEND: int
UF_OPAQUE: int
UF_NOUNLINK: int
UF_COMPRESSED: int
UF_HIDDEN: int
SF_ARCHIVED: int
SF_IMMUTABLE: int
SF_APPEND: int
SF_NOUNLINK: int
SF_SNAPSHOT: int
_filemode_table: Incomplete

def filemode(mode):
    """Convert a file's mode to a string of the form '-rwxrwxrwx'."""
