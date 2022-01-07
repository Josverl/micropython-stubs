import micropython
from zlib import *


class DecompIO:

    def __init__(self, stream, dict_bits):
        self.stream = stream
        self.decomp = decompressobj(dict_bits)
        self.pending = b""


    def read(self, size):
        while len(self.pending) < size:
            inp = self.stream.read(256)
            if not inp:
                break
            outp = self.decomp.decompress(inp)
            self.pending += outp

        outp = self.pending[:size]
        self.pending = self.pending[size:]
        return outp
