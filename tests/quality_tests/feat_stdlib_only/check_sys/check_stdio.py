import sys
from typing import BinaryIO

# verify if stdout and stderr acceppt bytes output
sys.stdout.write("foofoo")
sys.stdout.write(b"bar")
sys.stdout.flush()


sys.stderr.write("foofoo")
sys.stderr.write(b"bar")
sys.stderr.flush()


class Poller:
    def register(self, stream: BinaryIO, event: int) -> None: ...


class RemoteCommand:
    def __init__(self, poller: Poller) -> None:
        self.buf4 = bytearray(4)
        self.fout = sys.stdout.buffer
        self.fin = sys.stdin.buffer
        self.poller = poller
        self.poller.register(self.fin, 1)

    def rd_into(self, buf: bytearray, length: int) -> None:
        read = self.fin.readinto(buf, length)
        if read is None:
            return
        view = memoryview(buf)
        while read < length:
            count = self.fin.readinto(view[read:], length - read)
            if count is None:
                return
            read += count

    def begin(self, command_type: int) -> None:
        self.buf4[0] = 0x18
        self.buf4[1] = command_type
        self.fout.write(self.buf4, 2)
        self.fin.readinto(self.buf4)
        self.fin.readinto(self.buf4, 1)
