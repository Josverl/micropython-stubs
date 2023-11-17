import io

from typing import Any, IO, Optional

alloc_size = 512

buffer = io.StringIO(alloc_size) # stub-ignore: version=<1.18.0
buffer = io.BytesIO(alloc_size) # stub-ignore: version=<1.18.0

stream = open("file")

buf = io.BufferedWriter(stream, 8)  # type: ignore # TODO stdlib.io "TextIOWrapper" is incompatible with "RawIOBase"
print(buf.write(bytearray(16)))  # type: ignore # TODO  stdlib.io "bytearray" is incompatible with protocol "ReadableBuffer"


stream.close()
