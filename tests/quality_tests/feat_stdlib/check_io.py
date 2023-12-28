import io
from typing import IO, Any, Optional

alloc_size = 512

buffer_1 = io.StringIO(alloc_size) # stub-ignore: version=<1.18.0
buffer_2 = io.BytesIO(alloc_size) # stub-ignore: version=<1.18.0

stream = open("file")

buf = io.BufferedWriter(stream, 8)  # type: ignore # TODO stdlib.io "TextIOWrapper" is incompatible with "RawIOBase"
print(buf.write(bytearray(16)))  # type: ignore # TODO  stdlib.io "bytearray" is incompatible with protocol "ReadableBuffer"


stream.close()
