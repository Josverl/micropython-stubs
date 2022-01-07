import micropython
import tarfile
from tarfile import TarInfo
from tarfile import DIRTYPE, REGTYPE


def TarFile(fileobj):
    return tarfile.TarFile.open(fileobj=fileobj, mode="r|")
